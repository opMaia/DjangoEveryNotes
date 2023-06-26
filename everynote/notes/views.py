# views.py: Where we put all our note-related views

# from django.shortcuts import render
from django.shortcuts import render
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
    UpdateView,
)
    # TemplateView

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
    fields = [
        'owner', 'name', 'action', 'description', 'status',
        'comment', 'priority', 'due_date',
        'project_id', 'persistent', 'category'
    ]
    # 'comment', 'priority', 'due_date', 'date_completed',

    model = Note # O cpo model aponta p aq models.py e onde está
    print(f"*** model: '{ model }'")
    # print acima: <*** model: '<class 'everynote.notes.models.Note'>

    # automatically set the value of creator
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    # opMaia-ini
    print("\t\t*** Saí de NoteCreateView\n")
    # opMaia-fim


# Usuário: Atualizar um note existente - Item 55.1
# class NoteUpdateView(UpdateView): # Item 55.7
class NoteUpdateView(LoginRequiredMixin, UpdateView): # Obriga fazer login p alt note
    # opMaia-ini
    print("\t\t*** Estou em NoteUpdateView do aq /notes/views.py\n")
    # opMaia-fim
    model = Note
    fields = [
        'owner', 'name', 'action', 'description', 'status',
        'comment', 'priority', 'due_date', 'date_completed',
        'project_id', 'persistent', 'category', 'country_of_creator',
    ]

    action = "Update"


def view_em_tabela(request):
    print("\n==> Entrei em view_em_tabela")
    # context ={
        # "data":"Gfg is the best",
        # "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # }
    # result = [{
        # 'id':211,'owner':'owner41','name':'name41',
        # 'action':'action41','description':'description41',
        # 'comment':'comment41','priority':'41','due_date':'23-07-2024',
        # 'date_completed':'23-06-2023','flag_alive':'S',
        # 'project_id':'BdoRV','creator_id':'1'
    # }]
    # result = [
        # 'id': 211, 'owner': 'owner41', 'name': 'name41',
        # 'action': 'action41', 'description': 'description41',
        # 'comment': 'comment41', 'priority': '41', 'due_date': '23-07-2024',
        # 'date_completed': '23-06-2023', 'flag_alive': 'S',
        # 'project_id': 'BdoRV', 'creator_id': '1'
    # ]

    # render() Combines a given template with a given context dictionary and
    #          returns an HttpResponse object with that rendered text.
    #
    # Como func a função render:
    # Vide detalhes em: https://vegibit.com/django-render-function/
    #                   https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/
    # def render(request, template_name, context=None, content_type=None, status=None, using=None):
    #     """
    #     Return a HttpResponse whose content is filled with the result of calling
    #     django.template.loader.render_to_string() with the passed arguments.
    #     """
    #     content = loader.render_to_string(template_name, context, request, using=using)
    #     return HttpResponse(content, content_type, status)

    # def testing(request):
      # mydata = Member.objects.all().values()
      # template = loader.get_template('template.html')
      # context = {
        # 'mymembers': mydata,
      # }
      # return HttpResponse(template.render(context, request))

    allnotes = Note.objects.all().order_by('-status', 'priority', 'due_date').values()
    #                                         DESC       ASC         ASC
    context = {'allnotes': allnotes}
    print(f"view_em_tabela/17: allnotes:'{allnotes}'")
    return render(request, 'notes/note_table_list_header.html', context)
