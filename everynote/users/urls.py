from django.urls import path

from everynote.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]

#opMaia-ini
#	"~update/": Irá chamar a classe "class UserUpdateView(LoginRequiredMixin,
#	 UpdateView):" q está em views.py
#	"<str:username>/": Irá chamar a classe 'class UserDetailView(LoginRequiredMixin,
#    DetailView):' q está em views.py
#opMaia-fim
