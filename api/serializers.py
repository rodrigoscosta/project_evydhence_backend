from rest_framework.serializers import ModelSerializer
from .models import Person, Vehicle, Schedule
from rest_framework import serializers

class PersonSerializer(ModelSerializer):
    # Sobrescrevendo o campo dataNascFund para aceitar o formato DD/MM/YYYY
    dataNascFund = serializers.DateField(format='%Y-%m-%d', input_formats=['%d/%m/%Y'])

    class Meta:
        model = Person
        fields = ['idClient', 'nomeRazao', 'cpfCnpj', 'rg', 'dataNascFund', 'sexo', 'email', 'confirmarEmail', 'telefone','cep', 'logradouro', 'numeroResidencia', 'complemento', 'bairro', 'cidade', 'estado', 'uf', 'body', 'updated', 'created']
        extra_kwargs = {
            'body': {'required': False},
            'complemento': {'required': False}
        }

    def validate_dataNascFund(self, value):
        if not value:
            raise serializers.ValidationError("O campo dataNascFund não pode ser vazio.")
        return value


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['idVeiculo', 'idCliente', 'placa', 'marca', 'modelo', 'tipoVeiculo', 'anoFabricacao', 'anoModelo', 'updated', 'created']

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['idSchedule', 'idVeiculo', 'dtaAgendamento', 'horaAgendamento', 'localAgendamento', 'observacao', 'updated', 'created']