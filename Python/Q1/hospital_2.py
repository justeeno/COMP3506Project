
from hospital_base import HospitalBase
from patient import Patient


class Hospital_2 (HospitalBase):

    def __init__(self):
        super().__init__()
        self.patient_list = []

    def __iter__(self):
        """
            Add your code here!
        """
        return self

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        patient_time = self.str_to_int(patient)
        patient_element = [patient_time, patient]
        if patient_time < 800 or patient_time >= 1800:
            return False
        elif patient_time >= 1200 and patient_time < 1300:
            return False
        else:
            self.patient_list = self.append(self.patient_list, patient_element)
            return True

    # ==============================  Add any extra functions below   ==============================

    def __next__(self):
        if len(self.patient_list) == 0:
            raise StopIteration
        first_patient = None
        for patient in range(len(self.patient_list)):
            if patient == 0:
                first_patient = self.patient_list[patient]
            elif self.patient_list[patient][0] < first_patient[0]:
                first_patient = self.patient_list[patient]
            elif self.patient_list[patient][0] == first_patient[0]:
                continue
            else:
                continue
        self.patient_list = self.remove(self.patient_list, first_patient)
        return first_patient[1]

    def str_to_int(self, patient: Patient):
        string = patient.time
        time_int = string.replace(':','')
        return int(time_int)
    
    def append(self, patients, element):
        grow_array = [None for i in range(len(patients) + 1)]
        if len(grow_array) == 0:
            patients = [element]
            return patients
        else:
            for i in range(len(patients)):
                grow_array[i] = patients[i]
            patients = []
            grow_array[-1] = element
            patients = grow_array
            return patients

    def remove(self, og_list, element):
        new_list = []
        for i in range(len(og_list)):
            if og_list[i] != element:
                new_list = self.append(new_list, og_list[i])
        return new_list