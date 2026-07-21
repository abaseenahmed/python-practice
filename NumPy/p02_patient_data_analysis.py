#===================================== Hospital Patient Data Analysis ============================#
import numpy as np

#------------------------------------- Module 01 For HPDA System ---------------------------------#

total_patients = 1000
patient_ids = np.array(range(5001, 6001))  # 1000 patients
age = np.random.randint(1, 101, total_patients)  # Random ages between 1-100
temprature = np.random.uniform(35.0, 41.5, total_patients)
temprature_round = np.round(temprature, 1)
blood_pressure = np.round(np.random.uniform(90, 180, total_patients), 2)
heart_rate = np.round(np.random.uniform(45, 180, total_patients), 2)
oxygen_level = np.round(np.random.uniform(70, 100, total_patients), 2)
weight = np.random.uniform(30, 120, total_patients)
weight_round = np.round(weight, 1)

hospital_table = np.column_stack((patient_ids, age, temprature_round, blood_pressure, heart_rate, oxygen_level, weight_round))

for i in range(10):
    print(hospital_table[i])
print(f'Total Patients : {total_patients}')
print(f'Shape : {np.shape(hospital_table)}')  # Output: (1000, 7)
print(f'Number of Rows : {hospital_table.shape[0]}')
print(f'Number of Columns : {hospital_table.shape[1]}')
print(f'Memory Used by Table : {hospital_table.nbytes/1024:.2f} KB')

#------------------------------------- Module 02 For HPDA System ---------------------------------#

average_age = np.mean(age)
average_temperature = np.mean(temprature_round)
average_blood_pressure = np.mean(blood_pressure)
average_heart_rate = np.mean(heart_rate)
average_oxygen_level = np.mean(oxygen_level)
average_weight = np.mean(weight_round)
oldest_patient = np.argmax(age)
youngest_patient = np.argmin(age)
highest_temperature = np.argmax(temprature_round)
lowest_temperature = np.argmin(temprature_round)
highest_blood_pressure = np.argmax(blood_pressure)
lowest_blood_pressure = np.argmin(blood_pressure)
highest_heart_rate = np.argmax(heart_rate)
lowest_heart_rate = np.argmin(heart_rate)
highest_weight = np.argmax(weight)
lowest_weight = np.argmin(weight)

print(f'The Oldest Patient ID : {patient_ids[oldest_patient]} and Age : {age[oldest_patient]}')
print(f'The Youngest Patient ID : {patient_ids[youngest_patient]} and Age : {age[youngest_patient]}')
print(f'Highest Temperature ID : {patient_ids[highest_temperature]}, Temperature : {temprature_round[highest_temperature]} °C')
print(f'Lowest Temperature ID : {patient_ids[lowest_temperature]}, Temperature : {temprature_round[lowest_temperature]} °C')
print(f'Highest Blood Pressure ID : {patient_ids[highest_blood_pressure]}, Blood Pressure : {blood_pressure[highest_blood_pressure]}')
print(f'Lowest Blood Pressure ID : {patient_ids[lowest_blood_pressure]}, Blood Pressure : {blood_pressure[lowest_blood_pressure]}')
print(f'Highest Heart Rate ID : {patient_ids[highest_heart_rate]}, Heart Rate : {heart_rate[highest_heart_rate]}')
print(f'Lowest Heart Rate ID : {patient_ids[lowest_heart_rate]}, Heart Rate : {heart_rate[lowest_heart_rate]}')
print(f'Highest Weight ID : {patient_ids[highest_weight]}, Weight : {weight[highest_weight]}')
print(f'Lowestest Weight ID : {patient_ids[lowest_weight]}, Weight : {weight[lowest_weight]}')

#-------------------------------------------------- Module 03 HPDA System ------------------------------------
# ============ ELDERLY PATIENTS (Age > 60) ============
elderly_patients = hospital_table[hospital_table[:, 1] > 60]
elderly_patients_ids = elderly_patients[:, 0].astype(int)
elderly_count = len(elderly_patients)
elderly_percentage = (elderly_count/total_patients)*100
print(f'The Total Number of Elder Patients : {elderly_count}')
print(f'The Percentage of Elderly Patients : {elderly_percentage:.2f}%')
print(f'First 10 Elderly Patients IDs : ')
# FIXED: Added check to avoid IndexError if less than 10 patients
for i in range(min(10, len(elderly_patients_ids))):
    print(f'  {i+1}. {elderly_patients_ids[i]}')

