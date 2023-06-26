import pytest

from ..models import Note
from .factories import NoteFactory # pg 191

# Connects our tests with our database
pytestmark = pytest.mark.django_db

# Del (vide pg 191)
# def test___str__(): # pag 147
    #  To create a note via create()
    #  note = Note.objects.create(
    #					name="Stracchino",
    #					description="Semi-sweet note that goes well with starches.",
    #					status=Note.Status.SOFT,
    # )

    # To create a note via NoteFactory()
    # Add (vide pg 191)
    # "__str__": é um método especial, como __init__, usado para retornar uma
    # representação de string de um objeto.


def test___str__():
    # opMaia-ini
    # Esta classe valida o cpo status de um note
    print("\t\t10:*** I am in test___str__ do aq /tests/test-models.py\n")
    # opMaia-fim
    # Del (vide pg 192)
    # note = NoteFactory(name="Stracchino")
    # assert note.__str__() == "Stracchino"
    # assert str(note) == "Stracchino"

    # Add (vide pg 192)
    note = NoteFactory()
    print("\t\t12:*** I am in test___str__ do aq /tests/test-models.py\n")
    assert note.__str__() == note.name
    # (del ???)   assert str(note) == note.name
    assert str(note) == note.name


def test_get_absolute_url(): # pg 244
    # opMaia-ini
    # Esta classe valida o cpo status de um note
    print("\t\t10:*** I am in test_get_absolute_url do aq /tests/test-models.py\n")
    # opMaia-fim
    note = NoteFactory()
    url = note.get_absolute_url()

    assert url == f'/notes/{note.slug}/'
