from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF informado não é válido'})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': 'O nome não pode conter números!'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':' O RG deve ter 9 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': 'O celular deve estar no padrão 99 99999-9999'})

        return data