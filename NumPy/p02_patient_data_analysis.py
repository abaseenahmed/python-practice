#===================================== Hospital Patient Data Analysis ============================#
import numpy as np
import sys

#------------------------------------- DATA INITIALIZATION ---------------------------------#
def initialize_data():
    """Initialize all patient data and return variables"""
    global total_patients, patient_ids, age, temprature, temprature_round
    global blood_pressure, heart_rate, oxygen_level, weight, weight_round
    global hospital_table
    
    total_patients = 1000
    patient_ids = np.array(range(5001, 6001))
    age = np.random.randint(1, 101, total_patients)
    temprature = np.random.uniform(35.0, 41.5, total_patients)
    temprature_round = np.round(temprature, 1)
    blood_pressure = np.round(np.random.uniform(90, 180, total_patients), 2)
    heart_rate = np.round(np.random.uniform(45, 180, total_patients), 2)
    oxygen_level = np.round(np.random.uniform(70, 100, total_patients), 2)
    weight = np.random.uniform(30, 120, total_patients)
    weight_round = np.round(weight, 1)
    
    hospital_table = np.column_stack((patient_ids, age, temprature_round, blood_pressure, 
                                      heart_rate, oxygen_level, weight_round))
    
    print(f"\n✅ Data Initialized: {total_patients} patients loaded")
    print(f"   Shape: {hospital_table.shape}")
    print(f"   Memory: {hospital_table.nbytes/1024:.2f} KB")
    return True

#------------------------------------- MODULE 02: BASIC STATISTICS ---------------------------------#
def calculate_basic_stats():
    """Calculate and display basic statistics"""
    global average_age, average_temperature, average_blood_pressure, average_heart_rate
    global average_oxygen_level, average_weight, oldest_patient, youngest_patient
    global highest_temperature, lowest_temperature, highest_blood_pressure, lowest_blood_pressure
    global highest_heart_rate, lowest_heart_rate, highest_weight, lowest_weight
    
    print("\n" + "="*70)
    print("MODULE 02: BASIC STATISTICS")
    print("="*70)
    
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
    
    print(f"\n--- Averages ---")
    print(f"Average Age: {average_age:.1f} years")
    print(f"Average Temperature: {average_temperature:.1f}°C")
    print(f"Average Blood Pressure: {average_blood_pressure:.1f} mmHg")
    print(f"Average Heart Rate: {average_heart_rate:.1f} bpm")
    print(f"Average Oxygen Level: {average_oxygen_level:.1f}%")
    print(f"Average Weight: {average_weight:.1f} kg")
    
    print(f"\n--- Extreme Values ---")
    print(f"Oldest Patient: ID {patient_ids[oldest_patient]} (Age: {age[oldest_patient]} years)")
    print(f"Youngest Patient: ID {patient_ids[youngest_patient]} (Age: {age[youngest_patient]} years)")
    print(f"Highest Temperature: ID {patient_ids[highest_temperature]} ({temprature_round[highest_temperature]:.1f}°C)")
    print(f"Lowest Temperature: ID {patient_ids[lowest_temperature]} ({temprature_round[lowest_temperature]:.1f}°C)")
    print(f"Highest Blood Pressure: ID {patient_ids[highest_blood_pressure]} ({blood_pressure[highest_blood_pressure]:.1f} mmHg)")
    print(f"Lowest Blood Pressure: ID {patient_ids[lowest_blood_pressure]} ({blood_pressure[lowest_blood_pressure]:.1f} mmHg)")
    print(f"Highest Heart Rate: ID {patient_ids[highest_heart_rate]} ({heart_rate[highest_heart_rate]:.1f} bpm)")
    print(f"Lowest Heart Rate: ID {patient_ids[lowest_heart_rate]} ({heart_rate[lowest_heart_rate]:.1f} bpm)")
    print(f"Highest Weight: ID {patient_ids[highest_weight]} ({weight[highest_weight]:.1f} kg)")
    print(f"Lowest Weight: ID {patient_ids[lowest_weight]} ({weight[lowest_weight]:.1f} kg)")
    
    input("\nPress Enter to continue...")

