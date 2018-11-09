from django.urls import path
from . import views


urlpatterns =[
path(r'banks/', views.BanksListView.as_view()),
path(r'branch/', views.BranchListView.as_view()),
]