class GotCharacter:
    def __init__(self,first_name,is_alive=True) :
        self.first_name=first_name
        self.is_alive=is_alive

class starck(GotCharacter):
    def __init__(self, first_name=None,is_alive=True):
        super().__init__(first_name=first_name,is_alive=is_alive)
        self.family_name="starck"
        self.house_world="Winter is coming"
    def print_house_world(self):
        print(self.house_world)
    
    def die(self):
        self.is_alive=False

aya=starck("aya")
print(aya.family_name)
print(aya.house_world)

