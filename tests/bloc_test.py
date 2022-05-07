import unittest 
from models.bloc import Bloc

class TestBloc(unittest.TestCase):

    def setUp(self):
        self.bloc = Bloc("Shaft", "VE", "Slab", "Summit Crag")