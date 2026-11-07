"""Reproducible exploratory analysis and cleaning for the house-price dataset."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = PROJECT_DIR / "raw_data.csv"
DEFAULT_OUTPUT_DIR = PROJECT_DIR
TARGET = "price"
NUMERIC_COLUMNS = [
    "price",
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
]

sns.set_theme(style="whitegrid", context="notebook", palette="deep")
plt.rcParams.update(
    {
        "figure.dpi": 120,
        "savefig.dpi": 180,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "font.size": 9,
    }
)


def load_data(input_path: Path) -> pd.DataFrame:
    """Load the source CSV and standardize column names and text values."""
    if not input_path.is_file():
        raise FileNotFoundError(f"Input dataset was not found: {input_path}")

    frame = pd.read_csv(input_path)
    frame.columns = (
        frame.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )
    for column in frame.select_dtypes(include="object").columns:
        frame[column] = frame[column].str.strip()
        frame[column] = frame[column].replace("", np.nan)

    required = {"date", TARGET, "yr_built", "yr_renovated"}
    missing_columns = required.difference(frame.columns)
    if missing_columns:
        raise ValueError(f"Required columns are missing: {sorted(missing_columns)}")

    for column in NUMERIC_COLUMNS:
        if column in frame.columns:
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    return frame


def make_audit_tables(frame: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Build quality, summary, category, and IQR outlier audit tables."""
    row_count = len(frame)
    missing = frame.isna().sum().rename("missing_count").to_frame()
    missing["missing_percent"] = (
        missing["missing_count"].div(row_count).mul(100).round(2)
        if row_count
        else 0.0
    )
    missing.index.name = "column"

    numeric = frame.select_dtypes(include="number")
    numeric_summary = numeric.describe().T
    numeric_summary.index.name = "column"
    numeric_summary = numeric_summary.reset_index()

    categorical_parts = []
    for column in frame.select_dtypes(include=["object", "category"]).columns:
        categorical_parts.append(
            pd.DataFrame(
                [
                    {
                        "column": column,
                        "unique_values": frame[column].nunique(dropna=True),
                        "most_frequent_value": frame[column].mode().iloc[0]
                        if not frame[column].mode().empty
                        else np.nan,
                        "most_frequent_count": int(
                            frame[column].value_counts(dropna=False).max()
                        )
                        if not frame[column].empty
                        else 0,
                    }
                ]
            )
        )
    categorical_summary = (
        pd.concat(categorical_parts, ignore_index=True)
        if categorical_parts
        else pd.DataFrame(
            columns=[
                "column",
                "unique_values",
                "most_frequent_value",
                "most_frequent_count",
            ]
        )
    )

    outlier_rows = []
    for column in numeric.columns:
        values = numeric[column].dropna().to_numpy(dtype=float)
        if values.size == 0:
            continue
        q1, q3 = np.quantile(values, [0.25, 0.75])
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        outlier_rows.append(
            {
                "column": column,
                "lower_fence": lower_fence,
                "upper_fence": upper_fence,
                "outlier_count": int(((values < lower_fence) | (values > upper_fence)).sum()),
                "outlier_percent": float(
                    (((values < lower_fence) | (values > upper_fence)).mean()) * 100
                ),
            }
        )
    outliers = pd.DataFrame(outlier_rows)

    return {
        "missing_values": missing.reset_index(),
        "numeric_summary": numeric_summary,
        "categorical_summary": categorical_summary,
        "iqr_outliers": outliers,
    }