# ============ CHILD PATIENTS (Age < 12) ============
child_patients = hospital_table[hospital_table[:, 1] < 12]
child_patients_ids = child_patients[:, 0].astype(int)
child_count = len(child_patients)
print(f'\nThe Total Number of Child Patients in the Hospital Are : {child_count}')
print(f'The First 10 Child IDs Are : ')
# FIXED: Added check to avoid IndexError
for i in range(min(10, len(child_patients_ids))):
    print(f'  {i+1}. {child_patients_ids[i]}')

# ============ WARM PATIENTS (Temperature > 38) ============
patient_warm = hospital_table[hospital_table[:, 2] > 38]
patient_warm_ids = patient_warm[:, 0].astype(int)
patient_warm_count = len(patient_warm)
# FIXED: Get the patient with hottest temperature from the filtered array
if len(patient_warm) > 0:
    hottest_index = np.argmax(patient_warm[:, 2])  # Find index of max temperature in filtered array
    patient_hotest = patient_warm[hottest_index, 0].astype(int)  # Get ID of hottest patient
    hottest_temp = patient_warm[hottest_index, 2]  # Get the actual temperature
else:
    patient_hotest = "No patients found"
    hottest_temp = "N/A"

print(f'\nThe Total Number of Patient With Temperature > 38 Are : {patient_warm_count}')
print(f'The Top Ten Patients IDs are : ')
# FIXED: Added check to avoid IndexError
for i in range(min(10, len(patient_warm_ids))):
    print(f'  {i+1}. {patient_warm_ids[i]}')
print(f'The Patient with Hottest Temperature : {patient_hotest} (Temperature: {hottest_temp}°C)')

# ============ COLD PATIENTS (Temperature < 36) ============
cold_patients = hospital_table[hospital_table[:, 2] < 36]
cold_patients_ids = cold_patients[:, 0].astype(int)
cold_patients_count = len(cold_patients)
print(f'\nThe Number of Patients With Temperature < 36°C Are : {cold_patients_count}')
print(f'The First 10 Patients with cold temperature are : ')
# FIXED: Added check to avoid IndexError
for i in range(min(10, len(cold_patients_ids))):
    print(f'  {i+1}. {cold_patients_ids[i]}')

# ============ HIGH BLOOD PRESSURE (BP > 140) ============
patient_highBP = hospital_table[hospital_table[:, 3] > 140]
patient_highBP_count = len(patient_highBP)
# FIXED: Calculate average of blood pressure column (index 3), not the whole array
if len(patient_highBP) > 0:
    average_highBP = np.mean(patient_highBP[:, 3])  # Only average BP values
else:
    average_highBP = 0
print(f'\nThe Number of High Blood Pressure Patients are : {patient_highBP_count}')
print(f'The Average Blood Pressure of High BP Patients is : {average_highBP:.1f} mmHg')

# ============ HIGH HEART RATE (HR > 100) ============
patients_highHR = hospital_table[hospital_table[:, 4] > 100]
patients_highHR_count = len(patients_highHR)
# FIXED: Get max heart rate from the filtered array
if len(patients_highHR) > 0:
    highest_hr_index = np.argmax(patients_highHR[:, 4])
    patient_highestHR = patients_highHR[highest_hr_index, 0].astype(int)
    highest_hr_value = patients_highHR[highest_hr_index, 4]
else:
    patient_highestHR = "No patients found"
    highest_hr_value = "N/A"
print(f'\nThe Number of patients with Heart Rate > 100 are : {patients_highHR_count}')
print(f'Patient With Highest Heart Rate: ID {patient_highestHR} ({highest_hr_value} bpm)')

# ============ LOW OXYGEN (O2 < 90) ============
patients_lowOX = hospital_table[hospital_table[:, 5] < 90]
patients_lowOX_count = len(patients_lowOX)
# FIXED: Get min oxygen from the filtered array
if len(patients_lowOX) > 0:
    lowest_ox_index = np.argmin(patients_lowOX[:, 5])
    patient_lowestOX = patients_lowOX[lowest_ox_index, 0].astype(int)
    lowest_ox_value = patients_lowOX[lowest_ox_index, 5]
