from django import forms
from .models import Cliente, Inmueble, Arriendo, Pago


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = '__all__'


class ArriendoForm(forms.ModelForm):
    class Meta:
        model = Arriendo
        fields = '__all__'


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'