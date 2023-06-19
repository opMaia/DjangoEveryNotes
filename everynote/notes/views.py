# views.py: Where we put all our note-related views

# from django.shortcuts import render

"""
This is a simple view that lists all the notes on a single page.
When we import the Note model, we use a relative import be-
cause we’re importing it from within the same app.
"""
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.generic import ListView, DetailView
from .models import Note

# from django.views.generic import CreateView
from django.views.generic import ( # Item 55.1
    ListView,
    DetailView,
    CreateView,
    UpdateView
)

# Usuário: Exibir lista c todos os notes
class NoteListView(ListView):
#opMaia-ini
    print("\t\t*** Estou em NoteListView do aq /notes/views.py")
#    print("\t\t\t*** Param ListView={" + ListView + "}")
#opMaia-fim
    model = Note
#opMaia-ini
    print("\t\t*** Saí de NoteListView\n")
#opMaia-fim



# Usuário: Exibir os detalhes de um note selec
class NoteDetailView(DetailView):
#opMaia-ini
    print("\t\t*** Estou em NoteDetailView do aq /notes/views.py")
#opMaia-fim
    model = Note
#opMaia-ini
    print("\t\t*** Saí de NoteDetailView\n")
#opMaia-fim


# Usuário: Cadastrar um novo note
# class NoteCreateView(CreateView):
class NoteCreateView(LoginRequiredMixin, CreateView): # Obriga fazer login p cad note
#opMaia-ini
    print("\t\t*** Estou em NoteCreateView do aq /notes/views.py\n")
#opMaia-fim
    fields = ['name', 'description', 'firmness', 'country_of_origin']
    model = Note

	# automatically set the value of creator
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
#opMaia-ini
    print("\t\t*** Saí de NoteCreateView\n")
#opMaia-fim

# Usuário: Atualizar um note existente - Item 55.1
#class NoteUpdateView(UpdateView): # Item 55.7
class NoteUpdateView(LoginRequiredMixin, UpdateView): # Obriga fazer login p alt note
#opMaia-ini
    print("\t\t*** Estou em NoteUpdateView do aq /notes/views.py\n")
#opMaia-fim
    model = Note
    fields = [
        'name',
        'description',
        'firmness',
        'country_of_origin'
    ]
    action = "Update"
