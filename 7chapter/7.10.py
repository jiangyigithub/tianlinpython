resort='If you could visit one place in the world,where would you go?'
resort+="\n(Enter 'quit' when you are finished .)"
while True:
    city=input(resort)

    if city=='quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


