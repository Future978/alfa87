from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    contact = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=64, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.sku})" if self.sku else self.name


class Account(models.Model):
    ASSET = 'asset'
    LIABILITY = 'liability'
    EQUITY = 'equity'
    REVENUE = 'revenue'
    EXPENSE = 'expense'

    TYPE_CHOICES = [
        (ASSET, 'Asset'),
        (LIABILITY, 'Liability'),
        (EQUITY, 'Equity'),
        (REVENUE, 'Revenue'),
        (EXPENSE, 'Expense'),
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    balance = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.account.name} {self.amount} on {self.date.date()}"


class InventoryTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_transactions')
    quantity_change = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    transaction = models.ForeignKey(Transaction, null=True, blank=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        # Apply change to product quantity
        super().save(*args, **kwargs)
        self.product.quantity = models.F('quantity') + self.quantity_change
        self.product.save()

    def __str__(self):
        return f"{self.product.name} {self.quantity_change} on {self.date.date()}"
