from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
# Item "23.1 Add a Bio Field" do livro 
    bio = models.TextField("Bio", blank=True)

#opMaia-ini
# Os novos cpos definidos abaixo serão colocados na lista "fields" q está no aq
# views.py.
# Feito isso, executaremos "python manage.py makemigrations users" e depois 
# "python manage.py migrate users"
# Isto fará c q estes cpos apareçam na tela e possam ser atualizados   
#
    email = models.CharField(
		_("Email of User"), blank=True, max_length=255
	)
    soccer = models.CharField(
		_("Soccer Team of User"), blank=True, max_length=255
	)
    coments = models.CharField(
		_("Comments of User"), blank=True, max_length=255
	)
#opMaia-fim

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )


