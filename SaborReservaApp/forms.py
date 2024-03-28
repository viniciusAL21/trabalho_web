
from django import forms
from .models import Lanche, Vendedor

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nome_vendedor', 'email', 'contato']
class LancheForm(forms.ModelForm):
    class Meta:
        model = Lanche
        fields = ['produto_oferecido', 'preçodoproduto', 'foto']