from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Product, Transaction, Supplier, Customer, Account, InventoryTransaction
from .serializers import (
    ProductSerializer, TransactionSerializer, SupplierSerializer,
    CustomerSerializer, AccountSerializer, InventoryTransactionSerializer
)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@login_required
def dashboard(request):
    products_count = Product.objects.count()
    low_stock = Product.objects.filter(quantity__lte=5).count()
    context = {
        'products_count': products_count,
        'low_stock': low_stock,
    }
    return render(request, 'dashboard.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    permission_required = 'core.view_product'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'sku', 'description', 'price', 'quantity']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'core.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'sku', 'description', 'price', 'quantity']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'core.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'core.delete_product'


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class InventoryTransactionViewSet(viewsets.ModelViewSet):
    queryset = InventoryTransaction.objects.all()
    serializer_class = InventoryTransactionSerializer


class InventoryTransactionListView(PermissionRequiredMixin, ListView):
    model = InventoryTransaction
    template_name = 'inventory_transaction_list.html'
    context_object_name = 'inventory_transactions'
    permission_required = 'core.view_inventorytransaction'
