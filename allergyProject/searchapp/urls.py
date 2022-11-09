from django.urls import path
from . import views as searchviews

app_name = 'searchapp'

urlpatterns = [
    path('', searchviews.searchResult, name='searchResult'),
]

