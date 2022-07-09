favorite_numbers={
    'Jiang yi':['1','32','34'],
    'Xiao shunzi':['88','89','33'],
    'Tian Lin':['7','23'],
    'Mei Yanan':['32','3','12'],
    'Guang rong':['90','8','45'],
    }
for names, numbers in favorite_numbers.items():
    print(f"\n{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(f'\t{number}')