from django.db import models

from  django.contrib.auth.models import  User
from django.forms import  ValidationError
import re

from utils.validacpf import valida_cpf

class Perfil(models.Model):
    perfilDoUsuario = models.OneToOneField(User, on_delete = models.CASCADE)
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length = 11)
    endereco = models. CharField(max_length = 50)
    numero = models.CharField(max_length = 5)
    complemento = models.CharField(max_length = 20)
    bairro = models. CharField(max_length = 30)
    cep = models.CharField(max_length = 8)
    cidade = models.CharField(max_length = 20)
    estado = models.CharField(
        default = "SP",
        max_length = 2,
        choices = (
            ('AC' , 'Acre') ,
            ('AL' , 'Alagoas') ,
            ('AP' , 'Amapá') ,
            ('AM' , 'Amazonas') ,
            ('BA' , 'Bahia') ,
            ('CE' , 'Ceará') ,
            ('DF' , 'Distrito Federal') ,
            ('ES' , 'Espírito Santo') ,
            ('GO' , 'Goiás') ,
            ('MA' , 'Maranhão') ,
            ('MT' , 'Mato Grosso') ,
            ('MS' , 'Mato Grosso do Sul') ,
            ('MG' , 'Minas Gerais') ,
            ('PA' , 'Pará') ,
            ('PB' , 'Paraíba') ,
            ('PR' , 'Paraná') ,
            ('PE' , 'Pernambuco') ,
            ('PI' , 'Piauí') ,
            ('RJ' , 'Rio de Janeiro') ,
            ('RN' , 'Rio Grande do Norte') ,
            ('RS' , 'Rio Grande do Sul') ,
            ('RO' , 'Rondônia') ,
            ('RR' , 'Roraima') ,
            ('SC' , 'Santa Catarina') ,
            ('SP' , 'São Paulo') ,
            ('SE' , 'Sergipe') ,
            ('TO' , 'Tocantins') ,

        )

    )


    def __str__(self):
        return f'{self.usuario.first_name}{self.usuario.last_name}'
    def clean( self ):
        error_messages = {}
        if not valida_cpf(self.cpf):
            error_messages['cpf'] = 'Digite um CPF valido'

        if re.search(r'[ˆ0,9]', self.cep):
            error_messages['cep']= 'CEP invalido, digite apenas numeros'
        if error_messages:
            raise ValidationError(error_messages)


