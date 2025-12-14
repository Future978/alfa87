from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core import models


class Command(BaseCommand):
    help = 'Create default groups and assign basic permissions'

    def handle(self, *args, **options):
        groups = {
            'Admin': 'Full access',
            'Manager': 'Manage products and inventory',
            'Staff': 'View and update inventory'
        }

        model_names = ['product', 'transaction', 'supplier', 'customer', 'account', 'inventorytransaction']

        for name, desc in groups.items():
            group, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created group {name}'))
            # assign permissions
            for model_name in model_names:
                try:
                    ct = ContentType.objects.get(app_label='core', model=model_name)
                except ContentType.DoesNotExist:
                    continue
                perms = Permission.objects.filter(content_type=ct)
                if name == 'Admin':
                    group.permissions.add(*perms)
                elif name == 'Manager':
                    # allow add/change/view
                    manager_perms = perms.filter(codename__startswith=('add_', 'change_', 'view_'))
                    group.permissions.add(*manager_perms)
                elif name == 'Staff':
                    view_perms = perms.filter(codename__startswith='view_')
                    change_perms = perms.filter(codename__startswith='change_')
                    group.permissions.add(*view_perms)
                    group.permissions.add(*change_perms)

        self.stdout.write(self.style.SUCCESS('Default groups ensured'))
