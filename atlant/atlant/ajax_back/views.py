# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Info
from .serializers import PhotoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class SetData(viewsets.ModelViewSet):

    queryset = Info.objects.all()
    serializer_class = PhotoSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(SetData, self).dispatch(*args, **kwargs)
