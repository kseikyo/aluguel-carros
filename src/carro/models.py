from django.db import models
from cliente.models import CustomCliente
from datas.models import Datas

# class CarroQuerySet(models.QuerySet):
# 	def is_rented(self):
# 		return self.filter(alugado_por__isnull=False)

# 	def search(self, query):
# 		my_query = (Q(title__icontains=query) | Q(content__icontains=query))
# 		return self.filter(my_query) 

# # A Manager is the interface through which database query operations are provided to Django models.
# class CarroManager(models.Manager):
# 	def get_queryset(self):
# 		return CarroQuerySet(self.model, using=self._db)

# 	def is_rented(self):
# 		return self.get_queryset().is_rented()

# 	def search(self, query=None):
# 		if query is None:
# 			return self.get_queryset.none()
# 		return self.get_queryset().is_rented().search(query)

class Carro(models.Model):
    nome              = models.CharField(max_length=40)
    marca             = models.CharField(max_length=40)
    cor               = models.CharField(max_length=15)
    preco             = models.DecimalField(max_digits=10, decimal_places=2)
    alugado_por       = models.ForeignKey(CustomCliente, on_delete=models.SET_NULL, null=True, blank=True)
    datas_disponíveis = models.ManyToManyField(Datas)

    def __str__(self):
        return self.nome