from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
  first_name = forms.CharField(label="Nome")
  last_name = forms.CharField(label="Sobrenome")
  email = forms.EmailField(label="E-mail")
  document_rg = forms.CharField(label="RG")
  document_cpf = forms.CharField(label="CPF")
  birth_date = forms.DateField(label="Data de Nascimento")
  area_code = forms.CharField(label="DDD")
  phone_number = forms.CharField(label="Telefone")
  country = forms.CharField(label="País")
  state = forms.CharField(label="UF")
  city = forms.CharField(label="Cidade")

  class Meta:
    model = Customer
    fields = (
      "first_name",
      "last_name",
      "email",
      "document_rg",
      "document_cpf",
      "birth_date",
      "area_code",
      "phone_number",
      "country",
      "state",
      "city",
    )