from django.db.models.signals import post_save
from django.dispatch import receiver
from slugify import slugify

from stories.models import Recipe

@receiver(post_save, sender=Recipe, dispatch_uid="save_recipe")
def save_recipe(sender, instance, created, **kwargs):
    print(sender)
    print(kwargs)
    real_recipe_slug = f"{slugify(instance.title)}-{instance.id}"
    print(instance.slug)
    print(real_recipe_slug)
    if created or not instance.slug == real_recipe_slug:
        instance.slug = f"{slugify(instance.title)}-{instance.id}"
        instance.save()



