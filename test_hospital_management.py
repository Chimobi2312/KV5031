from HospitalManagement import Patient, DayPatient

# Creating a new patient
patient = Patient("John Doe", 65, 5501, "Hypertension", "2025-10-18")
print(patient.get_details())
print(patient.get_treatment_plan())

print("\n")

# Creating a new day patient
day_patient = DayPatient("Jane Smith", 45, 7892, "Migraine", "2025-10-19", "5:00 PM")
print(day_patient.get_details())
print(day_patient.get_treatment_plan())

