# A script that's needed to setup django if it's not already running on a server.
# Without this, you won't be able to import django modules
import sys, os, django

# Find the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project base directory to the sys.path
# This means the script will look in the base directory for any module imports
# Therefore you'll be able to import analysis.models etc
sys.path.insert(0, BASE_DIR)

# The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battle.settings")

# This is for setting up django
django.setup()


##################
#############################

from django.test import TestCase
from faker import Faker
from cards.models import Card
from battle import settings

fake = Faker()


class CardTests(TestCase):
    def test_it_creates_a_card(self):
        name = fake.word()
        hp = fake.random_int()
        card = Card.objects.create(name=name, hp=hp)

        assert card.name == name
        assert card.hp == hp
    
    def test_it_stringifies_a_card(self):
        name = fake.word()
        hp = fake.random_int()
        card = Card.objects.create(name=name, hp=hp)

        assert str(card) == f"{name} ({hp})"
