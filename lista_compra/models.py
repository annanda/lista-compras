# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Item(models.Model):
    nome = models.CharField(max_length = 300)
    categoria = models.CharField(max_length = 200)

    def __str__(self):
        return self.nome
