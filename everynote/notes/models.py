from django.db import models

# Ver item "27.6 Add the Note Model"

# Ver item "27.6.1" , "27.6.2"
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from django_countries.fields import CountryField

from django.urls import reverse

from django.conf import settings # 49.1 Add a Creator Field

class Note(TimeStampedModel):
#opMaia-ini
    print("\t\t*** Estou em Note do aq /notes/modes.py\n")
#opMaia-fim

    class Firmness(models.TextChoices):
#opMaia-ini
		# Esta classe valida o cpo firmness de um note
        print("\t\t*** Estou em Firmness do aq /notes/modes.py\n")
#opMaia-fim
        # Tricky/Ver item "27.6.4"
        # C isso podemos fazer coisas como esta comparação: 
        # if note.firmness == Note.Firmness.SOFT:
        #    Do Something
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    # Def dos campos de um note
    name = models.CharField("Name of Note", max_length=255)
    slug = AutoSlugField("Note Address",
           unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Firmness", max_length=20,
               choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    country_of_origin = CountryField("Country of Origin", blank=True)

	# Add a Creator Field (quem cadastrou)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL
                               )

    def get_absolute_url(self):
        """Return absolute URL to the Note Detail page."""
        return reverse('notes:detail',kwargs={"slug": self.slug})

    def __str__(self):
        return self.name