else:
    patient_lowestOX = "No patients found"
    lowest_ox_value = "N/A"
print(f'\nThe Number of patients with Oxygen Level < 90 are : {patients_lowOX_count}')
print(f'Patient With Lowest Oxygen Level: ID {patient_lowestOX} ({lowest_ox_value}%)')

# ============ HEAVY WEIGHT (Weight > 100) ============
patients_heavyWT = hospital_table[hospital_table[:, 6] > 100]
patients_heavyWT_count = len(patients_heavyWT)
# FIXED: Calculate average of weight column (index 6)
if len(patients_heavyWT) > 0:
    patients_average_heavyWT = np.mean(patients_heavyWT[:, 6])
else:
    patients_average_heavyWT = 0
print(f'\nThe Number of patients with Weight > 100 are  : {patients_heavyWT_count}')
print(f'The Average Weight of Heavy Weight People are : {patients_average_heavyWT:.1f} kg')

# ============ OLD & HOT PATIENTS (Age > 60 AND Temp > 38) ============
# FIXED: Corrected the condition - was using > 38 for both age and temp
old_hot_patients = hospital_table[(hospital_table[:, 1] > 60) & (hospital_table[:, 2] > 38)]
count_old_hot = len(old_hot_patients)
old_hot_ids = old_hot_patients[:, 0].astype(int) if len(old_hot_patients) > 0 else np.array([])
print(f'\nThe Number of Patients with Age > 60 & Temperature > 38 are: {count_old_hot}')
if count_old_hot > 0:
    print(f'The IDs of the first 10 Patients are:')
    for i in range(min(10, len(old_hot_ids))):
        print(f'  {i+1}. {old_hot_ids[i]}')
else:
    print('No patients found matching this criteria')

# ============ CRITICAL PATIENTS (O2 < 90 AND HR > 100) ============
# FIXED: Corrected the condition and variable names
ox_hr_patients = hospital_table[(hospital_table[:, 5] < 90) & (hospital_table[:, 4] > 100)]
ox_hr_patients_ids = ox_hr_patients[:, 0].astype(int) if len(ox_hr_patients) > 0 else np.array([])
print(f'\nThe Number of Critical Patients are : {len(ox_hr_patients)}')
if len(ox_hr_patients) > 0:
    print('The IDs of first 10 critical patients are:')
    for i in range(min(10, len(ox_hr_patients_ids))):
        print(f'  {i+1}. {ox_hr_patients_ids[i]}')
else:
    print('No critical patients found')

#--------------------------------------------- Module 04 HPDA System ------------------------------------------#
# ============ SINGLE FUNCTION FOR ALL STATISTICS ============
def calculate_statistics(data_array, feature_name):
    """
    This function calculates and prints all statistics for a given feature.
    """
    print(f"\n========== {feature_name} STATISTICS ==========")
    print(f"Mean (Average): {np.mean(data_array):.2f}")
    print(f"Median: {np.median(data_array):.2f}")
    print(f"Variance: {np.var(data_array):.2f}")
    print(f"Standard Deviation: {np.std(data_array):.2f}")
    print(f"Minimum: {np.min(data_array):.2f}")
    print(f"Maximum: {np.max(data_array):.2f}")
    print(f"Range: {np.max(data_array) - np.min(data_array):.2f}")

# Store all features for analysis
features = {
    'Age': age,
    'Temperature': temprature_round,
    'Blood Pressure': blood_pressure,
    'Heart Rate': heart_rate,
    'Oxygen Level': oxygen_level,
    'Weight': weight_round
}

# Calculate statistics for each feature
for name, data in features.items():
    calculate_statistics(data, name)

