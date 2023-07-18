import time
from random import randint
import os
from functools import wraps
#... your definition of log decorator...
def log(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        f = open("machin.log", "a")
        f.write(f'{func.__name__} Took [{total_time:.4f} seconds]\n')
        f.close()
        #print(f' {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper
class CoffeeMachine():
    water_level = 100
        
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    f = open("machin.log", "w")
    f.close()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
    
    