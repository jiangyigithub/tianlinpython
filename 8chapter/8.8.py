from pickle import TRUE


def make_album(singer_name,album_name,number=None):
    album={'singer':singer_name,'album':album_name}
    if number:
        album['number']=number
    return album

while TRUE:
    print("\nPlease teel me the information:")
    s_name=input("singer:")
    if s_name=="q": 
        break

    
    a_name=input("album:")
    if a_name=='q':
        break

    musician=make_album(s_name,a_name,number=69)
    print(f"\n{musician}")

