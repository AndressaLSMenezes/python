from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountView.as_view()),
    path("accounts/<int:account_id>/", views.AccountDetailView.as_view()),
]
