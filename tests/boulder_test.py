import unittest
from models.boulder import Boulder

class TestBoulder(unittest.TestCase):

    def setUp(self):
        self.boulder = Boulder("Summit Crag", "Hornstone")
    
    def test_boulder_has_name(self):
        self.assertEqual("Summit Crag", self.boulder.name)