from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from artifact.models import Artifact
import random


@api_view(["POST"])
def getRandomArtifact(request):
    try:
        number = request.data.get("number")
        artifacts = []
        length = Artifact.objects.count()
        # get random and unrepeatable id numbers
        sequence = []
        while len(sequence) < number:
            num = random.randint(1, length)
            if num not in sequence:
                sequence.append(num)

        for i in sequence:
            artifact = Artifact.objects.filter(id=i).values()[0]
            artifacts.append(artifact)
        return Response(artifacts, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