# ============ PERCENTILE CALCULATION ============
def calculate_percentiles(data_array, feature_name):
    """
    This function calculates and prints percentiles for a given feature.
    """
    print(f"\n----- {feature_name} Percentiles -----")
    print(f"5th Percentile: {np.percentile(data_array, 5):.2f}")
    print(f"10th Percentile: {np.percentile(data_array, 10):.2f}")
    print(f"25th Percentile: {np.percentile(data_array, 25):.2f}")
    print(f"50th Percentile (Median): {np.percentile(data_array, 50):.2f}")
    print(f"75th Percentile: {np.percentile(data_array, 75):.2f}")
    print(f"90th Percentile: {np.percentile(data_array, 90):.2f}")
    print(f"95th Percentile: {np.percentile(data_array, 95):.2f}")

print("\n" + "="*50)
print("PERCENTILE ANALYSIS")
print("="*50)

for name, data in features.items():
    calculate_percentiles(data, name)

# ============ FIND MOST VARIABLE FEATURE ============
print("\n" + "="*50)
print("MOST VARIABLE FEATURE ANALYSIS")
print("="*50)

# Calculate standard deviation for each feature
std_values = []
feature_names = []

for name, data in features.items():
    std_values.append(np.std(data))
    feature_names.append(name)

# Find which feature has highest standard deviation
most_variable_index = np.argmax(std_values)
most_variable_name = feature_names[most_variable_index]
most_variable_std = std_values[most_variable_index]

print(f"\nThe Most Variable Feature is: {most_variable_name}")
print(f"With Standard Deviation: {most_variable_std:.2f}")

# ============ OUTLIER DETECTION USING PERCENTILES ============
print("\n" + "="*50)
print("OUTLIER DETECTION USING PERCENTILES")
print("="*50)

def detect_outliers_percentile(data_array, patient_ids_array, feature_name, percentile_value, direction='above'):
    """
    Detect outliers based on percentiles.
    
    Parameters:
    data_array: The data to analyze
    patient_ids_array: Array of patient IDs
    feature_name: Name of the feature
    percentile_value: The percentile threshold (e.g., 95, 10)
    direction: 'above' for values above percentile, 'below' for values below percentile
    
    Returns:
    Dictionary with outlier information
    """
    # Calculate the percentile threshold
    threshold = np.percentile(data_array, percentile_value)
    
    # Find outliers based on direction
    if direction == 'above':
        outlier_mask = data_array > threshold
        direction_text = "above"
    else:  # direction == 'below'
        outlier_mask = data_array < threshold
        direction_text = "below"
    
    # Get the outlier data
    outlier_data = data_array[outlier_mask]
    outlier_ids = patient_ids_array[outlier_mask]
    
    # Calculate statistics
    count = len(outlier_data)
    percentage = (count / len(data_array)) * 100
    
    # Print results
    print(f"\n--- {feature_name} ---")
    print(f"Patients with {feature_name} {direction_text} the {percentile_value}th percentile ({threshold:.2f})")
    print(f"Count: {count} patients ({percentage:.1f}% of total)")
    
    if count > 0:
        print(f"First 10 Patient IDs:")
        for i in range(min(10, len(outlier_ids))):
            print(f"  {i+1}. Patient ID: {int(outlier_ids[i])}")
        
        # Additional statistics about outliers
        print(f"Range of {feature_name} for outliers: {np.min(outlier_data):.2f} - {np.max(outlier_data):.2f}")
        print(f"Average {feature_name} for outliers: {np.mean(outlier_data):.2f}")
    else:
        print("No patients found in this category")
    
    return {
        'count': count,
        'percentage': percentage,
        'ids': outlier_ids,
        'data': outlier_data,
        'threshold': threshold
    }

# ============ APPLY OUTLIER DETECTION ============

# 1. Patients whose age is above the 95th percentile
elderly_outliers = detect_outliers_percentile(
    age, patient_ids, "Age", 95, 'above'
)

# 2. Patients whose weight is below the 5th percentile
underweight_outliers = detect_outliers_percentile(
    weight_round, patient_ids, "Weight", 5, 'below'
)

# 3. Patients whose heart rate is above the 90th percentile
high_hr_outliers = detect_outliers_percentile(
    heart_rate, patient_ids, "Heart Rate", 90, 'above'
)

# 4. Patients whose oxygen level is below the 10th percentile
low_oxygen_outliers = detect_outliers_percentile(
    oxygen_level, patient_ids, "Oxygen Level", 10, 'below'
)

