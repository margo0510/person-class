class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.contact_number = ""

    def change_details(self):
        print("Please enter your name:")
        self.name = input()
        print("Please enter your age:")
        age_input = input()
        age = int(age_input)
        print("Please enter your contact number:")
        self.contact_number = input()

    def show_details(self):
        print("The details of the person are:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Contact Number:", self.contact_number)



p1 = Person()
p1.change_details()
p1.show_details()


p2 = Person()
p2.change_details()
p2.show_details()