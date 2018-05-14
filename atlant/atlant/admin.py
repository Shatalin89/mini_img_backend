# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from atlant.ajax_back.models import *


@admin.register(Info)
class PersonAdmin(admin.ModelAdmin):
    pass