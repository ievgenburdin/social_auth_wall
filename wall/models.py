from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey

from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Comment(MPTTModel):
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            db_index=True, on_delete=models.CASCADE)
    message = models.ForeignKey(Message,
                                null=True,
                                blank=False,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['created']
