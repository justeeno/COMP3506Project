
from login_system_base import LoginSystemBase


class LoginSystem (LoginSystemBase):

    def __init__(self):
        super().__init__()
        self.login_list = []
        for i in range(101):
            self.login_list[i] = None


    """
        Implement the described functions here !
    """

    def __len__(self):
        count = 0
        for i in range(len(self.login_list)):
            count += 1
        return count

    def get_num_of_users(self):
        count = 0
        for k in range(len(self.login_list)):
            if self.login_list[k] != None:
                count += 1
        return count

    def hash_codes(self, key: str):
        c = 31
        str_val = []
        res = 0
        for a in key:
            a_val = ord(a)
            str_val[len(str_val):] = [a_val] 
        
        for val in range(len(str_val)):
            if val < len(str_val) - 1:
                res = (res + str_val[val]) * c
                continue
            else:
                break
        return res + str_val[-1]

    def add_user(self, email, password):
        val = self.hash_codes(email)
        comp_func = val % len(self.login_list)
        user = (email, password)
        

    def remove_user(self, email, password):
        pass

    def check_password(self, email, password) -> int:
        for i in range(len(self.login_list)):
            if self.login_list[i][0] == email:
                if self.login_list[i][1] == password:
                    return i
                else:
                    return -2
            else:
                return -1

    def change_password(self, email, old_password, new_password) -> bool:
        return True


if __name__ == "__main__":
    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        The following main function is provided for simple debugging only
    """

    login = LoginSystem()

    assert login.hash_codes("GQHTMP") == login.hash_codes("H2HTN1")
    assert len(login) == 101
    assert login.check_password("a@b.c", "L6ZS9") == -1
    login.add_user("a@b.c", "L6ZS9")
    assert login.check_password("a@b.c", "ZZZZZZ") == -2
    assert login.check_password("a@b.c", "L6ZS9") == 94
    login.remove_user("a@b.c", "L6ZS9")
    assert login.check_password("a@b.c", "L6ZS9") == -1
