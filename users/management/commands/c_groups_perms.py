from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='manager')
        # Добавить нужные права
        permissions = [
            'view_mailing',
            'block_client',
            'disable_mailing',
        ]
        for perm in permissions:
            permission = Permission.objects.get(codename=perm)
            group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Группа "manager" успешно создана и настроена.'))
