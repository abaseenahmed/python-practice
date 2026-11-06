# House Price EDA and Data Preparation

This project profiles `raw_data.csv`, applies documented data-quality rules, and
exports a cleaned dataset for subsequent house-price modeling. The raw source is
never overwritten.

## Run

From this directory:

```powershell
python .\eda_house_prices.py
```

Or pass alternate locations:

```powershell
python .\eda_house_prices.py --input .\raw_data.csv --output-dir .
```

Dependencies are listed in `requirements.txt`.

## Workflow

The script uses NumPy, pandas, Matplotlib, and Seaborn to:

1. Standardize column names and trim text values.
2. Audit data types, missing values, numeric distributions, category cardinality,
   IQR outlier fences, duplicates, and domain-specific anomalies.
3. Remove exact duplicates and rows with missing or non-positive sale prices.
4. Convert zero bedroom/bathroom values to missing, and represent sale timing,
   house age, and renovation status with explicit features.
5. Exclude the near-unique street address and constant country fields from the
   model table while retaining city and ZIP code.
6. Save a diagnostic dashboard, audit tables, a text report, and cleaned CSV.

Missing feature values are intentionally retained. Fit imputation, scaling, and
categorical encoders on training data only (ideally in a scikit-learn pipeline)
to prevent data leakage. IQR outliers are reported, not automatically removed:
extreme but valid homes should be reviewed against source context before any
exclusion or transformation.

## Output files

- `data/cleaned_house_prices.csv`
- `reports/eda_report.txt`
- `reports/missing_values.csv`
- `reports/numeric_summary.csv`
- `reports/categorical_summary.csv`
- `reports/iqr_outliers.csv`
- `visualizations/house_price_eda_dashboard.png`

The cleaned table keeps `price` as the prediction target and `city`/`statezip`
as categorical columns. It is suitable for the next preprocessing/modeling step,
but categorical encoding and feature imputation still belong inside the model
training pipeline.
