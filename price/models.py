from django.db import models


class Symbol(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Symbol - {self.name}"


class Price(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Price of symbol: {self.symbol.name} created at: {self.created_at} is: {self.price}"
