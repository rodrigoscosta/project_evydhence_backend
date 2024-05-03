from rest_framework.decorators import api_view
from rest_framework.response import Response
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
            'ListVehicles': '/vehicles/',
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
    person = Person.objects.get(idClient=pk)
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPerson(request):
    data = request.data
    person = Person.objects.create(
        nomeRazao = data['nomeRazao'],
        cpfCnpj = data['cpfCnpj'],
        rg = data['rg'],
        dataNascFund = data['dataNascFund'],
        email = data['email'],
        confirmarEmail = data['confirmarEmail'],
        telefone = data['telefone'],
        body = data['body']
    )
    serializer = PersonSerializer(person, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatePerson(request, pk):
    data = request.data
    person = Person.objects.get(idClient=pk)
    serializer = PersonSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

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

# @api_view(['GET'])
# def getVehicle(request, pk):
#     vehicle = Vehicle.objects.get(idClient=pk)
#     serializer = VehicleSerializer(vehicle, many=False)
#     return Response(serializer.data)

@api_view(['POST'])
def createVehicle(request):
    data = request.data
    vehicle = Vehicle.objects.create(
        idCliente = data['idCliente'],
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
    data = request.data
    vehicle = Vehicle.objects.get(idVeiculo=pk)
    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(idVeiculo=pk)
    vehicle.delete()

    return Response('Veículo excluído!')