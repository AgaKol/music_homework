import pdb
from models.artist import Artist

import repositories.artist_repository as artist_repository

artist1 = Artist("The Beatles")
artist_repository.save(artist1)

# artist_repository.delete_all()

pdb.set_trace()