cities={
    'London':{'country':'British','population':'67.9 billion',
    'fact':'London is the political, economic, cultural and financial center of Britain',
    },
    'Shang hai' :{'country':'China','population':'20million','fact':'Shanghai is the economic center of China.'},
    'Washington' :{'country':'America','population':'70,2000','fact':'Washington is in the northwest of United State.'},
}
for city,information in cities.items():
    print(f"{city.upper()}'s information are:")
    country=information['country']
    population=information['population']
    fact=information['fact']
    print(f"\tCountry:{country.title()}")
    print(f"\tPopulation:{population.title()}")
    print(f"\tFact:{fact.title()}")