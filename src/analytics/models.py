from django.db import models

# Create your models here.
from shortener.models import KirrURL


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, KirrURL):
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None
    
class ClickEvent(models.Model):
    kirr_url    = models.OneToOneField(KirrURL)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return self.kirr_url.url