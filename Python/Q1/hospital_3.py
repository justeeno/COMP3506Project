
from hospital_base import HospitalBase
from patient import Patient


class Hospital_3 (HospitalBase):

    def __init__(self):
        super().__init__()

    def __iter__(self):
        """
            Add your code here!
        """

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """
        return True

    # ==============================  Add any extra functions below   ==============================

    def str_to_int(self, patient: Patient):
        string = patient.time
        time_int = string.replace(':','')
        return time_int
    
    def append(self, patients, element):
        patients[len(patients):] = [element]
    
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

# if __name__ == "__main__":
#     """
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
#             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#             The following main function is provided for simple debugging only
#         """
#     ll = Hospital_3()
#     ll.add_patient(Patient("Max", "11:00"))
#     ll.add_patient(Patient("Alex", "13:15"))
#     ll.add_patient(Patient("George", "14:00"))
#     list_of_patients = [Patient("Max", "11:00"), Patient("Alex", "13:15"), Patient("George", "14:00")]
#     for i, el in enumerate(ll):
#         assert el == list_of_patients[i]

