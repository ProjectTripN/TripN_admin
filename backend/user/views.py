from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from user.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_data(request):
    Processing().insert_data()
    return Response({'preprocess': 'SUCCESS'})