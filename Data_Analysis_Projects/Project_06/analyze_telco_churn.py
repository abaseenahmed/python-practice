from __future__ import annotations

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
SOURCE_PATH = DATA_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
CLEANED_PATH = PROJECT_DIR / "cleaned_data.csv"
REPORT_PATH = PROJECT_DIR / "eda_report.md"
PLOT_DIR = PROJECT_DIR / "visualizations"

EXPECTED_CATEGORIES = {
    "gender": {"Female", "Male"},
    "Partner": {"No", "Yes"},
    "Dependents": {"No", "Yes"},
    "PhoneService": {"No", "Yes"},
    "MultipleLines": {"No", "Yes", "No phone service"},
    "InternetService": {"DSL", "Fiber optic", "No"},
    "OnlineSecurity": {"No", "Yes", "No internet service"},
    "OnlineBackup": {"No", "Yes", "No internet service"},
    "DeviceProtection": {"No", "Yes", "No internet service"},
    "TechSupport": {"No", "Yes", "No internet service"},
    "StreamingTV": {"No", "Yes", "No internet service"},
    "StreamingMovies": {"No", "Yes", "No internet service"},
    "Contract": {"Month-to-month", "One year", "Two year"},
    "PaperlessBilling": {"No", "Yes"},
    "PaymentMethod": {
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check",
    },
    "Churn": {"No", "Yes"},
}

DEMOGRAPHIC_COLUMNS = ["gender", "SeniorCitizen", "Partner", "Dependents"]
ACCOUNT_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges"]
CONTRACT_COLUMNS = ["Contract", "PaymentMethod", "PaperlessBilling"]
SERVICE_COLUMNS = [
    "InternetService",
    "OnlineSecurity",
    "TechSupport",
    "OnlineBackup",
    "DeviceProtection",
    "StreamingTV",
    "StreamingMovies",
]

sns.set_theme(style="whitegrid", context="notebook")


def percent(value: float) -> str:
    return f"{value:.1%}"


def category_churn_rates(data: pd.DataFrame, column: str) -> pd.Series:
    return (
        data.groupby(column, observed=False)["ChurnFlag"]
        .mean()
        .sort_values(ascending=False)
    )


def label_for(column: str, value: object) -> str:
    if column == "SeniorCitizen":
        return "Senior" if value == 1 else "Not senior"
    return str(value)


def add_churn_rate_chart(
    ax: plt.Axes, data: pd.DataFrame, column: str, title: str
) -> pd.Series:
    rates = category_churn_rates(data, column)
    labels = [label_for(column, value) for value in rates.index]
    bars = ax.bar(labels, rates.values, color=sns.color_palette("crest", len(rates)))
    ax.bar_label(bars, labels=[percent(rate) for rate in rates.values], padding=3)
    ax.set_ylim(0, min(1.0, max(0.5, float(rates.max()) * 1.2)))
    ax.set_ylabel("Customers who churned")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda value, _: f"{value:.0%}"))
    ax.set_title(title)
    ax.tick_params(axis="x", rotation=20)
    return rates


def rate_observation(column: str, data: pd.DataFrame) -> str:
    rates = category_churn_rates(data, column)
    highest, lowest = rates.index[0], rates.index[-1]
    return (
        f"- **{column}:** {label_for(column, highest)} has the highest observed "
        f"churn rate ({percent(rates.iloc[0])}); {label_for(column, lowest)} has "
        f"the lowest ({percent(rates.iloc[-1])}). These are descriptive "
        "associations, not evidence that the category causes churn."
    )


