from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/wilayah/pemilu/ppwp/0.json',
        'GET /api/',
    ]

    return Response(routes)

