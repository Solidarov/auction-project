from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from auctions.models import AuctionImageModel
from PIL import Image

import os

# Signals for 'AuctionImageModel' model

@receiver(post_save, sender=AuctionImageModel)
def create_thumbnail(sender, instance, **kwargs):
    """
    Create thumbnail for image before saving it.
    """
    if not instance.image:
        return
    original_path = instance.image.path
    filename = os.path.basename(instance.image.name)

    thumbnail_dir = os.path.join(os.path.dirname(original_path), '../thumbnails/')
    thumbnail_path = os.path.join(thumbnail_dir, filename)
    
    os.makedirs(thumbnail_dir, exist_ok=True)

    with Image.open(original_path) as img:
        img.thumbnail((300, 200))
        img.save(thumbnail_path, format=img.format)


@receiver(post_delete, sender=AuctionImageModel)
def delete_image_file(sender, instance, **kwargs):
    """
    Delete image file when corresponding `AuctionImageModel` object is deleted.
    Fistly, delete thumbnail, then delete original image.
    """

    thumbnail_path = instance.get_thumbnail_path(relative=False)
    if thumbnail_path and os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

    if instance.image and instance.image.storage.exists(instance.image.name):
        instance.image.delete(save=False)
