items = [
    {'name': 'Soap', 'price': 25.50, 'quantity': 2},
    {'name': 'Shampoo', 'price': 120.00, 'quantity': 1},
    {'name': 'Toothpaste', 'price': 40.00, 'quantity': 3}
]
total_cost = 0
print("Itemized Bill:")
print("Item\t\tPrice\tQuantity\tTotal")
for item in items:
    item_total = item['price'] * item['quantity']
    total_cost += item_total
    print(f"{item['name']}\t\t{item['price']}\t{item['quantity']}\t\t{item_total}")
print("\nTotal Bill Amount:", total_cost)
