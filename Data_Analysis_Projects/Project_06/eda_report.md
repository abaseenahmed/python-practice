# Telco Customer Churn: Data Preparation and EDA

Source: [Kaggle IBM Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).
The original source CSV is retained unchanged in `data/`; `customerID` is retained for identification and must be excluded from model features. No model-specific encoding or scaling has been applied.

## Initial inspection

- Shape: 7,043 rows × 21 columns.
- Exact duplicate rows: 0.
- Duplicate `customerID` values: 0.
- Whitespace-only changes made to categorical/text cells: 11.
- Blank `TotalCharges` strings: 11.

### `head()`

```text
customerID gender  SeniorCitizen Partner Dependents  tenure PhoneService    MultipleLines InternetService OnlineSecurity OnlineBackup DeviceProtection TechSupport StreamingTV StreamingMovies       Contract PaperlessBilling             PaymentMethod  MonthlyCharges TotalCharges Churn
7590-VHVEG Female              0     Yes         No       1           No No phone service             DSL             No          Yes               No          No          No              No Month-to-month              Yes          Electronic check           29.85        29.85    No
5575-GNVDE   Male              0      No         No      34          Yes               No             DSL            Yes           No              Yes          No          No              No       One year               No              Mailed check           56.95       1889.5    No
3668-QPYBK   Male              0      No         No       2          Yes               No             DSL            Yes          Yes               No          No          No              No Month-to-month              Yes              Mailed check           53.85       108.15   Yes
7795-CFOCW   Male              0      No         No      45           No No phone service             DSL            Yes           No              Yes         Yes          No              No       One year               No Bank transfer (automatic)           42.30      1840.75    No
9237-HQITU Female              0      No         No       2          Yes               No     Fiber optic             No           No               No          No          No              No Month-to-month              Yes          Electronic check           70.70       151.65   Yes
```

