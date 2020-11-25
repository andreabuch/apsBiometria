from django.db import models
from django.contrib.auth.models import User

# Create your models here. Tabelas e metodos do Banco
class DigitalPessoa(models.Model):
    nome = models.CharField(max_length=50)
    data_inicio = models.DateTimeField(auto_now_add=True) 
    foto_impress_dig = models.ImageField(upload_to='digital')#grava caminho da img e salva no projeto
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.id)

                 
    class Meta: #nome aparece tabela
        db_table = 'Digital'



