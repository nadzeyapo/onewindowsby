from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_name')  # Отображение имени шаблона в списке
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
