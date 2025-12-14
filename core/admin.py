from django.contrib import admin
from .models import Supplier, Customer, Product, Account, Transaction, InventoryTransaction

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'price', 'quantity']
    search_fields = ['name', 'sku']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'balance']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'date']
    list_filter = ['account']


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity_change', 'date']
