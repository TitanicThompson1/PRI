import pandas as pd

lyrics = pd.read_csv("../clean_dataset/lyrics.csv")
songs = pd.read_csv("../clean_dataset/songs_1970_2018.csv")
albums = pd.read_csv("../clean_dataset/albums.csv")

songs.pop("change")

all = pd.merge(lyrics, songs, how="outer", on="song_name")
all = pd.merge(all, albums, how="outer", on="album_id")

all.drop(['album_id', 'full_title', 'release_date', 'album_description'], axis=1, inplace=True)
all.to_csv("../clean_dataset/songs.csv", index=False)