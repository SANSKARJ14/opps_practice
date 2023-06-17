
#multilevel inheritence example 
class bank:
    def tranaction(self):
        print ("this show tranactions")
    def account_opening(self):
        print("this show accounts")

class hdfc(bank):
    def hdfc_to_icici(self):
        print ("welcome to hdfc")


class icici_bank(hdfc):
    pass

i = icici_bank()
i.tranaction()
i.account_opening()
i.hdfc_to_icici()



