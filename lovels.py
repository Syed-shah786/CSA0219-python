loaves = int(input("Enter number of loaves of day old bread: "))
regular_price = loaves * 18
discount = regular_price * 0
total_price = regular_price - discount
print("Regular price: {:.2f} rupees".format(regular_price))
print("Discount: {:.2f} rupees".format(discount))
print("Total price: {:.2f} rupees".format(total_price))

