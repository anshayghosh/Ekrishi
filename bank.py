class bank:
    bank_balance = 0

    def __init__(self,val):
        self.bank_balance = val

    def add(self,val):
        self.bank_balance = self.bank_balance + val

    def subtract(self,val):        
        self.bank_balance = self.bank_balance - val

    def check_broke(self):
        if(self.bank_balance<=0):
            return True
        else:
            return False
