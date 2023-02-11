""" from django.shortcuts import render

# Create your views here.

# Na shell do Django:
from musicians.models import Musician
from bios.models import Bio

# Criamos a instancia de Musician
m1 = Musician(first_name="Jake", last_name="Bowen", instrument="Guitar")
# Utilizando o save, persistimos o objeto na base de dados
m1.save()

# Criando o objeto de Bio
b1 = Bio(author='Example Author', title='Some Bio Title 1', published_date='2001-06-15', musician=m1)
# Persistindo o objeto no banco
b1.save() """