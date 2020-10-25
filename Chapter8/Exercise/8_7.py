def make_album(singer, album, song_number = None):
    if song_number:
        album_info = {"singer": singer, "album": album, "song number": song_number}
    else:
        album_info = {"singer": singer, "album": album}
    return album_info
    
album = make_album("jay", "Twelve new", 12)
print(album)
album = make_album("jay", "A magic jay", 11)
print(album)
album = make_album("jay", "November Chopin", 12)
print(album)