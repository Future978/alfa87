from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'transactions', views.TransactionViewSet)
router.register(r'suppliers', views.SupplierViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'inventory', views.InventoryTransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.dashboard, name='dashboard'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('inventory/', views.InventoryTransactionListView.as_view(), name='inventory_list'),
]