#------------------------------------- MODULE 03: PATIENT FILTERING ---------------------------------#
def run_module_03():
    """Run patient filtering and categorization"""
    global elderly_count, child_count, patient_warm_count, cold_patients_count
    global patient_highBP_count, patients_highHR_count, patients_lowOX_count
    global patients_heavyWT_count, count_old_hot, ox_hr_patients
    
    print("\n" + "="*70)
    print("MODULE 03: PATIENT FILTERING & CATEGORIZATION")
    print("="*70)
    
    # ELDERLY PATIENTS
    elderly_patients = hospital_table[hospital_table[:, 1] > 60]
    elderly_patients_ids = elderly_patients[:, 0].astype(int)
    elderly_count = len(elderly_patients)
    elderly_percentage = (elderly_count/total_patients)*100
    
    print(f"\n--- Elderly Patients (Age > 60) ---")
    print(f"Count: {elderly_count} ({elderly_percentage:.1f}%)")
    print(f"First 10 IDs: {elderly_patients_ids[:10].tolist()}")
    
    # CHILD PATIENTS
    child_patients = hospital_table[hospital_table[:, 1] < 12]
    child_patients_ids = child_patients[:, 0].astype(int)
    child_count = len(child_patients)
    
    print(f"\n--- Child Patients (Age < 12) ---")
    print(f"Count: {child_count} ({child_count/total_patients*100:.1f}%)")
    print(f"First 10 IDs: {child_patients_ids[:10].tolist()}")
    
    # WARM PATIENTS
    patient_warm = hospital_table[hospital_table[:, 2] > 38]
    patient_warm_ids = patient_warm[:, 0].astype(int)
    patient_warm_count = len(patient_warm)
    
    print(f"\n--- Fever Patients (Temp > 38°C) ---")
    print(f"Count: {patient_warm_count} ({patient_warm_count/total_patients*100:.1f}%)")
    print(f"Top 10 IDs: {patient_warm_ids[:10].tolist()}")
    
    # COLD PATIENTS
    cold_patients = hospital_table[hospital_table[:, 2] < 36]
    cold_patients_ids = cold_patients[:, 0].astype(int)
    cold_patients_count = len(cold_patients)
    
    print(f"\n--- Cold Patients (Temp < 36°C) ---")
    print(f"Count: {cold_patients_count} ({cold_patients_count/total_patients*100:.1f}%)")
    print(f"First 10 IDs: {cold_patients_ids[:10].tolist()}")
    
    # HIGH BLOOD PRESSURE
    patient_highBP = hospital_table[hospital_table[:, 3] > 140]
    patient_highBP_count = len(patient_highBP)
    
    print(f"\n--- High Blood Pressure (> 140 mmHg) ---")
    print(f"Count: {patient_highBP_count} ({patient_highBP_count/total_patients*100:.1f}%)")
    
    # HIGH HEART RATE
    patients_highHR = hospital_table[hospital_table[:, 4] > 100]
    patients_highHR_count = len(patients_highHR)
    
    print(f"\n--- High Heart Rate (> 100 bpm) ---")
    print(f"Count: {patients_highHR_count} ({patients_highHR_count/total_patients*100:.1f}%)")
    
    # LOW OXYGEN
    patients_lowOX = hospital_table[hospital_table[:, 5] < 90]
    patients_lowOX_count = len(patients_lowOX)
    
    print(f"\n--- Low Oxygen (< 90%) ---")
    print(f"Count: {patients_lowOX_count} ({patients_lowOX_count/total_patients*100:.1f}%)")
    
    # HEAVY WEIGHT
    patients_heavyWT = hospital_table[hospital_table[:, 6] > 100]
    patients_heavyWT_count = len(patients_heavyWT)
    
    print(f"\n--- Heavy Weight (> 100 kg) ---")
    print(f"Count: {patients_heavyWT_count} ({patients_heavyWT_count/total_patients*100:.1f}%)")
    
    # OLD & HOT
    old_hot_patients = hospital_table[(hospital_table[:, 1] > 60) & (hospital_table[:, 2] > 38)]
    count_old_hot = len(old_hot_patients)
    
    print(f"\n--- Old & Hot (Age > 60 AND Temp > 38) ---")
    print(f"Count: {count_old_hot} ({count_old_hot/total_patients*100:.1f}%)")
    
    # CRITICAL PATIENTS
    ox_hr_patients = hospital_table[(hospital_table[:, 5] < 90) & (hospital_table[:, 4] > 100)]
    
    print(f"\n--- Critical Patients (O2 < 90 AND HR > 100) ---")
    print(f"Count: {len(ox_hr_patients)} ({len(ox_hr_patients)/total_patients*100:.1f}%)")
    
    input("\nPress Enter to continue...")

