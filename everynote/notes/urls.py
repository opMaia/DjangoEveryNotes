# everynote/notes/urls.py

from django.urls import path
from . import views

#opMaia-ini
print("\t\t*** Estou em /notes/urls.py")
#opMaia-fim

app_name = "notes"

"""
app_name: This is how we set the notes app name in an explicit
manner. Amongst other things, setting this here makes
it easy for us as developers to identify which file we are
working in.

path name: The NoteListView is given a URL name of list . We
do this because it allows us greater flexibility in naming
views across a project. Specifically, a too-simple naming
approach starts to be uncomfortable on even medium-sized
projects.
"""

"""
print ("10:/view.Create{" + view + "}")
view=views.NoteDetailView.as_view()
print ("12:/view.Detail{" + view + "}")
view=views.NoteListView.as_view(),
print ("14:/view.List{" + view + "}")
view=views.NoteUpdateView.as_view()
print ("16:/view.Update{" + view + "}")
"""

urlpatterns = [
	path(
		route='',
		view=views.NoteListView.as_view(),
		name='list'
		),
	path(
		route='add/',
		view=views.NoteCreateView.as_view(),
		name='add'
	),
    # Item 55.1
    path(
        route='<slug:slug>/update/',
        view=views.NoteUpdateView.as_view(),
        name='update'
    ),
	# URL Pattern for the NoteDetailView
	path(
		route='<slug:slug>/',
		view=views.NoteDetailView.as_view(),
		name='detail'
	),
]
#opMaia-ini
print("\t\t\turlpatterns=%s" % (urlpatterns,))
print("\t\t*** Saindo de /notes/urls.py\n")
#opMaia-fim
