print("===============================================================================")
print((" Donahue's Supermarket ").center(50,"="))
print("===============================================================================")


price=int( input("Enter price for item: "))

while (True):
    price=int(input(""))
    subtotal=(price)
    if (price==-1):
         break
    else:
         print("price $", price)

print("===============================================================================")


print("===============================================================================")


print("Subtotal $", subtotal)

tax=int(subtotal * 0.065)
print("Tax $", tax)

total=int(subtotal + tax)
print("Total $", total)


print("=============================================================================")
print (" Do come again ")
print("=============================================================================")

print(" Thank you for your business!")


