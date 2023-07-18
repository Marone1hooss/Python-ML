class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
    def transfer(self, amount):
        self.value += amount
    
    
    def iscorrupted(self):
        attributes0=dir(self)
        attributes=[attr for attr in attribute_names if not attr.startswith('__')]
        if len(attributes)%2==0:
            return True
        zip=False
        addr=False
        name=False
        id=False
        value=False
        for i in attributes:
            if i.startswith("b"):
                return True
            if i.startswith("zip"):
                zip=True
            if i.startswith("addr"):
                addr=True
            if i=="name":
                if isinstance(self.name,str):
                    name=True
            if i=="id":
                if isinstance(self.id,int):
                    id=True
            if i=="value":
                if isinstance(self.value,int) or isinstance(self.value,float):
                    value=True
            
            
        if zip and value and addr and id and name :
            return False
        return True    
        


# in the_bank.py
class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []
    
    def add(self, new_account):

    # test if new_account is an Account() instance and if
    # it can be appended to the attribute accounts
    # ... Your code ...
        if isinstance(new_account,Account):
            if not new_account.iscorrupted and new_account not in self.accounts :
                self.accounts.append(new_account)
                return True
        return False
    def transfer(self, origin, dest, amount):
        if origin not in self.accounts or dest not in self.accounts:
            return False
        if origin.value >= amount and amount > 0:
            dest.transfer(amount)
            origin.value-=amount
            return True
        return False
        
        # ... Your code ...
    def fix_account(self, name):
        ...
