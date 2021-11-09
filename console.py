import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# artist1 = Artist("The Beatles")
# artist_repository.save(artist1)
# album1 = Album("Abbey Road", "rock", artist1)
# album_repository.save(album1)

# # artist2 = Artist("Bob Dylan")
# # artist_repository.save(artist2)

# artist_repository.delete_all()
# album_repository.delete_all()

# # specific = artist_repository.select_one(4)
# # print (specific.__dict__)

# # for artist in artist_repository.select_all():
# #     print (artist.__dict__)

artist_repository.delete_one(11)
album_repository.delete_one(2)

# album1.genre = "Pop"
# album_repository.update(album1)

pdb.set_trace()