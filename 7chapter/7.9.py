sandwich_orders=['Peanut butter','pastrami','Fish meat','pastrami','French meat floss','pastrami']
finished_sandwiches=[]
print("The deli is out of 'pastrami'.")

while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
    print(f'I made you {sandwich_order}.')
    finished_sandwiches.append(sandwich_order)

print(finished_sandwiches)
print(sandwich_orders)
