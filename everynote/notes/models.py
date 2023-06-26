from django.db import models
# Ver item "27.6 Add the Note Model"
# Ver item "27.6.1" , "27.6.2"
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.urls import reverse
from django.conf import settings  # 49.1 Add a Creator Field


class Note(TimeStampedModel):
    """
       TimeStampedModel automatically gives the model created and modified fields,
       which automatically track when the object is created or modified.
    """
    # opMaia-ini
    print("\t\t*** Estou em Note do aq /notes/modes.py\n")
    # opMaia-fim


    class Status(models.TextChoices):
        # opMaia-ini
        print("\t\t*** Estou em Status do aq /notes/modes.py\n")
        # opMaia-fim
        # Tricky/Ver item "27.6.4"
        # C isso podemos fazer coisas como esta comparação:
        # if note.status == Note.Status.SOFT:
        #    Do Something
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "active", "Active"
        SEMI_SOFT = "suspended", "Suspended"
        HARD = "inactive", "Inactive"

    # Def dos campos de um note
    id = models.BigAutoField("ID", auto_created=True, primary_key=True,
                             serialize=False)
    owner = models.CharField("Owner", max_length=16)
    name = models.CharField("Note Name", max_length=255)
    slug = AutoSlugField("Note Address", unique=True, always_update=False,
                         default="", populate_from="name")
    action = models.CharField("Note Action", max_length=32)
    description = models.TextField("Description", blank=True)
    status = models.CharField("Status", max_length=20,
                                choices=Status.choices,
                                default=Status.UNSPECIFIED)
    comment = models.TextField("Comment", blank=True)
    priority = models.IntegerField("Priority")
    due_date = models.DateField("Due Date", default='')
    # date_completed = models.DateField("Date Completed", default="2023-12-31")
    # date_completed = models.DateField("Date Completed")
    date_completed = models.DateField("Date Completed", default="2023-12-31")
    project_id = models.CharField("Project", max_length=12)
    persistent = models.CharField("Persistent", max_length=1)
    category = models.CharField("Catg", max_length=16)
    # Add a Creator Field (quem cadastrou)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL)
    country_of_creator = CountryField("Country of Creator", blank=True)

    def get_absolute_url(self):
        """Return absolute URL to the Note Detail page."""
        # return reverse('notes:detail',kwargs={"slug": self.slug})
        return reverse('notes:detail', kwargs={"slug": self.slug})

    # Vide "28.6"
    def __str__(self):
        return self.name
