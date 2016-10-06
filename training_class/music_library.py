class Song(object):
	def __init__(self, name, album, number = 1, artist):
		self.name = name; self.number = number
		self.__album = album; self.__artist = artist
	
	def get_artist(self):
		return self.__artist
	
	def get_album(self):
		return self.__album
	
	def __str__(self):
		return "{name} {artist}. Album: {album}".format(name = self.name, artist = self.__artist, album = self.__album)

class Album(object):
	def __init__(self, name, artist):
		self.name = name
		self.__artist = artist
		self.songs = {}
	
	def add_song_to_album(self, song):
		self.songs[song.name] = song
	
	def remove_song_from_album(self, song_name):
		del self.songs[song_name]
	
	def get_songs(self):
		return sorted(self.songs.values(), key = lambda song: song.number)
	
	def get_artist(self):
		return self.__artist

class Artist(object):
	def __init__(self, name, description="No info")
		self.name = name
		self.__albums = {}
	
	def add_song_to_artist(self, song):
		if song.get_album().name not in self.__albums:
			self.add_album_to_artist(song.get_album())
		else:
			self.__albums[song.get_album().name].add_song_to_album(song)
	
	def add_album_to_artist(self, album):
		if album.name not in self.__albums:
			self.__albums[album.name] = album
	
	def get_albums(self):
		return sorted(self.__albums.values(), key = lambda album: album.name)
	
	def __str__(self):
		return "{0} \n\t\t{1}\n".format(self.name, self.description)

class Playlist(object):
	def __init__(self, name = "New Playlist"):
		self.name = name
		self.__songs = {}
	
	def add_to_playlist(self, item):
		if isinstance(item, Artist):
			self.__add_from(*[s for al in item.get_albums() for s in al.get_songs()])
		elif isinstance(item, Album):
			self.__add_from(item.get_songs())
		elif isinstance(item, Song):
			self.__add_from(item)
	
	def __add_from(self, *args):
		for s in args:
			if s.name not in self.__songs:
				self.__songs[s.name] = s
	
	def get_songs(self):
		return sorted(self.__songs.values(), key = lambda s: s.name)

