favorite_places={
    'Jiangyi':['Huang shi','Zhang jiajie'],
    'Tian lin':['Hu nan','Hu bei'],
    'Tian guangrong':['Hu nan','Zhang jiajie'],
}
for name , places in favorite_places.items():
    print(name.title())
    for place in places:
        print(f'\t{place.title()}')
