"""
CP1404 Practice
Practicing a simple menu-driven program
"""

menu = """(H)ello
(G)oodbye
(Q)uit"""

user_name = str(input("Enter name: "))
print(menu)
choice = str(input(">>> ")).upper()

while choice != "Q":
    if choice == "H":
        print("Hello", user_name)
    elif choice == "G":
        print("Goodbye", user_name)
    else:
        print("Invalid choice")
    print(menu)
    choice = str(input(">>>")).upper()
print("Finished")
