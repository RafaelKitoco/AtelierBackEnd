from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from .models import *

# Create your views here.
class RegistrarAPIView(APIView):
    def post(self, request):
        dados = request.data

        serializer = ImagensAtelierSerializer(data=dados)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class BuscarImagens(APIView):
    def get(self, request):
        
        imagens = ImagensAtelier.objects.all()

        serializer = ImagensAtelierSerializer(imagens)

        return Response(serializer.data)
