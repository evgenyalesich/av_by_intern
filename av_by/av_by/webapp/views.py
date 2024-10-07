# from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
# from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, SuggesterFilterBackend
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, BaseDocumentViewSet
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *

###### ЛЕГКОВЫЕ АВТО ######
class CarRetrieveView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer
    # permission_classes = [IsAuthenticated]
class CarRetrieveListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer
    # permission_classes = [IsAuthenticated]
class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = [IsAuthenticated]
class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer
    permission_classes = [IsAuthenticated]


