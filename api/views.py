from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.utils import formatar_data
from .serializers import PersonSerializer, VehicleSerializer
from .models import Person, Vehicle

# Create your views here.

@api_view(['GET'])
def getRoute(request):
    route = {
            'ListClients': '/persons/',
            'Select Client': '/persons/<int:pk>/',
            'Create Client': '/persons/create',
            'Update Client': '/persons/<int:pk>/update/',
            'Delete Client': '/persons/<int:pk>/delete/',
            'GetVehicles': '/vehicles/',
            'GetVehiclesByClient': '/vehicles/<int:pk>/',
            'Create Vehicle': '/vehicles/create',
            'Update Vehicle': '/vehicles/<int:pk>/update/',
            'Delete Vehicle': '/vehicles/<int:pk>/delete/'
        }
    return Response(route)

@api_view(['GET'])
def getPersons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPerson(request, pk):
    try:
        person = Person.objects.get(cpfCnpj=pk)
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    except Person.DoesNotExist:
        return Response({"detail": "Cliente não encontrado para o cpfCnpj fornecido."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createPerson(request):
    data = request.data
    #data['dataNascFund'] = formatar_data(data.get('dataNascFund')) 

    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePerson(request, pk):
    try:
        person = Person.objects.get(idClient=pk)
    except Person.DoesNotExist:
        return Response({"error": "Cliente não encontrado"}, status=404)
    
    data = request.data
    data['dataNascFund'] = formatar_data(data.get('dataNascFund'))  # Formata a data de nascimento

    serializer = PersonSerializer(person, data=data)

    if serializer.is_valid():
        updated_person = serializer.save()
        return Response({"message": "Cliente atualizado com sucesso", "data": serializer.data})
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletePerson(request, pk):
    person = Person.objects.get(idClient=pk)
    person.delete()

    return Response('Cliente excluído!')

@api_view(['GET'])
def getVehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getVehiclesByClient(request, pk):
    vehicle = Vehicle.objects.filter(idCliente=pk)
    serializer = VehicleSerializer(vehicle, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createVehicle(request):
    data = request.data

    # Obtém o objeto Person correspondente ao ID fornecido
    idCliente = data.get('idCliente')
    if idCliente:
        try:
            person = Person.objects.get(pk=idCliente)
        except Person.DoesNotExist:
            return Response({"message": "Person with ID {} does not exist".format(idCliente)}, status=400)
    else:
        return Response({"message": "idCliente is required"}, status=400)

    vehicle = Vehicle.objects.create(
        idCliente = person,
        placa = data['placa'],
        marca = data['marca'],
        modelo = data['modelo'],
        tipoVeiculo = data['tipoVeiculo'],
        anoFabricacao = data['anoFabricacao'],
        anoModelo = data['anoModelo']
    )
    serializer = VehicleSerializer(vehicle, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateVehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(idVeiculo=pk)
    except Vehicle.DoesNotExist:
        return Response({"error": "Veículo não encontrado"}, status=404)
    
    data = request.data

    serializer = VehicleSerializer(vehicle, data=data)

    if serializer.is_valid():
        updated_vehicle = serializer.save()
        return Response({"message": "Veículo atualizado com sucesso", "data": serializer.data})
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(idVeiculo=pk)
    vehicle.delete()

    return Response('Veículo excluído!')