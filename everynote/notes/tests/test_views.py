# Este aq foi criado c base no Item:53.2 Start With Imports
"""
	We did define a new view: NoteCreateView with a new URL
	pattern. It would be nice to test both of those, the view and the
	URL pattern. It’s also a good idea to have basic tests on our
	other views and URL patterns for completeness.
"""
# Item 53.2
import pytest 
from pytest_django.asserts import (
    assertContains,
    assertRedirects
    )

from django.urls import reverse
from django.contrib.sessions.middleware \
    import SessionMiddleware
from django.test import RequestFactory

from everynote.users.models import User
from ..models import Note
from ..views import (
    NoteCreateView,
    NoteListView,
    NoteDetailView,
    NoteUpdateView
    )
#from .factories import NoteFactory Item 56.1
from .factories import NoteFactory, note

pytestmark = pytest.mark.django_db # connects our tests to the database

"""
We like to start our tests by stubbing out a simple test function
for each view. These stubs are a great place to start when you’re
not sure what view tests need to be written.
"""
# LIST_VIEW
# =========
"""
# Vide item 53.3.1
def test_good_note_list_view_expanded(rf):  
	# Determine the URL
	url = reverse("notes:list")

 	# rf is pytest shortcut to django.test.RequestFactory
	# We generate a request as if from a user accessing
	# the note list view
	request = rf.get(url)

	# Call as_view() to make a callable object
	# callable_obj is analogous to a function-based view
	callable_obj = NoteListView.as_view()

	# Pass in the request into the callable_obj to get an
	# HTTP response served up by Django
	response = callable_obj(request)

	# Test that the HTTP response has 'Note List' in the
	# HTML and has a 200 response code
	assertContains(response, 'Note List') # assertContainsAndCheckStatus
"""

"""
# Vide item 53.3.2
def test_good_note_list_view(rf):
    # Get the request
    request = rf.get(reverse("notes:list"))

    # Use the request to get the response
    response = NoteListView.as_view()(request)

    # Test that the response is valid
    assertContains(response, 'Note List')
"""

# DETAIL_VIEW
# ===========
""" Item 5.1 
def test_good_note_detail_view(rf):
    # Order some note from the NoteFactory
    note = NoteFactory()
"""
# Item 56.1
def test_good_note_detail_view(rf, note):
    # Order some note from the NoteFactory

    # Make a request for our new note
    url = reverse("notes:detail",
        kwargs={'slug': note.slug})
    request = rf.get(url)
    
    # Use the request to get the response
    callable_obj = NoteDetailView.as_view()
    response = callable_obj(request, slug=note.slug)
    # Test that the response is valid
    assertContains(response, note.name)


# CREATE_VIEW
# ===========
# Ver item 53.3.3 A Basic Note Create Test
def test_good_note_create_view(rf, admin_user):
    # Order some note from the NoteFactory
    note = NoteFactory()
    # Make a request for our new note
    request = rf.get(reverse("notes:add"))
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    response = NoteCreateView.as_view()(request)
    # Test that the response is valid
    assert response.status_code == 200


# Ver item 53.4 Really Test the Note List View
def test_note_list_contains_2_notes(rf):
    # Let's create a couple notes
    note1 = NoteFactory()
    note2 = NoteFactory()

    # Create a request and then a response
    # for a list of notes
    request = rf.get(reverse('notes:list'))
    response = NoteListView.as_view()(request)

    # Assert that the response contains both note names
    # in the template.
    assertContains(response, note1.name)
    assertContains(response, note2.name)


# Ver item 53.5 Test the Note Detail View
def test_detail_contains_note_data(rf):
    note = NoteFactory()

    # Make a request for our new note
    url = reverse("notes:detail",
        kwargs={'slug': note.slug})
    request = rf.get(url)

    # Use the request to get the response
    callable_obj = NoteDetailView.as_view()
    response = callable_obj(request, slug=note.slug)

    # Let's test our Cheesy details!
    assertContains(response, note.name)
    assertContains(response, note.get_firmness_display())
    assertContains(response, note.country_of_origin.name)


# Ver item 53.6 Test the Note Create View
def test_note_create_form_valid(rf, admin_user):
    # Submit the note add form
    form_data = {
        "name": "Paski Sir",
        "description": "A salty hard note",
        "firmness": Note.Firmness.HARD
    }
    request = rf.post(reverse("notes:add"), form_data)
    request.user = admin_user
    response = NoteCreateView.as_view()(request)

    # Get the note based on the name
    note = Note.objects.get(name="Paski Sir")

    # Test that the note matches our form
    assert note.description == "A salty hard note"
    assert note.firmness == Note.Firmness.HARD
    assert note.creator == admin_user

# Item 56.2
def test_note_create_correct_title(rf, admin_user):
    """Page title for NoteCreateView should be Add Note."""
    request = rf.get(reverse('notes:add'))
    request.user = admin_user
    response = NoteCreateView.as_view()(request)
    assertContains(response, 'Add Note')

# Item 56.3
def test_good_note_update_view(rf, admin_user, note):
    url = reverse("notes:update",
        kwargs={'slug': note.slug})
    # Make a request for our new note
    request = rf.get(url)
    # Add an authenticated user
    request.user = admin_user
    # Use the request to get the response
    callable_obj = NoteUpdateView.as_view()
    response = callable_obj(request, slug=note.slug)
    # Test that the response is valid
    assertContains(response, "Update Note")

# Item 56.4
def test_note_update(rf, admin_user, note):
    """POST request to NoteUpdateView updates a note
       and redirects.
    """
    # Make a request for our new note
    form_data = {
        'name': note.name,
        'description': 'Something new',
        'firmness': note.firmness
    }
    url = reverse("notes:update",
        kwargs={'slug': note.slug})
    request = rf.post(url, form_data)
    request.user = admin_user
    callable_obj = NoteUpdateView.as_view()
    response = callable_obj(request, slug=note.slug)
    # # Check that the note has been changed
    note.refresh_from_db()
    assert note.description == 'Something new'
