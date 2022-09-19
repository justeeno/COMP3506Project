
from hospital_base import HospitalBase
from patient import Patient


class Hospital_1 (HospitalBase):

    def __init__(self):
        super().__init__()
        self.patient_list = []
        self.patient_time_list = []

    def __iter__(self):
        """
            Add your code here!
        """
        # min_time = 0
        # first_patient = None
        # for patient in self.patient_list:
        #     time = self.str_to_int(patient.time)
        #     if time < min_time:
        #         first_patient = patient

        for patient in self.patient_list:
            self.str_to_int(patient)
        self.quicksort(self.patient_list)
        
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
            self.append(self.patient_list, patient)
            self.append(self.patient_time_list, patient_time)
            return True

    # ==============================  Add any extra functions below   ==============================

    def str_to_int(self, patient: Patient):
        string = patient.time
        time_int = string.replace(':','')
        time_int = int(time_int)
        patient.time = time_int
        return patient
    
    def append(self, arr_list, element):
        arr_list[len(arr_list):] = [element]    

    def quicksort(self, arr):
        if len(arr) <=1:
            return arr
        
        pivot = arr[len(arr) // 2]
        less, eq, greater = [], [], []
        for i in arr:
            if i < pivot: 
                self.append(less.time, i)
            elif i > pivot:
                self.append(greater.time, i)
            else:
                self.append(eq.time, i)
        return self.quicksort(less) + eq + self.quicksort(greater)

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
