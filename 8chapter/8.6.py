def city_country(city,country):
    c_full_name=f"{city}, {country}"
    return c_full_name.title() 


while True:
    print("\nPlease tell me your full_name:")
    print("enter 'q' at any time to quit")

    a_city=input("city:")
    if a_city=='q':
       break

    b_country=input("country:")
    if  b_country=='q':
        break

    formatted_name=city_country(a_city,b_country)
    print(f"\n{formatted_name}")