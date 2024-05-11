from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from artifact.models import Artifact
import random


@api_view(["POST"])
def getRandomArtifact(request):
    try:
        number = request.data.get("number")
        artifacts = Artifact.objects.order_by("?")[:number].values()
        return Response(list(artifacts), status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

