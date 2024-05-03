from rest_framework.serializers import ModelSerializer
from .models import Person, Vehicle

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['idClient', 'nomeRazao', 'cpfCnpj', 'rg', 'dataNascFund', 'email', 'confirmarEmail', 'telefone', 'body', 'updated', 'created']


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['idVeiculo', 'idCliente', 'placa', 'marca', 'modelo', 'tipoVeiculo', 'anoFabricacao', 'anoModelo', 'updated', 'created']