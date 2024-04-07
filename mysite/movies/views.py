from django.db.models import Q
from django.shortcuts import render

from .models import Moviedata
from .serializers import MovieSerializer
from rest_framework import viewsets


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    # queryset = Moviedata.objects.filter(typ='comedy')
    # 使用 Q 对象进行逻辑或操作
    queryset = Moviedata.objects.filter(Q(typ='comedy') | Q(typ='Comedy'))
    serializer_class = MovieSerializer
