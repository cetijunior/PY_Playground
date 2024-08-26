'''
def get_formatted_name(first_name,  last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

musician = get_formatted_name('cj',  'hendrix', 'jc')
print(musician)

musician = get_formatted_name('cj', 'hendrix')
print(musician)




def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('cj', 'hendrix', age=20)
print(musician)




def get_formatted_name(first_name,  last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

while True:
    print("\nPlease tell name: \n ('q' to quit)")
    f_name = input("\nfirst: \t")
    if f_name == 'q':
        break
    l_name = input("last: \t")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHell0, {formatted_name}")


'''



albums = {}
survey = True

def make_album(artist_name, album_title, nr_songs = None):

    if nr_songs:
        album = {'name': artist_name, 'title': album_title, 'songs': nr_songs}
    else:
        album = {'name': artist_name, 'title': album_title}

    return album


while True:
    print("\nComplete the fields: \n ('q' to quit)")
    a_name = input("\nArtist Name: \t")
    if a_name == 'q':
        break
    a_title = input("Album Title: \t")
    if a_title == 'q':
        break
    a_songs = int(input("Album Songs: \t"))
    if a_songs == 'q':
        break

    album = make_album(a_name, a_title, a_songs)
    print(f"\nAlbum: \n - Artist Name: {a_name}\n - Album Title: {a_title}\n - Album Songs: {a_songs}")