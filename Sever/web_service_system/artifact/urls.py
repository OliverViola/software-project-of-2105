from django.urls import path

from artifact.views.getInfo import getRandomArtifact
from artifact.views.searchArtifacts import searchArtifacts, recommendArtifacts

urlpatterns = [
    path('getRandom/', getRandomArtifact, name='getRandomArtifact'),
    path('search/', searchArtifacts, name='searchArtifacts'),
    path('recommend/', recommendArtifacts, name='recommendArtifacts'),
]
