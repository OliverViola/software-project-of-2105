from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


from artifact.models import Artifact


@api_view(['POST'])
def searchArtifacts(request):
    try:
        prompt = request.data.get('prompt')
        obj_artifacts = Artifact.objects.filter(Q(name__icontains=prompt) | Q(description__icontains=prompt)
                                | Q(type__icontains=prompt) | Q(time__icontains=prompt) | Q(creator__icontains=prompt)
                                | Q(museum__icontains=prompt) | Q(material__icontains=prompt)
                                | Q(level__icontains=prompt) | Q(placeOfOrigin__icontains=prompt)
                                | Q(size__icontains=prompt)).values()
        artifact_list = list(obj_artifacts)
        return Response(data=artifact_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