#------------------------------------- MODULE 04: STATISTICAL ANALYSIS ---------------------------------#
def run_module_04():
    """Run statistical analysis including mean, median, std, percentiles"""
    print("\n" + "="*70)
    print("MODULE 04: STATISTICAL ANALYSIS")
    print("="*70)
    
    features = {
        'Age': age,
        'Temperature': temprature_round,
        'Blood Pressure': blood_pressure,
        'Heart Rate': heart_rate,
        'Oxygen Level': oxygen_level,
        'Weight': weight_round
    }
    
    print("\n--- Statistical Summary ---")
    print("\nFeature         | Mean   | Median | Std Dev | Variance")
    print("-" * 60)
    
    for name, data in features.items():
        mean_val = np.mean(data)
        median_val = np.median(data)
        std_val = np.std(data)
        var_val = np.var(data)
        print(f"{name:15} | {mean_val:6.1f} | {median_val:6.1f} | {std_val:7.2f} | {var_val:8.2f}")
    
    print("\n--- Percentile Summary ---")
    print("\nFeature         | 5th   | 25th  | 50th  | 75th  | 90th  | 95th")
    print("-" * 70)
    
    for name, data in features.items():
        p5 = np.percentile(data, 5)
        p25 = np.percentile(data, 25)
        p50 = np.percentile(data, 50)
        p75 = np.percentile(data, 75)
        p90 = np.percentile(data, 90)
        p95 = np.percentile(data, 95)
        print(f"{name:15} | {p5:5.1f} | {p25:5.1f} | {p50:5.1f} | {p75:5.1f} | {p90:5.1f} | {p95:5.1f}")
    
    print("\n--- Most Variable Feature ---")
    std_values = [np.std(data) for data in features.values()]
    most_variable_idx = np.argmax(std_values)
    most_variable_name = list(features.keys())[most_variable_idx]
    print(f"Most Variable: {most_variable_name} (Std Dev: {std_values[most_variable_idx]:.2f})")
    
    input("\nPress Enter to continue...")

