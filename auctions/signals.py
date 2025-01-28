from django.db.models.signals import post_delete
from django.dispatch import receiver
from auctions.models import AuctionImageModel


@receiver(post_delete, sender=AuctionImageModel)
def delete_image_file(sender, instance, **kwargs):
    """
    Delete image file when corresponding `AuctionImageModel` object is deleted.
    """
    if instance.image and instance.image.storage.exists(instance.image.name):
        instance.image.delete(save=False)