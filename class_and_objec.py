class shopping_cart():
    name = ""
    age = 20
    region = "Germany"
    item = "iphone_15"
    section = "smartphone"

    #constructor method 
    def __init__(self):
        print("creating a shopping itenery: ")

    def change_item(self):
        print("Please Enter your item: ")
        self.item = input()
        print("Please Enter Name Of User: ")
        self.name = input()

    # funtion to show details 
    def show_details(self):
        print("The Details Of Items Are: ")
        print(self.name)
        print(self.age)
        print(self.region)
        print(self.item)
        print(self.section)


Jonthon = shopping_cart()        
Jonthon.change_item()
Jonthon.show_details()


