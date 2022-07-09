def make_album(singer_name,album_name,number=None):
    album={'singer':singer_name,'album':album_name}
    if number:
        album['number']=number
    return album

musician=make_album("JACK","the sun",number=69)
print(musician)

