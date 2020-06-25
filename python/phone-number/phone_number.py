from string import digits

class PhoneNumber:
    def __init__(self, usr_num):
        self.number = PhoneNumber.clean(usr_num)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.sub_number = self.number[6:]

    def pretty(self):
        return f"({self.area_code}) {self.exchange_code}-{self.sub_number}"

    @staticmethod
    def clean(unclean_num):
        out = ""
        for char in unclean_num:
            if char in digits:
                out = out + char
        if len(out) not in (10, 11):
            raise ValueError("Invalid Number!")
        else:
            if len(out) == 11:
                if int(out[0])==1:
                    out = out[1:]
                else:
                    raise ValueError("Invalid Number!")

            if int(out[0])<2 or int(out[3])<2:
                raise ValueError("Invalid Number!")
            else:
                return out
