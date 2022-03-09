import pandas as pd

albums_data = pd.read_csv("./dataset/albums.csv", na_values=['NA'])
artists_data = pd.read_csv("./dataset/artists.csv", na_values=['NA'])
lyrics_data = pd.read_csv("./dataset/lyrics.csv", na_values=['NA'])
songs_data = pd.read_csv("./dataset/songs_1970_2018.csv", encoding='unicode_escape')

# Modify data fiels
for i in range(len(songs_data.index)):

    try:
        artist_name = songs_data['date'][i]
        songs_data['date'][i] = pd.to_datetime(songs_data['date'][i])

    except:
        continue

# Remove null values
albums_data.dropna(inplace=True)
artists_data.dropna(inplace=True)
lyrics_data.dropna(inplace=True)

# Normalize columns name 
songs_data.rename(columns={'song name': 'song_name',
                        'artist name': 'artist_name', 
                        'date': 'music_date',
                        'rank': 'music_rank'}, inplace=True)
artists_data.rename(columns={'description':'artist_description', 
                            'artist name': 'artist_name',
                            'alternate name': 'alternate_name'}, inplace=True)
albums_data.rename(columns={'description':'album_description',
                            'album id': 'album_id',
                            'album name': 'album_name',
                            'full title': 'full_title',
                            'release date': 'release_date'}, inplace=True)

lyrics_data.rename(columns={'album id': 'album_id',
                            'song name': 'song_name'}, inplace=True)

# Remove duplicateds
removed_dup_albums_data = albums_data.drop_duplicates(subset=['album_id'], keep='first')
removed_dup_artist_data = artists_data.drop_duplicates(subset=['artist_name'], keep='first')
removed_dup_lyrics_data = lyrics_data.drop_duplicates(subset=['song_name'], keep='first')

# Save in new csv files
removed_dup_albums_data.to_csv('./clean_dataset/albums.csv', index=False)
removed_dup_artist_data.to_csv('./clean_dataset/artists.csv', index=False)
removed_dup_lyrics_data.to_csv('./clean_dataset/lyrics.csv', index=False)
songs_data.to_csv('./clean_dataset/songs_1970_2018.csv', index=False)