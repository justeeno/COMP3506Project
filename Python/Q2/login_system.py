
from login_system_base import LoginSystemBase


class LoginSystem (LoginSystemBase):

    def __init__(self):
        super().__init__()
        self.login_list = [None for i in range(101)]
        
    """
        Implement the described functions here !
    """

    def __len__(self):
        return len(self.login_list)

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
        
        if self.get_num_of_users == len(self.login_list):
            extra_space = [None for i in range(len(self.login_list))]
            self.login_list = self.login_list + (extra_space * 2)

        if self.login_list[comp_func] != None:
            for i in range(comp_func, len(self.login_list)):
                if self.login_list[i] == None:
                    self.login_list[i] = [email, password]
                    return True
                elif self.login_list[i] != None:
                    continue
                elif self.login_list[i][0] == email:
                    return False
        else:
            self.login_list[comp_func] = [email, password]
            return True
        
    def remove_user(self, email, password):
        password_correct = self.check_password(email, password)

        if password_correct in (-1, -2):
            return False
        else:
            self.login_list[password_correct] = None
            return True

    def check_password(self, email, password) -> int:
        val = self.hash_codes(email)
        comp_func = val % len(self.login_list)

        for i in range(comp_func, len(self.login_list)):
            if self.login_list[i] == None:
                continue
            elif self.login_list[i][0] == email:
                if self.login_list[i][1] == password:
                    return i
                else:
                    return -2
            else:
                continue
        return -1
        

    def change_password(self, email, old_password, new_password) -> bool:
        password_correct = self.check_password(email, old_password)

        if password_correct in (-1, -2):
            return False
        else:
            self.login_list[password_correct] = [email, new_password]
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
