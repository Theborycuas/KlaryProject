from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Place
from .serializers import PlaceSerializer

"""VER LISTA DE TODAS LAS CATEGORÍAS"""

class PlaceListView(ListAPIView):
    serializer_class = PlaceSerializer
    permission_classes = ()
    queryset = Place.objects.all()

"""CREAR CATEGORÍAS DESDE LA API"""
class PlaceCreateView(CreateAPIView):
    serializer_class = PlaceSerializer
    permission_classes = ()

"""LISTAR SEGUN ID"""

class PlaceRetriveView(RetrieveAPIView):
    serializer_class = PlaceSerializer
    permission_classes = ()    
    queryset = Place.objects.all()
    lookup_field = 'id'

"""EDITA ELEMENTOS EN LA BASE DE DATOS"""
class PlaceUpdateView(UpdateAPIView):
    serializer_class = PlaceSerializer
    permission_classes = ()    
    queryset = Place.objects.all()
    lookup_field = 'id'

"""ELIMINA ELEMENTOS EN LA BASE DE DATOS"""
class PlaceDestroyView(DestroyAPIView):
    permission_classes = ()    
    queryset = Place.objects.all()
    lookup_field = 'id'    
