# Dictionary of countries and their capitals

countrydb = {}

while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capital")
    print("5. Delete")

    choice = int(input("Enter your choice : "))


    if choice == 1:
        country = input("Enter Country: ").lower()
        capital = input("Enter Capital: ").lower()
        countrydb[country] = capital

    elif choice == 2:
        print(countrydb.keys())


    elif choice == 3:
        print(countrydb.values())

    elif choice == 4:
        country = input("Enter Country: ").lower()
        print(countrydb[country])

    elif choice == 5:
        country = input ("Enter Country: ").lower()
        del countrydb[country]

    else:
        break

