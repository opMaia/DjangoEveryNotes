"""
   Item "40.2 Define a NoteFactory" powered by Factory Boy, a 3rd party library
		It generates Notes objects
"""
from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Note

from everynote.users.tests.factories import UserFactory # 51.2 Modify Note Factory


import pytest # Item 56.1

@pytest.fixture
def note():
  return NoteFactory()


class NoteFactory(factory.django.DjangoModelFactory):
#opMaia-ini
    print("\t\t*** Estou em /notes/tests/factories.py/NoteFactory")
#opMaia-fim
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    status = factory.fuzzy.FuzzyChoice(
                  [x[0] for x in Note.Status.choices]
               )
    country_of_origin = factory.Faker('country_code')
    creator = factory.SubFactory(UserFactory) # 51.2 Modify Note Factory 
#opMaia-ini
    print("\t\t*** Saindo de /notes/tests/factories.py/NoteFactory\n")
#opMaia-fim

    class Meta:
    #opMaia-ini
        print("\t\t*** Estou em /notes/tests/factories.py/Meta")
    #opMaia-fim
        model = Note
    #opMaia-ini
        print("\t\t*** Saindo de /notes/tests/factories.py/Meta\n")
    #opMaia-fim

