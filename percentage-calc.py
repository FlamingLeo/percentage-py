print("Available Calculations: ")
print("A: X is what " + "%" + " of Y?")
print("B: What is X" + "%" + " of Y?")
print("C: Y is how much " + "%" + " more/less than X?")
print()

while True:
    option = input("Option: ")
    if option.upper() == 'A':
        break
    elif option.upper() == 'B':
        break
    elif option.upper() == 'C':
        break
    else:
        print("Invalid Option.")

print()

while True:
    try:
        x = float(input("X: "))
        y = float(input("Y: "))
        break
    except ValueError:
        print("Invalid Value.")

print()
if option.upper() == 'A':
    z = x/y*100
    print(str(z) + "%")
elif option.upper() == 'B':
    z = x/100*y
    print(str(z))
elif option.upper() == 'C':
    z = (y-x)/x*100
    print(str(z) + "%")

input("Press Enter to close program. \n")
