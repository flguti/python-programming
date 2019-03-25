'''
class Student:
    def __init__(self):
        print('class instantiated')

flavio = Student()
mascus = Student()

#instance variable are created by self
class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def name_and_address(self):
        return self.name + ' lives in ' self.address


student_1 = Student('flavio', 'Toronto')
student_2 = Student('marcus', 'Guelph')

print(student_2.name)
print(student_1.name_and_address())
'''
from random import randint

class Playlist:
    def __init__(self):
        self.playlist = []
    def add_to_playlist(self, song):
        self.playlist.append(song)
#you need to find the index to be removed
    def remove_from_playlist(self, id):
        for idx, song in enumerate(self.playlist):
            if song['id'] == id:
                self.playlist.pop(idx)
    def get_songs(self):
        for song in self.playlist:
            print('{} - by {}'.format(song['tittle'], song['artist']))
    def size(self):
        print(len(my_songs.playlist))
    def shuffle(self):
        for idx, _ in enumerate(self.playlist):
            x = randint(0, len(my_songs.playlist) - 1)
            self.playlist[idx], self.playlist[x] = self.playlist[x], self.playlist[idx]



my_songs = Playlist()
my_songs.add_to_playlist({'id': 0,'tittle': 'i dont know', 'artist': 'Cardi B'})
my_songs.add_to_playlist({'id': 1,'tittle': 'the flag song', 'artist': 'Unknow'})
my_songs.add_to_playlist({'id': 2,'tittle': 'whatever', 'artist': 'Cardi B'})
my_songs.add_to_playlist({'id': 3,'tittle': 'one more song', 'artist': 'Unknow'})
my_songs.add_to_playlist({'id': 4,'tittle': 'another song', 'artist': 'Cardi B'})
my_songs.add_to_playlist({'id': 5,'tittle': 'last song', 'artist': 'Unknow'})
my_songs.get_songs()
#my_songs.remove_from_playlist(1)
my_songs.size()
my_songs.shuffle()
my_songs.get_songs()
#my_songs.size()
