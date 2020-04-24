## import pickle
# Let we create a class
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        print(self.name, "\t", self.model, "\t", self.color)


def dump():
    with open("car.pkl", "wb") as f:
        l = []
        n = int(input("How many record to be entered"))
        for i in range(n):
            name = input("Name:")
            model = input("Model:")
            color = input("Color:")
            c = Car(name, model, color)
            l.append(c)
        pickle.dump(l, f)
        print("Record updated successfully")


def load():
    with open("car.pkl", 'rb') as f:
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    i.display()
            except EOFError:
                print("Data read is completed")
                break


def remove():
    obj = None
    with open("car.pkl", "rb") as f:
        h = input("Enter the name of the Car you want to remove: ")
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    print(i.name)
                    if i.name == h:
                        obj.remove(i)
            except EOFError:
                print("Data read is removed")
                break
    with open("car.pkl", "wb") as f:
        pickle.dump(obj, f)


def modify():
    obj = None
    with open("car.pkl", "rb") as f:
        h = input("Enter the name of the Car you want to modify: ")
        while (1):
            try:
                obj = pickle.load(f)
                for i in obj:
                    if i.name == h:
                        i.model = input("Enter the model to change")
            except EOFError:
                print("Data read is modified")
                break
    with open("car.pkl", "wb") as f:
        pickle.dump(obj, f)


ch = 9
while (ch != 0):
    print("\n1:Enter record\n2:View record\n3:Remove\n4:Modify\n0:Exit")
    ch = int(input())
    if ch == 1:
        dump()
    elif ch == 2:
        load()
    elif ch == 3:
        remove()
    elif ch == 4:
        modify()
