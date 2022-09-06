
from hospital_base import HospitalBase
from patient import Patient


class Hospital_1 (HospitalBase):

    def __init__(self):
        super().__init__()
        patient_list = []
        patient_time_list = []
        ordered_list = []

    def __iter__(self):
        """
            Add your code here!
        """
        return self

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        
        patient_time = patient.time
        if int(patient_time[3]) % 2 != 0 or int(patient_time[4] != 0):
            return False
        elif patient_time in self.patient_time_list:
            return False
        else:
            self.patient_list.append(patient)
            self.patient_time_list.append(patient_time)
            return True

    # ==============================  Add any extra functions below   ==============================

    def str_to_int(self, patient: Patient):
        string = patient.time
        time_int = string.replace(':','')
        return time_int

if __name__ == "__main__":
    """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            The following main function is provided for simple debugging only
        """
    hospital = Hospital_1()
    hospital.add_patient(Patient("Max", "11:00"))
    hospital.add_patient(Patient("Alex", "13:20"))
    hospital.add_patient(Patient("George", "14:00"))
    list_of_patients = [Patient("Max", "11:00"), Patient("Alex", "13:20"), Patient("George", "14:00")]
    for i, el in enumerate(hospital):
        assert el == list_of_patients[i]
