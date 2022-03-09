import lyricsgenius
import csv
import pandas as pd
import os

SONGS_PATH = './clean_dataset/songs_1970_2018.csv'
ACCESS_TOKEN = '5dsEAw5NbiHcChvDPXMxVQb4cy9g4qpSbLiPHAkmSkKqhvDFbn7spkYnxBFOIkri'

class Scraper:
    def __init__(self):

        self.genius = lyricsgenius.Genius(ACCESS_TOKEN)
        
        file = open(SONGS_PATH, encoding='unicode_escape') 
        csv_reader = csv.reader(file)
        next(csv_reader)

        self.songs = []
        for row in csv_reader:
            self.songs.append({'title': row[1], 'artist': row[2]})
        

    def get_lyrics(self):
        print("Getting all lyrics...")
        all_songs = pd.DataFrame({'album id': [], 'artist_name': []})
        for song in self.songs:
            try:
                info = self.genius.search_song(song['title'], artist=song['artist'])
                song_info = self.genius.song(info.id)
                album_id = song_info['song']['album']['id']
                #lyrics = info.lyrics
                artist_name = song['artist']
            except:
                album_id = None
                artist_name = None

            song_info = pd.DataFrame({'album id': [album_id], 'artist_name': [artist_name]})
            all_songs = pd.concat([all_songs, song_info])

        print("Done!")
        all_songs.to_csv('./dataset/lyrics_alb.csv', index=False)
        return

    def get_artists(self):

        all_artist = pd.DataFrame({'artist name': [], 'alternate names': [], 'description': []})
        for song in self.songs:
            try:
                info = self.genius.search_song(song['title'], artist=song['artist'])
                artist = self.genius.artist(info.primary_artist.id)
                artist_main = artist['artist']['name']
                alternate_names = artist['artist']['alternate_names']
                description = artist['artist']['description']['plain']
            except:
                alternate_names = None
                description = None

            artist_info = pd.DataFrame({'artist name': song['artist'], 'alternate names': [alternate_names], 'description': [description]})
            all_artist = pd.concat([all_artist, artist_info])

        all_artist.to_csv('./dataset/artists.csv', index=False)
        
        return

    def get_albums(self):

        all_albums = pd.DataFrame({'album id': [], 'album name': [], 'full title': [], 'release date': [], 'description': []})
        for song in self.songs:
            try:
                info = self.genius.search_song(song['title'], artist=song['artist'])
                song_info = self.genius.song(info.id)
                album_id = song_info['song']['album']['id']
                album_info = self.genius.album(album_id)

                description = album_info['album']['description_preview']
                release_date = album_info['album']['release_date']
                name = album_info['album']['name']
                full_title= album_info['album']['full_title']
            except:
                description = None
                release_date = None
                name = None
                full_title= None

            albums_info = pd.DataFrame({'album id': [album_id], 'album name': [name], 'full title': [full_title], 'release date': [release_date], 'description': [description]})
            all_albums = pd.concat([all_albums, albums_info])

        all_albums.to_csv('./dataset/albums.csv', index=False)
        
        return

    def delete_files(self):

        if(os.path.exists('./dataset/albums.csv') and os.path.isfile('./dataset/albums.csv')):
            os.remove('./dataset/albums.csv')

        if(os.path.exists('./dataset/artists.csv') and os.path.isfile('./dataset/artists.csv')):
            os.remove('./dataset/artists.csv')

        if(os.path.exists('./dataset/lyrics.csv') and os.path.isfile('./dataset/lyrics.csv')):
            os.remove('./dataset/lyrics.csv')
        return

genius = lyricsgenius.Genius(ACCESS_TOKEN)


scraper = Scraper()
# scraper.get_artists()
# scraper.get_albums()
scraper.get_lyrics()