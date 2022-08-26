
from alert_system_base import AlertSystemBase, User


class AlertSystem(AlertSystemBase):

    def __init__(self):
        super().__init__()

    """
        Implement the described functions here !
    """


if __name__ == "__main__":
    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        The following main function is provided for simple debugging only
    """

    alert = AlertSystem()
    u1, u2 = User("Alex"), User("Max")
    u3, u4 = User("Nick"), User("Bing")
    users = [u1, u2, u3, u4]
    for u in users:
        alert.add_person(u)
    alert.add_contact(u1, u2)
    alert.add_contact(u1, u3)
    alert.add_contact(u2, u4)
    assert alert.count_contacts(u1) == 2
    alert.mark_infected(u1, virus_degree=1)
    assert u1.infected
    assert u2.infected
    assert not u4.infected