#------------------------------------- MODULE 05: PATIENT RANKING & SORTING ---------------------------------#
def run_module_05():
    """Run patient ranking and sorting with severity score"""
    global severity_score_rounded, sorted_by_severity, hospital_table_with_severity
    
    print("\n" + "="*70)
    print("MODULE 05: PATIENT RANKING & SORTING")
    print("="*70)
    
    # Sort by Age
    print("\n--- Youngest 10 Patients ---")
    sorted_by_age = hospital_table[np.argsort(hospital_table[:, 1])]
    youngest_10 = sorted_by_age[:10]
    print("ID\tAge\tTemp\tHR\tO2")
    for patient in youngest_10[:5]:  # Show first 5 for brevity
        print(f"{int(patient[0])}\t{int(patient[1])}\t{patient[2]:.1f}\t{patient[4]:.1f}\t{patient[5]:.1f}")
    print(f"... and {len(youngest_10)-5} more patients")
    
    print("\n--- Oldest 10 Patients ---")
    oldest_10 = sorted_by_age[-10:]
    print("ID\tAge\tTemp\tHR\tO2")
    for patient in oldest_10[:5]:
        print(f"{int(patient[0])}\t{int(patient[1])}\t{patient[2]:.1f}\t{patient[4]:.1f}\t{patient[5]:.1f}")
    print(f"... and {len(oldest_10)-5} more patients")
    
    # Sort by Temperature
    print("\n--- Temperature Extremes ---")
    sorted_by_temp = hospital_table[np.argsort(hospital_table[:, 2])]
    print(f"Hottest Patient: ID {int(sorted_by_temp[-1, 0])} ({sorted_by_temp[-1, 2]:.1f}°C), Age: {int(sorted_by_temp[-1, 1])}")
    print(f"Coldest Patient: ID {int(sorted_by_temp[0, 0])} ({sorted_by_temp[0, 2]:.1f}°C), Age: {int(sorted_by_temp[0, 1])}")
    
    # Sort by Oxygen
    print("\n--- Lowest 15 Oxygen Patients (Most Critical) ---")
    sorted_by_oxygen = hospital_table[np.argsort(hospital_table[:, 5])]
    lowest_15_oxygen = sorted_by_oxygen[:15]
    print("ID\tO2%\tAge")
    for patient in lowest_15_oxygen[:5]:
        print(f"{int(patient[0])}\t{patient[5]:.1f}\t{int(patient[1])}")
    print(f"... and {len(lowest_15_oxygen)-5} more patients")
    print(f"Oxygen Range: {lowest_15_oxygen[0, 5]:.1f}% - {lowest_15_oxygen[-1, 5]:.1f}%")
    
    # Sort by Heart Rate
    print("\n--- Top 10 Highest Heart Rate ---")
    sorted_by_hr = hospital_table[np.argsort(hospital_table[:, 4])]
    top_10_hr = sorted_by_hr[-10:]
    print("ID\tHR\tAge")
    for patient in top_10_hr[:5]:
        print(f"{int(patient[0])}\t{patient[4]:.1f}\t{int(patient[1])}")
    print(f"... and {len(top_10_hr)-5} more patients")
    print(f"HR Range: {top_10_hr[0, 4]:.1f} - {top_10_hr[-1, 4]:.1f} bpm")
    
    # Sort by Weight
    print("\n--- Top 5 Heaviest Patients ---")
    sorted_by_weight = hospital_table[np.argsort(hospital_table[:, 6])]
    top_5_weight = sorted_by_weight[-5:]
    print("ID\tWeight\tAge")
    for patient in top_5_weight:
        print(f"{int(patient[0])}\t{patient[6]:.1f}kg\t{int(patient[1])}")
    
    # SEVERITY SCORE
    print("\n--- Severity Score Calculation ---")
    temp_weight = 2.0
    hr_weight = 1.0
    oxygen_weight = 3.0
    
    temp_component = np.maximum((temprature_round - 36) * temp_weight, 0)
    hr_component = np.maximum((heart_rate - 60) * hr_weight, 0)
    oxygen_component = np.maximum((100 - oxygen_level) * oxygen_weight, 0)
    
    severity_score = temp_component + hr_component + oxygen_component
    severity_score_rounded = np.round(severity_score, 1)
    
    hospital_table_with_severity = np.column_stack((hospital_table, severity_score_rounded))
    sorted_by_severity = hospital_table_with_severity[np.argsort(severity_score_rounded)[::-1]]
    
    print(f"Severity Score Range: {np.min(severity_score_rounded):.1f} - {np.max(severity_score_rounded):.1f}")
    print(f"Average Severity Score: {np.mean(severity_score_rounded):.1f}")
    
    print("\n--- Top 10 Most Critical Patients ---")
    print("Rank\tID\tAge\tTemp\tHR\tO2\tScore")
    for rank, patient in enumerate(sorted_by_severity[:10], 1):
        print(f"{rank}\t{int(patient[0])}\t{int(patient[1])}\t{patient[2]:.1f}\t{patient[4]:.1f}\t{patient[5]:.1f}\t{patient[7]:.1f}")
    
    input("\nPress Enter to continue...")

