import re
from rest_framework import serializers
from validate_docbr import CPF
from clientes.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, numero_cpf):
        cpf = CPF()
        if not cpf.validate(numero_cpf):
            raise serializers.ValidationError("O CPF deve ser válido")
        return cpf

    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo")
        return nome

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos")
        return rg

    def validate_celular(self, celular):
        model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(model, celular)
        if not resposta:
            raise serializers.ValidationError("O número de celular deve seguir o padrão (99) 99999-9999")
        return celular
