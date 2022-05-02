import pdb
from models.bloc import Bloc
from models.boulder import Boulder

import repositories.boulder_repository as boulder_repository
import repositories.bloc_repository as bloc_repository

bloc_repository.delete_all()
boulder_repository.delete_all()

boulder1 = Boulder("Forest Rock", "Slate")
boulder_repository.save(boulder1)

bloc1 = Bloc("Forest Wall Sit-Start", "V3", "Slab", boulder1, True)
bloc_repository.save(bloc1)

bloc2 = Bloc("Heathen Chemistry Low Start", "V11", "Overhang", boulder1, False)
bloc_repository.save(bloc2)