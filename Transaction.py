class Transaction :

    def __init__(self, from_person, to_person, amount, id):
        self.from_person = from_person
        self.to_person = to_person
        self.amount = amount
        self.id = id
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return str({"From Person": self.from_person , "To Person": self.to_person, "Amount" : self.amount, "Id": self.id})
