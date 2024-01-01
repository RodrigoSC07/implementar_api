from rest_framework import serializers

from enfermeros.models import Enfermero, Datos, Enfermedad


class EnfermeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enfermero
        fields = ('url', 'id', 'cedula', 'nombre', 'apellido', 'genero', 'especialidad', 'celular', 'correo', 'activo',)

class DatosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Datos
        fields = ('url', 'diagnostico', 'peso', 'altura', 'alergia',)

class EnfermedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enfermedad
        fields = ('url', 'familiar',)
