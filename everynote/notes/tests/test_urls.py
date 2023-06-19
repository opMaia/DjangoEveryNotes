# Ver item 54.1 Add the Imported Note

import pytest
from django.urls import reverse, resolve
from .factories import NoteFactory

pytestmark = pytest.mark.django_db

@pytest.fixture
def note():
  return NoteFactory()

def test_list_reverse(): # Item 54.3
    """notes:list should reverse to /notes/."""
    assert reverse('notes:list') == '/notes/'

def test_list_resolve():
    """/notes/ should resolve to notes:list."""
    assert resolve('/notes/').view_name == 'notes:list'

def test_add_reverse(): # Item 54.4
    """notes:add should reverse to /notes/add/."""
    assert reverse('notes:add') == '/notes/add/'

def test_add_resolve():
    """/notes/add/ should resolve to notes:add."""
    assert resolve('/notes/add/').view_name == 'notes:add'

def test_detail_reverse(note): # Item 54.5
    """notes:detail should reverse to /notes/noteslug/."""
    url = reverse('notes:detail',
        kwargs={'slug': note.slug})
    assert url == f'/notes/{note.slug}/'

def test_detail_resolve(note):
    """/notes/noteslug/ should resolve to notes:detail."""
    url = f'/notes/{note.slug}/'
    assert resolve(url).view_name == 'notes:detail'