def clean_data(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    """Apply conservative, documented cleaning and derive model features."""
    initial_rows = len(frame)
    duplicate_count = int(frame.duplicated().sum())
    cleaned = frame.drop_duplicates().copy()

    invalid_target = cleaned[TARGET].isna() | cleaned[TARGET].le(0)
    invalid_target_count = int(invalid_target.sum())
    cleaned = cleaned.loc[~invalid_target].copy()

    invalid_date = int(cleaned["date"].isna().sum())
    cleaned = cleaned.dropna(subset=["date"]).copy()
    cleaned["sale_year"] = cleaned["date"].dt.year.astype("int64")
    cleaned["sale_month"] = cleaned["date"].dt.month.astype("int64")

    invalid_renovation = cleaned["yr_renovated"].notna() & (
        cleaned["yr_renovated"].ne(0)
        & (
            cleaned["yr_renovated"].lt(cleaned["yr_built"])
            | cleaned["yr_renovated"].gt(cleaned["sale_year"])
        )
    )
    invalid_renovation_count = int(invalid_renovation.sum())
    valid_renovation = (
        cleaned["yr_renovated"].gt(0)
        & ~invalid_renovation
        & cleaned["yr_renovated"].notna()
    )
    cleaned["has_renovation"] = valid_renovation.astype("int8")
    cleaned["years_since_renovation"] = np.where(
        valid_renovation,
        cleaned["sale_year"] - cleaned["yr_renovated"],
        0,
    ).astype("int64")

    zero_bedrooms = cleaned["bedrooms"].eq(0)
    zero_bathrooms = cleaned["bathrooms"].eq(0)
    zero_bedroom_count = int(zero_bedrooms.sum())
    zero_bathroom_count = int(zero_bathrooms.sum())
    cleaned.loc[zero_bedrooms, "bedrooms"] = np.nan
    cleaned.loc[zero_bathrooms, "bathrooms"] = np.nan

    cleaned["house_age"] = cleaned["sale_year"] - cleaned["yr_built"]
    cleaned = cleaned.drop(
        columns=[
            column
            for column in ["date", "street", "country", "yr_built", "yr_renovated"]
            if column in cleaned.columns
        ]
    )
    cleaned = cleaned.reset_index(drop=True)

    changes = {
        "input_rows": initial_rows,
        "exact_duplicates_removed": duplicate_count,
        "nonpositive_or_missing_price_rows_removed": invalid_target_count,
        "invalid_dates_removed": invalid_date,
        "invalid_renovation_years": invalid_renovation_count,
        "zero_bedroom_values_set_missing": zero_bedroom_count,
        "zero_bathroom_values_set_missing": zero_bathroom_count,
        "output_rows": len(cleaned),
    }
    return cleaned, changes


def create_dashboard(frame: pd.DataFrame, output_path: Path) -> None:
    """Save a six-panel EDA dashboard using the cleaned observations."""
    fig, axes = plt.subplots(3, 2, figsize=(15, 17))
    fig.suptitle("House Prices | Exploratory Data Analysis", fontsize=18, weight="bold")
    ax_price, ax_area, ax_city, ax_corr, ax_missing, ax_bedrooms = axes.flat

    sns.histplot(
        data=frame,
        x=TARGET,
        bins=45,
        log_scale=True,
        color="#2878B5",
        ax=ax_price,
    )
    ax_price.set_title("Sale price distribution (log scale)")
    ax_price.set_xlabel("Sale price ($)")
    ax_price.set_ylabel("Number of homes")

    sns.scatterplot(
        data=frame,
        x="sqft_living",
        y=TARGET,
        alpha=0.35,
        s=22,
        color="#D9534F",
        edgecolor=None,
        ax=ax_area,
    )
    ax_area.set_yscale("log")
    ax_area.set_title("Living area vs. sale price")
    ax_area.set_xlabel("Living area (sq ft)")
    ax_area.set_ylabel("Sale price ($, log scale)")

    city_prices = (
        frame.groupby("city", observed=True)[TARGET]
        .agg(["median", "count"])
        .query("count >= 10")
        .nlargest(10, "median")
        .sort_values("median")
    )
    sns.barplot(
        data=city_prices.reset_index(),
        x="median",
        y="city",
        color="#59A14F",
        ax=ax_city,
    )
    ax_city.set_title("Median sale price by city (10+ records)")
    ax_city.set_xlabel("Median sale price ($)")
    ax_city.set_ylabel("")
    ax_city.xaxis.set_major_formatter(
        plt.FuncFormatter(lambda value, _: f"${value / 1_000:,.0f}k")
    )

    correlation_columns = [
        column
        for column in [
            "price",
            "bedrooms",
            "bathrooms",
            "sqft_living",
            "sqft_lot",
            "floors",
            "waterfront",
            "view",
            "condition",
            "sqft_above",
            "sqft_basement",
            "house_age",
            "has_renovation",
            "years_since_renovation",
        ]
        if column in frame.columns
    ]
    correlation = frame[correlation_columns].corr(method="spearman")
    mask = np.triu(np.ones_like(correlation, dtype=bool), k=1)
    sns.heatmap(
        correlation,
        mask=mask,
        cmap="vlag",
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.4,
        cbar_kws={"shrink": 0.75},
        ax=ax_corr,
    )
    ax_corr.set_title("Spearman rank correlations")
    ax_corr.tick_params(axis="x", labelrotation=55)

    missing = frame.isna().mean().mul(100)
    missing = missing.loc[missing.gt(0)].sort_values()
    if missing.empty:
        ax_missing.text(
            0.5,
            0.5,
            "No missing values",
            ha="center",
            va="center",
            fontsize=13,
            transform=ax_missing.transAxes,
        )
        ax_missing.set_axis_off()
    else:
        sns.barplot(
            x=missing.values,
            y=missing.index,
            color="#F28E2B",
            ax=ax_missing,
        )
        ax_missing.set_title("Missing feature values after cleaning")
        ax_missing.set_xlabel("Rows missing (%)")
        ax_missing.set_ylabel("")

    bedroom_counts = frame["bedrooms"].value_counts()
    supported_bedrooms = sorted(bedroom_counts.loc[bedroom_counts.ge(10)].index)
    bedroom_data = frame.loc[frame["bedrooms"].isin(supported_bedrooms)]
    sns.boxplot(
        data=bedroom_data,
        x="bedrooms",
        y=TARGET,
        order=supported_bedrooms,
        showfliers=False,
        color="#76B7B2",
        ax=ax_bedrooms,
    )
    ax_bedrooms.set_yscale("log")
    ax_bedrooms.set_title("Sale price by bedrooms (log scale; outliers hidden)")
    ax_bedrooms.set_xlabel("Bedrooms (sample size)")
    ax_bedrooms.set_ylabel("Sale price ($, log scale)")
    ax_bedrooms.set_xticks(
        range(len(supported_bedrooms)),
        labels=[
            f"{int(bedrooms)}\n(n={int(bedroom_counts[bedrooms]):,})"
            for bedrooms in supported_bedrooms
        ],
    )

    fig.tight_layout(rect=(0, 0, 1, 0.97))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def write_report(
    raw: pd.DataFrame,
    cleaned: pd.DataFrame,
    changes: dict[str, int],
    audit: dict[str, pd.DataFrame],
    report_path: Path,
) -> None:
    """Write a concise, data-specific EDA and cleaning report."""
    prices = raw[TARGET].dropna()
    positive_prices = prices.loc[prices.gt(0)]
    price_outliers = audit["iqr_outliers"].set_index("column").loc[TARGET]
    missing_feature_counts = cleaned.isna().sum()
    missing_feature_counts = missing_feature_counts.loc[missing_feature_counts.gt(0)]
    city_counts = raw["city"].value_counts().head(5)
    price_median = positive_prices.median()
    price_mean = positive_prices.mean()
    skewness = positive_prices.skew()

    lines = [
        "HOUSE PRICE DATASET — EDA AND CLEANING REPORT",
        "=" * 52,
        "",
        "Dataset scope",
        f"- Raw observations and fields: {raw.shape[0]:,} rows x {raw.shape[1]:,} columns",
        f"- Cleaned observations and fields: {cleaned.shape[0]:,} rows x {cleaned.shape[1]:,} columns",
        f"- Sale date range: {raw['date'].min().date()} to {raw['date'].max().date()}",
        f"- Exact duplicate rows found: {changes['exact_duplicates_removed']:,}",
        f"- Missing cells in raw input: {int(raw.isna().sum().sum()):,}",
        "",
        "Target analysis",
        "- Non-positive/missing sale-price rows removed: "
        f"{changes['nonpositive_or_missing_price_rows_removed']:,}",
        f"- Median positive sale price: ${price_median:,.0f}",
        f"- Mean positive sale price: ${price_mean:,.0f}",
        f"- Positive-price skewness: {skewness:.2f}",
        f"- Positive-price range: ${positive_prices.min():,.0f} to ${positive_prices.max():,.0f}",
        f"- Price observations beyond the 1.5xIQR fences: {int(price_outliers['outlier_count']):,} "
        f"({price_outliers['outlier_percent']:.2f}%)",
        "",
        "Data quality findings and treatment",
        f"- Rows removed for exact duplication: {changes['exact_duplicates_removed']:,}.",
        f"- Rows excluded for a non-positive/missing target: "
        f"{changes['nonpositive_or_missing_price_rows_removed']:,}.",
        f"- Invalid sale dates removed: {changes['invalid_dates_removed']:,}.",
        f"- Invalid renovation years (before construction or after sale): "
        f"{changes['invalid_renovation_years']:,}; treated as no reliable renovation evidence.",
        f"- Zero bedroom values set to missing: {changes['zero_bedroom_values_set_missing']:,}.",
        f"- Zero bathroom values set to missing: {changes['zero_bathroom_values_set_missing']:,}.",
        "- `street` was excluded because it is a near-unique address identifier; `country` "
        "was excluded because it is constant.",
        "- Sale date was decomposed into sale year/month; construction and renovation years "
        "were represented as house age, a renovation indicator, and years since renovation.",
        "- Missing feature values are retained. Fit imputers on training folds only to avoid "
        "validation/test leakage.",
        "",
        "Potential outliers",
        "- IQR fences are a screening device, not proof of data error. No positive-price "
        "observations were removed solely for being extreme.",
        "- Inspect the extreme-price and large-lot records against source/business context "
        "before deciding on a transformation, robust loss, or exclusion rule.",
        "",
        "Geographic coverage",
        "- Most frequent cities: "
        + ", ".join(f"{city} ({count:,})" for city, count in city_counts.items()),
        "",
        "Training recommendations",
        "- Define `price` as the target and use a train/validation/test split before fitting "
        "imputation, scaling, encoding, or feature selection.",
        "- Keep `city` and `statezip` as categorical features and encode them inside a "
        "training pipeline; check category coverage in held-out data.",
        "- Evaluate target skew and residuals; compare a raw-price model with a log-target "
        "approach using metrics reported in dollars.",
        "- Consider a geographic-aware split or grouped validation because homes in nearby "
        "areas can share pricing patterns.",
        "",
        "Generated artifacts",
        "- data/cleaned_house_prices.csv",
        "- reports/missing_values.csv, reports/numeric_summary.csv,",
        "  reports/categorical_summary.csv, reports/iqr_outliers.csv",
        "- visualizations/house_price_eda_dashboard.png",
    ]
    if not missing_feature_counts.empty:
        lines.extend(
            [
                "",
                "Remaining missing model features",
                *[
                    f"- {column}: {int(count):,} ({count / len(cleaned) * 100:.2f}%)"
                    for column, count in missing_feature_counts.items()
                ],
            ]
        )

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_analysis(input_path: Path, output_dir: Path) -> None:
    raw = load_data(input_path)
    audit = make_audit_tables(raw)
    cleaned, changes = clean_data(raw)

    data_dir = output_dir / "data"
    reports_dir = output_dir / "reports"
    visualizations_dir = output_dir / "visualizations"
    data_dir.mkdir(parents=True, exist_ok=True)
    reports_dir.mkdir(parents=True, exist_ok=True)

    cleaned.to_csv(data_dir / "cleaned_house_prices.csv", index=False)
    for name, table in audit.items():
        table.to_csv(reports_dir / f"{name}.csv", index=False)
    create_dashboard(cleaned, visualizations_dir / "house_price_eda_dashboard.png")
    write_report(raw, cleaned, changes, audit, reports_dir / "eda_report.txt")

    print(f"Input: {input_path}")
    print(f"Rows: {len(raw):,} -> {len(cleaned):,}")
    print(
        "Removed "
        f"{changes['exact_duplicates_removed']:,} duplicates and "
        f"{changes['nonpositive_or_missing_price_rows_removed']:,} invalid targets."
    )
    print(f"Cleaned dataset: {data_dir / 'cleaned_house_prices.csv'}")
    print(f"EDA report: {reports_dir / 'eda_report.txt'}")
    print(f"Dashboard: {visualizations_dir / 'house_price_eda_dashboard.png'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Profile, clean, and visualize the house-price dataset."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Path to raw_data.csv (defaults to the file beside this script).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Project directory for data/, reports/, and visualizations/ outputs.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    run_analysis(arguments.input, arguments.output_dir)
