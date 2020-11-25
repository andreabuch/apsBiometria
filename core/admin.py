from django.contrib import admin
from .models import DigitalPessoa

# Register your models here. Registrar no admin para visualizar tela django

@admin.register(DigitalPessoa)
class DigitalPessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'user']
    
