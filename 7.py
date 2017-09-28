def make_album(artist, title, number_of_tracks=""):
    if str(number_of_tracks):
        album_info = {"name": artist, "title": title, "number of tracks": number_of_tracks}
    else:
        album_info = {"name": artist, "title": title}
    return album_info


print(make_album("Seal", "Kiss for a rose"))
print(make_album("Reba", "Fancy"))
print(make_album("Dolly", "Jolene"))