### `info()`

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7043 entries, 0 to 7042
Data columns (total 21 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   customerID        7043 non-null   object 
 1   gender            7043 non-null   object 
 2   SeniorCitizen     7043 non-null   int64  
 3   Partner           7043 non-null   object 
 4   Dependents        7043 non-null   object 
 5   tenure            7043 non-null   int64  
 6   PhoneService      7043 non-null   object 
 7   MultipleLines     7043 non-null   object 
 8   InternetService   7043 non-null   object 
 9   OnlineSecurity    7043 non-null   object 
 10  OnlineBackup      7043 non-null   object 
 11  DeviceProtection  7043 non-null   object 
 12  TechSupport       7043 non-null   object 
 13  StreamingTV       7043 non-null   object 
 14  StreamingMovies   7043 non-null   object 
 15  Contract          7043 non-null   object 
 16  PaperlessBilling  7043 non-null   object 
 17  PaymentMethod     7043 non-null   object 
 18  MonthlyCharges    7043 non-null   float64
 19  TotalCharges      7043 non-null   object 
 20  Churn             7043 non-null   object 
dtypes: float64(1), int64(2), object(18)
memory usage: 1.1+ MB
```

### `describe()`

```text
        customerID gender  SeniorCitizen Partner Dependents       tenure PhoneService MultipleLines InternetService OnlineSecurity OnlineBackup DeviceProtection TechSupport StreamingTV StreamingMovies        Contract PaperlessBilling     PaymentMethod  MonthlyCharges TotalCharges Churn
count         7043   7043    7043.000000    7043       7043  7043.000000         7043          7043            7043           7043         7043             7043        7043        7043            7043            7043             7043              7043     7043.000000         7043  7043
unique        7043      2            NaN       2          2          NaN            2             3               3              3            3                3           3           3               3               3                2                 4             NaN         6531     2
top     7590-VHVEG   Male            NaN      No         No          NaN          Yes            No     Fiber optic             No           No               No          No          No              No  Month-to-month              Yes  Electronic check             NaN                 No
freq             1   3555            NaN    3641       4933          NaN         6361          3390            3096           3498         3088             3095        3473        2810            2785            3875             4171              2365             NaN           11  5174
mean           NaN    NaN       0.162147     NaN        NaN    32.371149          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       64.761692          NaN   NaN
std            NaN    NaN       0.368612     NaN        NaN    24.559481          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       30.090047          NaN   NaN
min            NaN    NaN       0.000000     NaN        NaN     0.000000          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       18.250000          NaN   NaN
25%            NaN    NaN       0.000000     NaN        NaN     9.000000          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       35.500000          NaN   NaN
50%            NaN    NaN       0.000000     NaN        NaN    29.000000          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       70.350000          NaN   NaN
75%            NaN    NaN       0.000000     NaN        NaN    55.000000          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN       89.850000          NaN   NaN
max            NaN    NaN       1.000000     NaN        NaN    72.000000          NaN           NaN             NaN            NaN          NaN              NaN         NaN         NaN             NaN             NaN              NaN               NaN      118.750000          NaN   NaN
```

### Missing values, duplicates, and unique values

- `isnull().sum()`: {'customerID': 0, 'gender': 0, 'SeniorCitizen': 0, 'Partner': 0, 'Dependents': 0, 'tenure': 0, 'PhoneService': 0, 'MultipleLines': 0, 'InternetService': 0, 'OnlineSecurity': 0, 'OnlineBackup': 0, 'DeviceProtection': 0, 'TechSupport': 0, 'StreamingTV': 0, 'StreamingMovies': 0, 'Contract': 0, 'PaperlessBilling': 0, 'PaymentMethod': 0, 'MonthlyCharges': 0, 'TotalCharges': 0, 'Churn': 0}
- `duplicated().sum()`: 0
- `customerID.duplicated().sum()`: 0
- `nunique()`: {'customerID': 7043, 'gender': 2, 'SeniorCitizen': 2, 'Partner': 2, 'Dependents': 2, 'tenure': 73, 'PhoneService': 2, 'MultipleLines': 3, 'InternetService': 3, 'OnlineSecurity': 3, 'OnlineBackup': 3, 'DeviceProtection': 3, 'TechSupport': 3, 'StreamingTV': 3, 'StreamingMovies': 3, 'Contract': 3, 'PaperlessBilling': 2, 'PaymentMethod': 4, 'MonthlyCharges': 1585, 'TotalCharges': 6531, 'Churn': 2}

## Cleaning decisions and validation

- Removed 0 exact duplicate row(s); no duplicate customer IDs were found. Duplicate IDs would stop the script for explicit review rather than silently discarding a customer record.
- Stripped surrounding whitespace from text values (11 cells changed); all categorical values match the expected source categories.
- `TotalCharges` was parsed as numeric. Its 11 blank source strings all belong to customers with `tenure == 0`, consistent with newly opened accounts having no accumulated charges; those values are set to 0.0, and all 11 records are retained.
- `No internet service` and `No phone service` are valid states and remain unchanged; they are not treated as missing values.
- `customerID` remains in the cleaned file. Drop it from the eventual training feature matrix to avoid using an identifier as a predictor.
- Range checks passed: `SeniorCitizen` is binary, `tenure` is 0–72 months, and charge values are nonnegative.

### Numeric ranges and IQR outlier flags

Outlier flags below use the 1.5×IQR rule for review only. No valid records were deleted on the basis of an outlier flag.
- `tenure`: min=0, Q1=9, median=29, Q3=55, max=72; IQR review bounds [-60.00, 124.00], flagged=0.
- `MonthlyCharges`: min=18.25, Q1=35.5, median=70.35, Q3=89.85, max=118.75; IQR review bounds [-46.02, 171.38], flagged=0.
- `TotalCharges`: min=0, Q1=398.55, median=1394.55, Q3=3786.6, max=8684.8; IQR review bounds [-4683.52, 8868.67], flagged=0.

## EDA and visual observations

### Churn distribution (`01_churn_distribution.png`)
- 5,174 customers (73.5%) stayed and 1,869 (26.5%) churned. The class distribution is imbalanced, so later model evaluation should include precision/recall, ROC-AUC or PR-AUC, and a stratified split rather than accuracy alone.

### Demographics (`02_demographics.png`)

- **gender:** Female has the highest observed churn rate (26.9%); Male has the lowest (26.2%). These are descriptive associations, not evidence that the category causes churn.
- **SeniorCitizen:** Senior has the highest observed churn rate (41.7%); Not senior has the lowest (23.6%). These are descriptive associations, not evidence that the category causes churn.
- **Partner:** No has the highest observed churn rate (33.0%); Yes has the lowest (19.7%). These are descriptive associations, not evidence that the category causes churn.
- **Dependents:** No has the highest observed churn rate (31.3%); Yes has the lowest (15.5%). These are descriptive associations, not evidence that the category causes churn.

### Account distributions (`03_account_distributions.png`)

- **tenure:** The churned group has a lower median (10.00) than the retained group (38.00). The histogram and boxplot show the distribution and spread; the relationship is observational.
- **MonthlyCharges:** The churned group has a higher median (79.65) than the retained group (64.43). The histogram and boxplot show the distribution and spread; the relationship is observational.
- **TotalCharges:** The churned group has a lower median (703.55) than the retained group (1679.53). The histogram and boxplot show the distribution and spread; the relationship is observational.

### Contracts, payments, and billing (`04_contract_and_payment.png`)

- **Contract:** Month-to-month has the highest observed churn rate (42.7%); Two year has the lowest (2.8%). These are descriptive associations, not evidence that the category causes churn.
- **PaymentMethod:** Electronic check has the highest observed churn rate (45.3%); Credit card (automatic) has the lowest (15.2%). These are descriptive associations, not evidence that the category causes churn.
- **PaperlessBilling:** Yes has the highest observed churn rate (33.6%); No has the lowest (16.3%). These are descriptive associations, not evidence that the category causes churn.

### Services (`05_services.png`)

- **InternetService:** Fiber optic has the highest observed churn rate (41.9%); No has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **OnlineSecurity:** No has the highest observed churn rate (41.8%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **TechSupport:** No has the highest observed churn rate (41.6%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **OnlineBackup:** No has the highest observed churn rate (39.9%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **DeviceProtection:** No has the highest observed churn rate (39.1%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **StreamingTV:** No has the highest observed churn rate (33.5%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- **StreamingMovies:** No has the highest observed churn rate (33.7%); No internet service has the lowest (7.4%). These are descriptive associations, not evidence that the category causes churn.
- In `OnlineSecurity`, `TechSupport`, `OnlineBackup`, `DeviceProtection`, `StreamingTV`, and `StreamingMovies`, `No internet service` remains a valid separate category; its plotted rate is not a missing-value artifact.

### Correlation heatmap (`06_correlation_heatmap.png`)
- Among the displayed numeric variables, `tenure` has the strongest negative linear correlation with the binary churn indicator (r=-0.35); `MonthlyCharges` has the strongest positive correlation (r=0.19). This is a compact linear summary, not a causal result; categorical features are not included in this numeric-only heatmap.

## Business insights

- 1. **Contract commitment is strongly associated with retention:** month-to-month customers churn at 42.7%, versus 2.8% for two-year customers.
- 2. **The first year is a high-risk period:** customers with 0–12 months tenure churn at 47.4%, compared with 9.5% for customers with 49–72 months tenure.
- 3. **Electronic-check customers are a priority segment:** their churn rate is 45.3%, the highest among payment methods; test payment-friction reduction rather than assuming payment type itself causes churn.
- 4. **Security-service adoption tracks with lower churn:** customers without OnlineSecurity churn at 41.8%, compared with 14.6% among subscribers.
- 5. **Customer relationships mark different retention profiles:** customers without a partner churn at 33.0%, compared with 19.7% for customers with a partner.
- 6. **Churned customers have higher monthly charges but lower accumulated charges:** median MonthlyCharges are $79.65 vs $64.43; median TotalCharges are $703.55 vs $1679.53. The shorter tenure of churned customers contributes to lower accumulated charges.
- 7. **Senior customers show elevated churn:** 41.7% versus 23.6% for non-senior customers; consider segment-specific support and validate the pattern with appropriate statistical/model analysis.

## Training-readiness notes

- Cleaned file: `cleaned_data.csv` (7,043 rows, 21 columns). `customerID` is included for identification but should be dropped before fitting.
- `Churn` remains the human-readable target (`Yes`/`No`); `ChurnFlag` is not included in the exported CSV, preventing accidental target duplication/leakage.
- All source rows are retained (including 0-tenure customers and valid service categories). Outlier flags are documented, not filtered.
- This is cleaned tabular data, not a completed model matrix: encode categorical predictors and choose a validation strategy in the next feature-engineering/modeling phase. Fit any scalers/encoders on training data only.
