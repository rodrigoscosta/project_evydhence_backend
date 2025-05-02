from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import date
from django.utils import timezone

from api.utils import formatar_data
from .serializers import PersonSerializer, VehicleSerializer, ScheduleSerializer
from .models import Person, Vehicle, Schedule

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
            'Delete Vehicle': '/vehicles/<int:pk>/delete/',
            'GetSchedules': '/schedules/',
            'GetSchedulesByVehicle': '/schedules/<int:pk>/',
            'Create Schedules': '/schedules/create',
            'Update Schedules': '/schedules/<int:pk>/update/',
            'Delete Schedules': '/schedules/<int:pk>/delete/',
            'Total Clients': '/persons/total/',
            'Total Clients By Gender': '/persons/total/gender/',
            'Total Schedules By Months': '/schedules/total/months/',
            'Total Vehicles': '/vehicles/total/',
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
    
@api_view(['GET'])
def getPersonById(request, pk):
    try:
        person = Person.objects.get(idClient=pk)
        serializer = PersonSerializer(person, many=False)
        return Response(serializer.data)
    except Person.DoesNotExist:
        return Response({"detail": "Cliente não encontrado."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createPerson(request):
    data = request.data
    #verificar posteriormente
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
    #verificar posteriormente
    #data['dataNascFund'] = formatar_data(data.get('dataNascFund'))  # Formata a data de nascimento

    # Remover a propriedade 'created' dos dados enviados, se estiver presente
    if 'created' in data:
        data.pop('created')

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

    # Remover a propriedade 'created' dos dados enviados, se estiver presente
    if 'created' in data:
        data.pop('created')

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


@api_view(['GET'])
def getSchedules(request):
    schedules = Schedule.objects.all()
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSchedulesByVehicle(request, pk):
    schedule = Schedule.objects.filter(idVeiculo=pk)
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createSchedule(request):
    data = request.data

    data['dtaAgendamento'] = formatar_data(data.get('dtaAgendamento'))

    # Obtém o objeto Vehicle correspondente ao ID fornecido
    idVeiculo = data.get('idVeiculo')
    if idVeiculo:
        try:
            veiculo = Vehicle.objects.get(pk=idVeiculo)
        except Person.DoesNotExist:
            return Response({"message": "Vehicle with ID {} does not exist".format(idVeiculo)}, status=400)
    else:
        return Response({"message": "idVeiculo is required"}, status=400)

    schedule = Schedule.objects.create(
        idVeiculo = veiculo,
        dtaAgendamento = data['dtaAgendamento'],
        horaAgendamento = data['horaAgendamento'],
        localAgendamento = data['localAgendamento'],
        observacao = data['observacao'],
    )
    serializer = ScheduleSerializer(schedule, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateSchedule(request, pk):
    try:
        schedule = Schedule.objects.get(idSchedule=pk)
    except Schedule.DoesNotExist:
        return Response({"error": "Agendamento não encontrado"}, status=404)

    data = request.data

    # Formatar a data do agendamento
    data['dtaAgendamento'] = formatar_data(data.get('dtaAgendamento'))

    # Remover a propriedade 'created' dos dados enviados, se estiver presente
    if 'created' in data:
        data.pop('created')

    serializer = ScheduleSerializer(schedule, data=data, partial=True)

    if serializer.is_valid():
        updated_schedule = serializer.save()
        return Response({"message": "Agendamento atualizado com sucesso", "data": serializer.data})
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteSchedule(request, pk):
    schedule = Schedule.objects.get(idSchedule=pk)
    schedule.delete()

    return Response('Agendamento excluído!')

@api_view(['GET'])
def totalClients(request):
    total = Person.objects.count() 
    return Response({"qtdClientes": total})

@api_view(['GET'])
def totalClientsByGender(request):
    clientes_por_sexo = Person.objects.values('sexo').annotate(total=Count('idClient'))

    # Ajustando o formato de saída para o frontend
    resultado = [{'sexo': cliente['sexo'], 'qtdClientes': cliente['total']} for cliente in clientes_por_sexo]

    return Response(resultado)


@api_view(['GET'])
def totalSchedulesByMonths(request):
    # Pega o parâmetro 'ano' da URL, se não vier nada, usa o ano atual
    ano_param = request.query_params.get('ano')
    try:
        ano = int(ano_param) if ano_param else date.today().year
    except ValueError:
        return Response({'error': 'Ano inválido.'}, status=400)

    # Define o primeiro e último dia do ano selecionado
    start_date = date(ano, 1, 1)
    end_date = date(ano, 12, 31)

    # Filtra apenas as vistorias realizadas dentro do ano selecionado
    vistoria_por_mes = (
        Schedule.objects
        .filter(dtaAgendamento__range=(start_date, end_date))
        .annotate(mes=TruncMonth('dtaAgendamento'))
        .values('mes')
        .annotate(total=Count('idSchedule'))
        .order_by('mes')
    )

    meses_pt = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    resultado = [
        {
            'mes': f"{meses_pt[registro['mes'].month - 1]}/{registro['mes'].year}",
            'qtdVistorias': registro['total']
        }
        for registro in vistoria_por_mes
    ]

    return Response(resultado)

@api_view(['GET'])
def totalVehicles(request):
    total = Vehicle.objects.count() 
    return Response({"qtdVeiculos": total})

@api_view(['GET'])
def getNextSchedules(request):
    hoje = timezone.now()

    vistorias = (
        Schedule.objects
        .filter(dtaAgendamento__gte=hoje)
        .values(
            'idVeiculo__idCliente__nomeRazao',
            'dtaAgendamento',
            'horaAgendamento',
            'localAgendamento'
        )
        .order_by('dtaAgendamento')
    )

    resultado = [
        {
            'cliente': vistoria['idVeiculo__idCliente__nomeRazao'],
            'data': vistoria['dtaAgendamento'],
            'hora': vistoria['horaAgendamento'],
            'local': vistoria['localAgendamento']
        }
        for vistoria in vistorias
    ]

    return Response(resultado)