def main() -> None:
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(
            f"Original Kaggle CSV not found at {SOURCE_PATH}. Download it from "
            "https://www.kaggle.com/datasets/blastchar/telco-customer-churn"
        )

    original = pd.read_csv(SOURCE_PATH)
    required_columns = {
        "customerID",
        "gender",
        "SeniorCitizen",
        "Partner",
        "Dependents",
        "tenure",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod",
        "MonthlyCharges",
        "TotalCharges",
        "Churn",
    }
    if missing_columns := required_columns - set(original.columns):
        raise ValueError(f"Source CSV is missing required columns: {sorted(missing_columns)}")

    initial_info = StringIO()
    with redirect_stdout(initial_info):
        original.info()
    initial_description = original.describe(include="all").to_string()
    initial_head = original.head().to_string(index=False)
    initial_missing = original.isnull().sum()
    initial_nunique = original.nunique(dropna=False)
    initial_duplicate_rows = int(original.duplicated().sum())
    initial_duplicate_ids = int(original["customerID"].duplicated().sum())

    cleaned = original.copy()
    trimmed_cell_count = 0
    for column in cleaned.select_dtypes(include="object").columns:
        trimmed = cleaned[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )
        trimmed_cell_count += int(cleaned[column].ne(trimmed).sum())
        cleaned[column] = trimmed

    if initial_duplicate_rows:
        cleaned = cleaned.drop_duplicates().copy()
    if cleaned["customerID"].duplicated().any():
        duplicates = cleaned.loc[
            cleaned["customerID"].duplicated(keep=False), "customerID"
        ].unique()
        raise ValueError(
            "Duplicate customer IDs need explicit resolution; refusing to discard "
            f"records: {duplicates[:10].tolist()}"
        )

    total_charges_text = cleaned["TotalCharges"].astype("string").str.strip()
    blank_total_charges = total_charges_text.eq("")
    total_charges_numeric = pd.to_numeric(
        total_charges_text.mask(blank_total_charges), errors="coerce"
    )
    invalid_total_charges = total_charges_numeric.isna() & ~blank_total_charges
    if invalid_total_charges.any():
        bad_values = total_charges_text.loc[invalid_total_charges].unique().tolist()
        raise ValueError(f"Unparseable nonblank TotalCharges values: {bad_values}")
    blank_rows_have_zero_tenure = cleaned.loc[blank_total_charges, "tenure"].eq(0)
    if not blank_rows_have_zero_tenure.all():
        raise ValueError(
            "Blank TotalCharges values are not all zero-tenure records; "
            "their cause must be reviewed before imputation."
        )
    cleaned["TotalCharges"] = total_charges_numeric.fillna(0).astype(float)

    unexpected_categories: dict[str, list[str]] = {}
    for column, expected in EXPECTED_CATEGORIES.items():
        observed = set(cleaned[column].dropna().unique())
        unexpected = observed - expected
        if unexpected:
            unexpected_categories[column] = sorted(map(str, unexpected))
    if unexpected_categories:
        raise ValueError(f"Unexpected categorical values: {unexpected_categories}")

    cleaned["SeniorCitizen"] = pd.to_numeric(
        cleaned["SeniorCitizen"], errors="raise"
    ).astype(int)
    for column in ["tenure", "MonthlyCharges", "TotalCharges"]:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="raise")

    if not cleaned["SeniorCitizen"].isin([0, 1]).all():
        raise ValueError("SeniorCitizen must contain only 0 and 1.")
    if not cleaned["tenure"].between(0, 72).all():
        raise ValueError("tenure values must be between 0 and 72 months.")
    if (cleaned[["MonthlyCharges", "TotalCharges"]] < 0).any().any():
        raise ValueError("Charge columns must not contain negative values.")
    if cleaned.isnull().any().any():
        raise ValueError(
            "Missing values remain after cleaning: "
            f"{cleaned.isnull().sum()[cleaned.isnull().sum() > 0].to_dict()}"
        )

    cleaned["ChurnFlag"] = cleaned["Churn"].eq("Yes").astype(int)
    numeric_features = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]
    model_view = cleaned.drop(columns="ChurnFlag")
    model_view.to_csv(CLEANED_PATH, index=False)

    PLOT_DIR.mkdir(exist_ok=True)
    report_lines = [
        "# Telco Customer Churn: Data Preparation and EDA",
        "",
        f"Source: [Kaggle IBM Telco Customer Churn dataset]"
        "(https://www.kaggle.com/datasets/blastchar/telco-customer-churn).",
        "The original source CSV is retained unchanged in `data/`; "
        "`customerID` is retained for identification and must be excluded from "
        "model features. No model-specific encoding or scaling has been applied.",
        "",
        "## Initial inspection",
        "",
        f"- Shape: {original.shape[0]:,} rows × {original.shape[1]} columns.",
        f"- Exact duplicate rows: {initial_duplicate_rows:,}.",
        f"- Duplicate `customerID` values: {initial_duplicate_ids:,}.",
        f"- Whitespace-only changes made to categorical/text cells: {trimmed_cell_count:,}.",
        f"- Blank `TotalCharges` strings: {int(blank_total_charges.sum()):,}.",
        "",
        "### `head()`",
        "",
        "```text",
        initial_head,
        "```",
        "",
        "### `info()`",
        "",
        "```text",
        initial_info.getvalue().rstrip(),
        "```",
        "",
        "### `describe()`",
        "",
        "```text",
        initial_description,
        "```",
        "",
        "### Missing values, duplicates, and unique values",
        "",
        f"- `isnull().sum()`: {initial_missing.to_dict()}",
        f"- `duplicated().sum()`: {initial_duplicate_rows}",
        f"- `customerID.duplicated().sum()`: {initial_duplicate_ids}",
        f"- `nunique()`: {initial_nunique.to_dict()}",
        "",
        "## Cleaning decisions and validation",
        "",
        f"- Removed {initial_duplicate_rows:,} exact duplicate row(s); no duplicate "
        "customer IDs were found. Duplicate IDs would stop the script for explicit "
        "review rather than silently discarding a customer record.",
        f"- Stripped surrounding whitespace from text values ({trimmed_cell_count:,} "
        "cells changed); all categorical values match the expected source categories.",
        "- `TotalCharges` was parsed as numeric. Its 11 blank source strings all "
        "belong to customers with `tenure == 0`, consistent with newly opened "
        "accounts having no accumulated charges; those values are set to 0.0, "
        "and all 11 records are retained.",
        "- `No internet service` and `No phone service` are valid states and remain "
        "unchanged; they are not treated as missing values.",
        "- `customerID` remains in the cleaned file. Drop it from the eventual "
        "training feature matrix to avoid using an identifier as a predictor.",
        "- Range checks passed: `SeniorCitizen` is binary, `tenure` is 0–72 months, "
        "and charge values are nonnegative.",
        "",
        "### Numeric ranges and IQR outlier flags",
        "",
        "Outlier flags below use the 1.5×IQR rule for review only. No valid records "
        "were deleted on the basis of an outlier flag.",
    ]
    for column in ["tenure", "MonthlyCharges", "TotalCharges"]:
        series = cleaned[column]
        q1, q3 = series.quantile([0.25, 0.75])
        iqr = q3 - q1
        lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        flagged = int(((series < lower) | (series > upper)).sum())
        report_lines.append(
            f"- `{column}`: min={series.min():g}, Q1={q1:g}, median={series.median():g}, "
            f"Q3={q3:g}, max={series.max():g}; IQR review bounds "
            f"[{lower:.2f}, {upper:.2f}], flagged={flagged:,}."
        )
    report_lines.extend(
        [
            "",
            "## EDA and visual observations",
            "",
        ]
    )

    churn_counts = cleaned["Churn"].value_counts().reindex(["No", "Yes"], fill_value=0)
    churn_percentages = churn_counts / len(cleaned)
    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(
        ["Stayed", "Churned"],
        [churn_counts["No"], churn_counts["Yes"]],
        color=["#4C9F70", "#D95D5D"],
    )
    ax.bar_label(
        bars,
        labels=[
            f"{int(churn_counts['No']):,}\n{percent(churn_percentages['No'])}",
            f"{int(churn_counts['Yes']):,}\n{percent(churn_percentages['Yes'])}",
        ],
        padding=3,
    )
    ax.set_title("Customer churn distribution")
    ax.set_ylabel("Customers")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "01_churn_distribution.png", dpi=160)
    plt.close(fig)
    report_lines.extend(
        [
            "### Churn distribution (`01_churn_distribution.png`)",
            f"- {int(churn_counts['No']):,} customers ({percent(churn_percentages['No'])}) "
            f"stayed and {int(churn_counts['Yes']):,} ({percent(churn_percentages['Yes'])}) "
            "churned. The class distribution is imbalanced, so later model evaluation "
            "should include precision/recall, ROC-AUC or PR-AUC, and a stratified split "
            "rather than accuracy alone.",
            "",
        ]
    )

    demographic_data = cleaned.copy()
    demographic_data["SeniorCitizen"] = demographic_data["SeniorCitizen"].map(
        {0: "No", 1: "Yes"}
    )
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    for ax, column in zip(axes.flat, DEMOGRAPHIC_COLUMNS):
        sns.countplot(
            data=demographic_data,
            x=column,
            hue="Churn",
            order=sorted(demographic_data[column].dropna().unique()),
            hue_order=["No", "Yes"],
            ax=ax,
        )
        ax.set_title(f"Churn by {column}")
        ax.set_ylabel("Customers")
        ax.tick_params(axis="x", rotation=15)
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "02_demographics.png", dpi=160)
    plt.close(fig)
    report_lines.extend(["### Demographics (`02_demographics.png`)", ""])
    for column in DEMOGRAPHIC_COLUMNS:
        report_lines.append(rate_observation(column, cleaned))
    report_lines.append("")

    fig, axes = plt.subplots(3, 2, figsize=(14, 14))
    for row, column in enumerate(ACCOUNT_COLUMNS):
        sns.histplot(
            data=cleaned,
            x=column,
            hue="Churn",
            hue_order=["No", "Yes"],
            stat="density",
            common_norm=False,
            element="step",
            fill=False,
            ax=axes[row, 0],
        )
        axes[row, 0].set_title(f"{column} distribution by churn")
        sns.boxplot(data=cleaned, x="Churn", y=column, order=["No", "Yes"], ax=axes[row, 1])
        axes[row, 1].set_title(f"{column} by churn")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "03_account_distributions.png", dpi=160)
    plt.close(fig)
    report_lines.extend(
        [
            "### Account distributions (`03_account_distributions.png`)",
            "",
        ]
    )
    for column in ACCOUNT_COLUMNS:
        medians = cleaned.groupby("Churn")[column].median()
        direction = (
            "higher" if medians["Yes"] > medians["No"] else "lower"
        )
        report_lines.append(
            f"- **{column}:** The churned group has a {direction} median "
            f"({medians['Yes']:.2f}) than the retained group ({medians['No']:.2f}). "
            "The histogram and boxplot show the distribution and spread; the "
            "relationship is observational."
        )
    report_lines.append("")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    for ax, column in zip(axes, CONTRACT_COLUMNS):
        add_churn_rate_chart(ax, cleaned, column, f"Churn rate by {column}")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "04_contract_and_payment.png", dpi=160)
    plt.close(fig)
    report_lines.extend(
        [
            "### Contracts, payments, and billing (`04_contract_and_payment.png`)",
            "",
        ]
    )
    report_lines.extend(rate_observation(column, cleaned) for column in CONTRACT_COLUMNS)
    report_lines.append("")

    fig, axes = plt.subplots(2, 4, figsize=(19, 10))
    for ax, column in zip(axes.flat, SERVICE_COLUMNS):
        add_churn_rate_chart(ax, cleaned, column, f"Churn rate by {column}")
    axes.flat[-1].axis("off")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "05_services.png", dpi=160)
    plt.close(fig)
    report_lines.extend(["### Services (`05_services.png`)", ""])
    report_lines.extend(rate_observation(column, cleaned) for column in SERVICE_COLUMNS)
    report_lines.append(
        "- In `OnlineSecurity`, `TechSupport`, `OnlineBackup`, `DeviceProtection`, "
        "`StreamingTV`, and `StreamingMovies`, `No internet service` remains a valid "
        "separate category; its plotted rate is not a missing-value artifact."
    )
    report_lines.append("")

    correlation_data = cleaned[numeric_features].copy()
    correlation_data["ChurnFlag"] = cleaned["ChurnFlag"]
    correlation = correlation_data.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="vlag",
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        ax=ax,
    )
    ax.set_title("Numeric-feature and churn correlation")
    fig.tight_layout()
    fig.savefig(PLOT_DIR / "06_correlation_heatmap.png", dpi=160)
    plt.close(fig)
    churn_correlations = correlation["ChurnFlag"].drop("ChurnFlag").sort_values()
    strongest_negative = churn_correlations.index[0]
    strongest_positive = churn_correlations.index[-1]
    report_lines.extend(
        [
            "### Correlation heatmap (`06_correlation_heatmap.png`)",
            f"- Among the displayed numeric variables, `{strongest_negative}` has the "
            f"strongest negative linear correlation with the binary churn indicator "
            f"(r={churn_correlations[strongest_negative]:.2f}); "
            f"`{strongest_positive}` has the strongest positive correlation "
            f"(r={churn_correlations[strongest_positive]:.2f}). This is a compact "
            "linear summary, not a causal result; categorical features are not included "
            "in this numeric-only heatmap.",
            "",
            "## Business insights",
            "",
        ]
    )

    def rate(column: str, category: object) -> float:
        return float(category_churn_rates(cleaned, column).loc[category])

    month_to_month = rate("Contract", "Month-to-month")
    two_year = rate("Contract", "Two year")
    electronic_check = rate("PaymentMethod", "Electronic check")
    tenure_bins = pd.cut(
        cleaned["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=["0–12", "13–24", "25–48", "49–72"],
    )
    tenure_rates = cleaned.groupby(tenure_bins, observed=False)["ChurnFlag"].mean()
    early_rate, long_rate = float(tenure_rates.loc["0–12"]), float(tenure_rates.loc["49–72"])
    no_security = rate("OnlineSecurity", "No")
    yes_security = rate("OnlineSecurity", "Yes")
    no_partner = rate("Partner", "No")
    yes_partner = rate("Partner", "Yes")
    senior_rate = rate("SeniorCitizen", 1)
    nonsenior_rate = rate("SeniorCitizen", 0)
    monthly_medians = cleaned.groupby("Churn")["MonthlyCharges"].median()
    total_medians = cleaned.groupby("Churn")["TotalCharges"].median()
    insights = [
        f"1. **Contract commitment is strongly associated with retention:** "
        f"month-to-month customers churn at {percent(month_to_month)}, versus "
        f"{percent(two_year)} for two-year customers.",
        f"2. **The first year is a high-risk period:** customers with 0–12 months "
        f"tenure churn at {percent(early_rate)}, compared with {percent(long_rate)} "
        "for customers with 49–72 months tenure.",
        f"3. **Electronic-check customers are a priority segment:** their churn rate "
        f"is {percent(electronic_check)}, the highest among payment methods; test "
        "payment-friction reduction rather than assuming payment type itself causes churn.",
        f"4. **Security-service adoption tracks with lower churn:** customers without "
        f"OnlineSecurity churn at {percent(no_security)}, compared with "
        f"{percent(yes_security)} among subscribers.",
        f"5. **Customer relationships mark different retention profiles:** customers "
        f"without a partner churn at {percent(no_partner)}, compared with "
        f"{percent(yes_partner)} for customers with a partner.",
        f"6. **Churned customers have higher monthly charges but lower accumulated "
        f"charges:** median MonthlyCharges are ${monthly_medians['Yes']:.2f} vs "
        f"${monthly_medians['No']:.2f}; median TotalCharges are "
        f"${total_medians['Yes']:.2f} vs ${total_medians['No']:.2f}. The shorter "
        "tenure of churned customers contributes to lower accumulated charges.",
        f"7. **Senior customers show elevated churn:** {percent(senior_rate)} versus "
        f"{percent(nonsenior_rate)} for non-senior customers; consider segment-specific "
        "support and validate the pattern with appropriate statistical/model analysis.",
    ]
    report_lines.extend(f"- {insight}" for insight in insights)
    report_lines.extend(
        [
            "",
            "## Training-readiness notes",
            "",
            f"- Cleaned file: `{CLEANED_PATH.name}` ({len(cleaned):,} rows, "
            f"{len(model_view.columns)} columns). `customerID` is included for "
            "identification but should be dropped before fitting.",
            "- `Churn` remains the human-readable target (`Yes`/`No`); `ChurnFlag` "
            "is not included in the exported CSV, preventing accidental target "
            "duplication/leakage.",
            "- All source rows are retained (including 0-tenure customers and valid "
            "service categories). Outlier flags are documented, not filtered.",
            "- This is cleaned tabular data, not a completed model matrix: encode "
            "categorical predictors and choose a validation strategy in the next "
            "feature-engineering/modeling phase. Fit any scalers/encoders on training "
            "data only.",
            "",
        ]
    )
    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Saved cleaned dataset: {CLEANED_PATH}")
    print(f"Saved EDA report: {REPORT_PATH}")
    print(f"Saved visualizations: {PLOT_DIR}")
    print(
        f"Final rows={len(cleaned):,}; churn={percent(churn_percentages['Yes'])}; "
        f"missing={int(cleaned.isnull().sum().sum())}; "
        f"duplicate IDs={int(cleaned['customerID'].duplicated().sum())}"
    )


if __name__ == "__main__":
    main()
