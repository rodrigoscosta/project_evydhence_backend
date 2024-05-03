from django.db import models

# Create your models here.

class Person(models.Model):
    idClient = models.AutoField(primary_key=True, unique=True, null=False)
    nomeRazao = models.CharField(max_length=100, null=False)
    cpfCnpj = models.CharField(max_length=16, unique=True, null=False)
    rg = models.CharField(max_length=16, unique=True, null=False)
    dataNascFund = models.DateField(null=False)
    email = models.EmailField(unique=True, null=False)
    confirmarEmail = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11, null=False)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomeRazao
    
    class Meta:
        ordering = ['-updated']


class Vehicle(models.Model):
    idVeiculo = models.AutoField(primary_key=True, unique=True, null=False)
    idCliente = models.ForeignKey(Person, on_delete=models.CASCADE)
    placa = models.CharField(max_length=20, unique=True, null=False)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=20, null=False)
    tipoVeiculo = models.CharField(max_length=20, null=False)
    anoFabricacao = models.CharField(max_length=4, null=False)
    anoModelo = models.CharField(max_length=4, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa
    
    class Meta:
        ordering = ['-updated']