#------------------------------------- MODULE 06: HOSPITAL EXECUTIVE REPORT ---------------------------------#
def run_module_06():
    """Generate comprehensive hospital executive report"""
    print("\n" + "="*70)
    print("                    HOSPITAL EXECUTIVE REPORT")
    print("                    Patient Data Analysis Summary")
    print("="*70)
    
    # PART 1: Hospital Overview
    print("\n" + "="*70)
    print("PART 1: HOSPITAL OVERVIEW")
    print("="*70)
    print(f"\nTotal Patients: {total_patients}")
    print(f"Total Features: {hospital_table.shape[1]}")
    print(f"Memory Usage: {hospital_table.nbytes/1024:.2f} KB")
    print(f"\nAverage Age: {average_age:.1f} years")
    print(f"Average Temperature: {average_temperature:.1f}°C")
    print(f"Average Blood Pressure: {average_blood_pressure:.1f} mmHg")
    print(f"Average Heart Rate: {average_heart_rate:.1f} bpm")
    print(f"Average Oxygen Level: {average_oxygen_level:.1f}%")
    print(f"Average Weight: {average_weight:.1f} kg")
    
    # PART 2: Patient Distribution
    print("\n" + "="*70)
    print("PART 2: PATIENT DISTRIBUTION")
    print("="*70)
    
    categories = [
        ("Elderly (Age > 60)", elderly_count),
        ("Children (Age < 12)", child_count),
        ("Fever (Temp > 38°C)", patient_warm_count),
        ("Cold (Temp < 36°C)", cold_patients_count),
        ("High BP (> 140)", patient_highBP_count),
        ("High HR (> 100)", patients_highHR_count),
        ("Low O2 (< 90%)", patients_lowOX_count),
        ("Heavy Weight (> 100kg)", patients_heavyWT_count)
    ]
    
    print("\nCategory                    | Count | Percentage")
    print("-" * 55)
    for category, count in categories:
        pct = (count/total_patients)*100
        print(f"{category:26} | {count:5} | {pct:6.1f}%")
    
    # PART 3: Critical Conditions
    print("\n" + "="*70)
    print("PART 3: CRITICAL CONDITIONS")
    print("="*70)
    print(f"\nOld + Fever Patients: {count_old_hot}")
    print(f"High HR + Low O2 Patients: {len(ox_hr_patients)}")
    print(f"Highest Severity Score: {np.max(severity_score_rounded):.1f}")
    print(f"Average Severity Score: {np.mean(severity_score_rounded):.1f}")
    
    # PART 4: Risk Analysis
    print("\n" + "="*70)
    print("PART 4: RISK ANALYSIS")
    print("="*70)
    
    critical_patients = np.sum(severity_score_rounded > 100)
    high_risk = np.sum((severity_score_rounded >= 70) & (severity_score_rounded <= 100))
    moderate_risk = np.sum((severity_score_rounded >= 40) & (severity_score_rounded < 70))
    stable = np.sum((severity_score_rounded >= 20) & (severity_score_rounded < 40))
    low_risk = np.sum(severity_score_rounded < 20)
    
    print(f"\nCritical (Score > 100): {critical_patients} ({critical_patients/total_patients*100:.1f}%)")
    print(f"High Risk (70-100): {high_risk} ({high_risk/total_patients*100:.1f}%)")
    print(f"Moderate Risk (40-69): {moderate_risk} ({moderate_risk/total_patients*100:.1f}%)")
    print(f"Stable (20-39): {stable} ({stable/total_patients*100:.1f}%)")
    print(f"Low Risk (< 20): {low_risk} ({low_risk/total_patients*100:.1f}%)")
    
    # PART 5: Hospital Health Index
    print("\n" + "="*70)
    print("PART 5: HOSPITAL HEALTH INDEX")
    print("="*70)
    
    health_score = 100
    health_score -= (patient_warm_count / total_patients) * 20
    health_score -= (critical_patients / total_patients) * 30
    health_score -= (patients_lowOX_count / total_patients) * 25
    health_score -= (patient_highBP_count / total_patients) * 15
    health_score -= (patients_highHR_count / total_patients) * 10
    health_score = max(0, min(100, health_score))
    
    if health_score >= 90:
        status = "EXCELLENT 🌟"
    elif health_score >= 75:
        status = "GOOD ✅"
    elif health_score >= 60:
        status = "FAIR ⚠️"
    elif health_score >= 40:
        status = "POOR ❌"
    else:
        status = "CRITICAL 🔴"
    
    print(f"\nHospital Health Score: {health_score:.1f}/100")
    print(f"Status: {status}")
    
    # PART 6: Alerts and Recommendations
    print("\n" + "="*70)
    print("PART 6: ALERTS & RECOMMENDATIONS")
    print("="*70)
    
    alerts = []
    if patient_warm_count/total_patients*100 > 20:
        alerts.append("⚠️ High fever cases detected (>20%)")
    if patients_lowOX_count/total_patients*100 > 15:
        alerts.append("⚠️ Critical oxygen shortage (>15%)")
    if elderly_count/total_patients*100 > 35:
        alerts.append("⚠️ Large elderly population (>35%)")
    if average_heart_rate > 100:
        alerts.append("⚠️ Average heart rate exceeds 100 bpm")
    if patients_highBP_count/total_patients*100 > 30:
        alerts.append("⚠️ High hypertension rate (>30%)")
    
    if alerts:
        print("\nAlerts Detected:")
        for alert in alerts:
            print(f"  {alert}")
    else:
        print("\n✅ No critical alerts detected. Hospital condition appears stable.")
    
    print("\nRecommendations:")
    if health_score >= 75:
        print("  1. Continue regular monitoring")
        print("  2. Maintain current protocols")
    elif health_score >= 60:
        print("  1. Increase monitoring of at-risk patients")
        print("  2. Review treatment protocols")
    else:
        print("  1. IMMEDIATE: Increase ICU capacity")
        print("  2. URGENT: Address oxygen supply")
        print("  3. PRIORITY: Enhance emergency response")
    
    # PART 7: Final Analysis
    print("\n" + "="*70)
    print("PART 7: FINAL ANALYSIS")
    print("="*70)
    
    # Most common issue
    issues = {
        "Fever": patient_warm_count,
        "High BP": patient_highBP_count,
        "High HR": patients_highHR_count,
        "Low O2": patients_lowOX_count,
        "Elderly": elderly_count
    }
    most_common = max(issues, key=issues.get)
    
    print(f"\nMost Common Health Issue: {most_common} ({issues[most_common]} patients)")
    print(f"Highest Risk Patient: ID {int(sorted_by_severity[0, 0])} (Score: {sorted_by_severity[0, 7]:.1f})")
    
    print(f"\nOverall Hospital Status: {status}")
    print(f"Health Score: {health_score:.1f}/100")
    
    print("\n" + "="*70)
    print("                    END OF HOSPITAL EXECUTIVE REPORT")
    print("="*70)
    
    input("\nPress Enter to continue...")

