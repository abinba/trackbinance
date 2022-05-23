# from django.db import models


# class Symbol(models.Model):
#     content = models.CharField(max_length=10, unique=True)
#
#
# class Price(models.Model):
#     symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
#     price = models.IntegerField(default=0)
#
#     created_at = models.DateTimeField(auto_now_add=True)
