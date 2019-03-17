# -*- coding: utf-8 -*-
"""
Database models for django_communes.
"""

from __future__ import absolute_import, unicode_literals
from django.contrib.gis.geos import Point

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Commune(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    # TODO: add field definitions
    name = models.CharField(max_length=255)

    created = models.DateTimeField()
    from django.contrib.gis.db import models
    poly = models.PolygonField()
    rast = models.RasterField(null=True, blank=True)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<Commune, ID: {}>'.format(self.id)
