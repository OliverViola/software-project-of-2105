from django.urls import path

from artifact.views.getInfo import getRandomArtifact

urlpatterns = [
    path('getRandom/', getRandomArtifact, name='getRandomArtifact'),
]