from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    template_name = models.CharField(max_length=100)  # Имя шаблона

    def __str__(self):
        return self.name
