from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'relationship_app':  # Change to your app name
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.filter(codename=perm).first()
                if permission:
                    group.permissions.add(permission)
