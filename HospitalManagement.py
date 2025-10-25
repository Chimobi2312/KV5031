
class Patient:
    """A class to represent a patient."""

    def __init__(self, name: str, age: int, patient_id: int, illness: str, admission_date: str):
        """Initializes a new Patient object."""
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.illness = illness
        self.admission_date = admission_date

    def get_details(self) -> str:
        """Returns a string containing the patient's details."""
        return f"Patient Name: {self.name}, Age: {self.age}, ID: {self.patient_id}, Illness: {self.illness}, Admission Date: {self.admission_date}"

    def get_treatment_plan(self) -> str:
        """Returns a string representing a generic treatment plan."""
        return "The treatment plan for this patient will be provided after further assessment."


class DayPatient(Patient):
    """A class to represent a day patient."""

    def __init__(self, name: str, age: int, patient_id: int, illness: str, admission_date: str, discharge_time: str):
        """Initializes a new DayPatient object."""
        super().__init__(name, age, patient_id, illness, admission_date)
        self.discharge_time = discharge_time

    def get_details(self) -> str:
        """Returns a string containing the day patient's details."""
        return f"Day Patient Name: {self.name}, Age: {self.age}, ID: {self.patient_id}, Illness: {self.illness}, Admission Date: {self.admission_date}, Discharge Time: {self.discharge_time}"

    def get_treatment_plan(self) -> str:
        """Returns a string representing a treatment plan for a day patient."""
        return f"The treatment plan includes day procedures and the patient will be discharged by {self.discharge_time}."

