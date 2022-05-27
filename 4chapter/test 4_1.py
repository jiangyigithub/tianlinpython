pizzas=['pepperoni','orange','apple']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I realy love pizza!")

my_pizzas=['pepperoni','orange','apple']
friend_pizzas=my_pizzas[:]
my_pizzas.append('banana')
friend_pizzas.append('carrot')

print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print("My friends favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
