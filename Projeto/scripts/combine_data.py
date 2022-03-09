import pandas as pd
  
albums_data = pd.read_csv("./clean_dataset/albums.csv")
artists_data = pd.read_csv("./clean_dataset/artists.csv")
lyrics_data = pd.read_csv("./clean_dataset/lyrics.csv")
songs_data = pd.read_csv("./clean_dataset/songs_1970_2018.csv", encoding='unicode_escape')
  
merge1 = pd.merge(songs_data, lyrics_data, on='song name', how='inner')

merge2 = pd.merge(merge1, albums_data, on='album id', how='inner')

merge3 = pd.merge(merge2, artists_data , on='artist name', how='inner')

merge3.to_csv('./clean_dataset/combined_data.csv', index=False)