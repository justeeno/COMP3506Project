
import time
from hospital_base import HospitalBase
from patient import Patient


class Hospital_1 (HospitalBase):

    def __init__(self):
        super().__init__()
        self.patient_list = []
        self.patient_list_time = []

    def __iter__(self):
        """
            Add your code here!
        """
        return self
        # min_time = 0
        # first_patient = None
        # for patient in self.patient_list:
        #     time = self.str_to_int(patient.time)
        #     if time < min_time:
        #         first_patient = patient

        # for patient in self.patient_list:
        #     self.str_to_int(patient)
        # self.quicksort(self.patient_list)

    def add_patient(self, patient: Patient):
        """
            Add your code here!
        """

        patient_time = self.str_to_int(patient)
        patient_time_str = patient.time
        patient_element = [patient_time, patient]
        if patient_time < 800 or patient_time >= 1800:
            return False
        elif patient_time >= 1200 and patient_time < 1300:
            return False
        if int(patient_time_str[3]) % 2 != 0 or int(patient_time_str[4]) != 0:
            return False
        elif patient_time in self.patient_list_time:
            return False
        else:
            self.append(self.patient_list, patient_element)
            self.append(self.patient_list_time, patient_time)
        return True

        # if int(patient_time[3]) % 2 != 0 or int(patient_time[4]) != 0:
        #     return False
        # elif patient_time in self.patient_list_time:
        #     return False
        # else:
        #     self.append(self.patient_list, patient)
        #     self.append(self.patient_list_time, patient_time)
            # if len(self.patient_list) == 0:
            #     self.append(self.patient_list, patient)
            # else:
            #     self.patient_list.insert_to_tail(patient)
            # return True
        # if len(self.patient_list) != 0:
        #     self.patient_list.insert_to_list(patient)
        # else:
        #     pass
            


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
        patients[len(patients):] = [element]

    def remove(self, og_list, element):
        new_list = []
        for i in range(len(og_list)):
            if og_list[i] != element:
                self.append(new_list, og_list[i])
        return new_list  

    # def quicksort(self, arr):
    #     if len(arr) <=1:
    #         return arr
        
    #     pivot = arr[len(arr) // 2]
    #     less, eq, greater = [], [], []
    #     for i in arr:
    #         if i < pivot: 
    #             self.append(less.time, i)
    #         elif i > pivot:
    #             self.append(greater.time, i)
    #         else:
    #             self.append(eq.time, i)
    #     return self.quicksort(less) + eq + self.quicksort(greater)

# class Node:
#     def __init__(self, data):
#         self.item = data
#         self.head = None
#         self.tail = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.start_node = None

#     def insert_to_list(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#         else:
#             print("The list is empty")

#     def insert_to_tail(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#             return
#         n = self.start_node
#         while n.head is not None:
#             n = n.head
#         new_node = Node(data)
#         n.head = new_node
#         new_node.tail = n

#     def insert_to_head(self, data):
#         if self.start_node is None:
#             new_node = Node(data)
#             self.start_node = new_node
#             return
#         n = self.start_node
#         while n.tail is not None:
#             n = n.tail
#         new_node = Node(data)
#         n.tail = new_node
#         new_node.head = n

if __name__ == "__main__":
    """
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            The following main function is provided for simple debugging only
        """
    ll = Hospital_1()
    ll.add_patient(Patient("George", "14:00"))
    ll.add_patient(Patient("Alex", "13:15"))
    ll.add_patient(Patient("Max", "11:00"))
    ll.add_patient(Patient("Justin", "12:00"))
    ll.add_patient(Patient("Alice", "10:00"))
    ll.add_patient(Patient("Emily", "10:00"))
    ll.add_patient(Patient("John", "18:05"))
    ll.add_patient(Patient("Sid", "08:43"))
    
    list_of_patients = [Patient("Alice", "10:00"), Patient("Max", "11:00"), Patient("George", "14:00")]
    for i, el in enumerate(ll):
        assert el == list_of_patients[i]