#------------------------------------- MAIN MENU SYSTEM ---------------------------------#
def display_menu():
    """Display the main menu"""
    print("\n" + "="*70)
    print("           HOSPITAL PATIENT DATA ANALYSIS SYSTEM")
    print("="*70)
    print("\n" + "="*70)
    print("MAIN MENU")
    print("="*70)
    print("\n1. Initialize/Randomize Data")
    print("2. Module 02: Basic Statistics")
    print("3. Module 03: Patient Filtering & Categorization")
    print("4. Module 04: Statistical Analysis")
    print("5. Module 05: Patient Ranking & Sorting")
    print("6. Module 06: Hospital Executive Report")
    print("7. Run All Modules (Complete Analysis)")
    print("8. Exit")
    print("-" * 70)

#------------------------------------- MAIN PROGRAM ---------------------------------#
def main():
    """Main program loop"""
    data_initialized = False
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '1':
            data_initialized = initialize_data()
        
        elif choice == '2':
            if not data_initialized:
                print("\n⚠️ Please initialize data first (Option 1)")
            else:
                calculate_basic_stats()
        
        elif choice == '3':
            if not data_initialized:
                print("\n⚠️ Please initialize data first (Option 1)")
            else:
                run_module_03()
        
        elif choice == '4':
            if not data_initialized:
                print("\n⚠️ Please initialize data first (Option 1)")
            else:
                run_module_04()
        
        elif choice == '5':
            if not data_initialized:
                print("\n⚠️ Please initialize data first (Option 1)")
            else:
                run_module_05()
        
        elif choice == '6':
            if not data_initialized:
                print("\n⚠️ Please initialize data first (Option 1)")
            else:
                run_module_06()
        
        elif choice == '7':
            if not data_initialized:
                data_initialized = initialize_data()
            if data_initialized:
                print("\n" + "="*70)
                print("RUNNING COMPLETE ANALYSIS")
                print("="*70)
                calculate_basic_stats()
                run_module_03()
                run_module_04()
                run_module_05()
                run_module_06()
                print("\n✅ Complete analysis finished!")
        
        elif choice == '8':
            print("\n" + "="*70)
            print("Thank you for using the Hospital Patient Data Analysis System")
            print("="*70)
            sys.exit()
        
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()