# 5. Patients whose temperature is above the 95th percentile (extra example)
high_temp_outliers = detect_outliers_percentile(
    temprature_round, patient_ids, "Temperature", 95, 'above'
)

# 6. Patients whose blood pressure is below the 5th percentile (extra example)
low_bp_outliers = detect_outliers_percentile(
    blood_pressure, patient_ids, "Blood Pressure", 5, 'below'
)

# 7. Patients whose blood pressure is above the 95th percentile (extra example)
high_bp_outliers = detect_outliers_percentile(
    blood_pressure, patient_ids, "Blood Pressure", 95, 'above'
)

# ============ COMPLEX OUTLIER CONDITIONS ============
print("\n" + "="*50)
print("COMPLEX OUTLIER CONDITIONS (Combining Multiple Features)")
print("="*50)

# 1. Elderly with high heart rate (Age > 95th percentile AND Heart Rate > 90th percentile)
age_95th = np.percentile(age, 95)
hr_90th = np.percentile(heart_rate, 90)

complex_outliers_1 = hospital_table[(hospital_table[:, 1] > age_95th) & (hospital_table[:, 4] > hr_90th)]
count_1 = len(complex_outliers_1)

print(f"\n--- Elderly Patients with High Heart Rate ---")
print(f"Patients with Age > {age_95th:.2f} (95th percentile) AND Heart Rate > {hr_90th:.2f} (90th percentile)")
print(f"Count: {count_1} patients")
if count_1 > 0:
    print(f"First 10 Patient IDs:")
    for i in range(min(10, count_1)):
        print(f"  {i+1}. Patient ID: {int(complex_outliers_1[i, 0])}")

# 2. Underweight with low oxygen (Weight < 5th percentile AND Oxygen < 10th percentile)
weight_5th = np.percentile(weight_round, 5)
oxygen_10th = np.percentile(oxygen_level, 10)

complex_outliers_2 = hospital_table[(hospital_table[:, 6] < weight_5th) & (hospital_table[:, 5] < oxygen_10th)]
count_2 = len(complex_outliers_2)

print(f"\n--- Underweight Patients with Low Oxygen ---")
print(f"Patients with Weight < {weight_5th:.2f} (5th percentile) AND Oxygen < {oxygen_10th:.2f} (10th percentile)")
print(f"Count: {count_2} patients")
if count_2 > 0:
    print(f"First 10 Patient IDs:")
    for i in range(min(10, count_2)):
        print(f"  {i+1}. Patient ID: {int(complex_outliers_2[i, 0])}")

# 3. High temperature with high heart rate (Temperature > 95th percentile AND Heart Rate > 90th percentile)
temp_95th = np.percentile(temprature_round, 95)

complex_outliers_3 = hospital_table[(hospital_table[:, 2] > temp_95th) & (hospital_table[:, 4] > hr_90th)]
count_3 = len(complex_outliers_3)

print(f"\n--- High Temperature with High Heart Rate ---")
print(f"Patients with Temperature > {temp_95th:.2f} (95th percentile) AND Heart Rate > {hr_90th:.2f} (90th percentile)")
print(f"Count: {count_3} patients")
if count_3 > 0:
    print(f"First 10 Patient IDs:")
    for i in range(min(10, count_3)):
        print(f"  {i+1}. Patient ID: {int(complex_outliers_3[i, 0])}")

# ============ SUMMARY OF ALL OUTLIERS ============
print("\n" + "="*50)
print("SUMMARY OF OUTLIER DETECTION")
print("="*50)

outlier_summary = [
    ("Age > 95th percentile", elderly_outliers['count']),
    ("Weight < 5th percentile", underweight_outliers['count']),
    ("Heart Rate > 90th percentile", high_hr_outliers['count']),
    ("Oxygen Level < 10th percentile", low_oxygen_outliers['count']),
    ("Temperature > 95th percentile", high_temp_outliers['count']),
    ("Blood Pressure < 5th percentile", low_bp_outliers['count']),
    ("Blood Pressure > 95th percentile", high_bp_outliers['count'])
]

print("\nOutlier Category | Count")
print("-" * 40)
for category, count in outlier_summary:
    print(f"{category:25} | {count:5}")

print("\nTotal patients in hospital:", total_patients)
print("Note: Patients can appear in multiple outlier categories")