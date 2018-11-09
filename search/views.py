from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Banks
from .serializers import BanksSerializer
from rest_framework import filters


class BanksListView(generics.ListAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('ifsc', )


class BranchListView(generics.ListAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('city','id', )
