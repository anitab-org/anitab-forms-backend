from django.db import models

class AbstractTimestamp(models.Model):
    """
    Abstract model for Created Time and Updated Time fields
    """ 

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
