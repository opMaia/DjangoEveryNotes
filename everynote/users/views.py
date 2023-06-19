from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
)

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
#opMaia-ini
    print("\t\t*** Estou em UserDetailView do aq /users/views.py")
#opMaia-fim

    model = User
    # These Next Two Lines Tell the View to Index
    #   Lookups by Username
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()
#opMaia-ini
print("\t\t*** Saindo de UserDetailView do aq /users/views.py")
#opMaia-fim

"""
opMaia/22.9 This view corresponds to the page where we entered in the name of
our user. Note the following:
• The fields list contains the fields that are part of the form.
The one field that exists, name, is in this list.
"""
class UserUpdateView(LoginRequiredMixin, UpdateView):
	#opMaia-ini
	# Cpos da lista "fields" abaixo estão defs em /users/models.py
	#opMaia-fim

#opMaia    fields = [
#opMaia        "name",
#opMaia    ]

#opMaia-ini
    print("\t\t*** Estou em UserUpdateView do aq /users/views.py\n")
# The fields list contains the fields that are part of the form.
# A ordem dos cpos na lista abaixo det a ordem em q aparecem na tela
    fields = [
        "name", "bio", "email", "soccer", "coments",
	]
#opMaia-fim

    # We already imported user in the View code above,
    #   remember?
    model = User

    # Send the User Back to Their Own Page after a
    #   successful Update
    def get_success_url(self):
#opMaia-ini
        print("\t\t*** Estou em UserUpdateView.get_success_url do aq /users/views.py")
#opMaia-fim
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
#opMaia-ini
        print("\t\t*** Estou em UserUpdateView.get_object do aq /users/views.py")
#opMaia-fim
        # Only Get the User Record for the
        #   User Making the Request
        return User.objects.get(
            username=self.request.user.username
        )

user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
#opMaia-ini
    print("\t\t*** Estou em UserRedirectView do aq /users/views.py")
#opMaia-fim
    permanent = False

    def get_redirect_url(self):
#opMaia-ini
        print("\t\t*** Estou em UserRedirectView.get_redirect_url do aq /users/views.py")
#opMaia-fim
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )

user_redirect_view = UserRedirectView.as_view()
