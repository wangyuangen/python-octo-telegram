from ModelBase import Base

class Customer(Base):
    def __init__(self):
        self.CustName = ''
        self.Sex = ''
        self.NickName = ''
        self.Address = ''
        self.Mobile = ''
        self.AccountInfoId = 0