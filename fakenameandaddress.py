
from faker import Faker 

def name():
   fake = Faker(['en_UK'])
   return fake.name()
    
def address():
    fake = Faker(['en_UK'])
    return fake.address()
    


def construct():
    counter = 0
    file = open("NamesAddresses's.txt", "w")
    while counter <= 25:
        c = name() + "\n" + address() + "\n"
        counter += 1
        file.write(c + "\n")
    file.close()