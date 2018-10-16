from wagtail_tinify.models import TinyPngOptimizeThread
from wagtail.images import get_image_model
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


rendition_model = get_image_model().get_rendition_model()


@receiver(post_save, sender=rendition_model)
def rendition_optimize(sender, instance, **kwargs):
    TinyPngOptimizeThread(instance).start()
