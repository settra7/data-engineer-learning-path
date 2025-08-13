# Practice:
# Create a list of 5 numbers, loop through them and output their squares.

x = [12, 14, 16, 18, 20]
     
for i in x:
    print(pow(i, 2))

# Create a dictionary with 3 pairs of "product: price", loop through them and output in the format: "Product - Price".

y = {"apple": 1, "banana": 0.5, "orange": 0.75}

for product, price in y.items():
    print(f"{product} — {price} $.")