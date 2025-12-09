#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/8/25
# Version 1.1

class Song:
    # class-level trackers shared by all Song instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # store instance data
        self.name = name
        self.artist = artist
        self.genre = genre

        # update class-level bookkeeping for each new Song
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artist(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        # increment total number of Song instances
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # track all genres used (duplicates allowed unless you choose otherwise)
        cls.genres.append(genre)

    @classmethod
    def add_to_artist(cls, artist):
        # track all artists used
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # count how many songs belong to each genre
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # count how many songs each artist has
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
