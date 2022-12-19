from django.shortcuts import render, redirect
from .models import Inscripcion, Institucion
from .forms import FormInscritos

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from .serialiazers import InscripcionSerializer, InstitucionSerializer
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inscripcion(request):
    return render(request, 'inscripcion.html')

def listar_inscripcion(request):
    inscripcion = Inscripcion.objects.all()
    data = {'inscripcion': inscripcion}
    return render(request, 'listar_inscripcion.html', data)

def agregar_inscrito(request):
    form = FormInscritos()
    if request.method == 'POST':
        print(request.POST)
        form = FormInscritos(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscrito.html', data)

def eliminar_inscrito(request, id):
    inscrito =Inscripcion.objects.get(id = id)
    inscrito.delete()
    return redirect('/inscripcion/listar_inscripcion')

def actualizar_inscrito(request, id):
    inscrito_actualizado = Inscripcion.objects.get(id = id)
    form = FormInscritos(instance=inscrito_actualizado)
    if request.method == 'POST':
        form = FormInscritos(request.POST, instance=inscrito_actualizado)
        if form.is_valid() :
            form.save()
        return redirect('/inscripcion/listar_inscripcion')
    data = {'form' : form}
    return render(request, 'actualizar_inscrito.html', data)

def verinscritoDb(request):
    inscrito = Inscripcion.objects.all()
    data = {'inscrito' : list(inscrito.values('nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','estado','observacion'))}

    return JsonResponse(data)

class ListarInscrito(APIView):

    def get(self, request):
        inscri = Inscripcion.objects.all()
        serial = InscripcionSerializer(inscri, many=True)
        return Response(serial.data)


class DetalleInscrito(APIView):

    def get_object(self, pk):
        try:
            return Inscripcion.objects.get(pk=pk)
        except Inscripcion.DoesNotExist:
            return Http404

    def get(self, request, pk):
        inscri = self.get_object(pk)
        serial = InscripcionSerializer(inscri)
        return Response(serial.data)

@api_view(['GET'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerializer(insti, many=True)
        return Response(serial.data)

@api_view(['GET'])
def institucion_detalle(request, pk):
    try:
        insti = Institucion.objects.get(id = pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)