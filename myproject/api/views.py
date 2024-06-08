from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from base.models import Person


@api_view(['GET'])
def getData(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)