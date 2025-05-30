# Imports from modules in netbox
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

from netbox.models import NetBoxModel

#Imports from files in netbox
from ..choices import ActionChoices, ProtocolChoices

## Create the AccessList class collom preferenes

class AccessList(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    default_action = models.CharField(
        max_length=30,
        choices=ActionChoices
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_demo:accesslist', args=[self.pk])

    def get_default_action_color(self):
        return ActionChoices.colors.get(self.default_action)


## Create the AccessListRules class collom preferenes

class AccessListRule(NetBoxModel):
    access_list = models.ForeignKey(
        to=AccessList,
        on_delete=models.CASCADE,
        related_name='rules'
    )
    index = models.PositiveIntegerField()
    protocol = models.CharField(
        max_length=30,
        choices=ProtocolChoices,
        blank=True
    )
    source_prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    source_ports = ArrayField(
        base_field=models.PositiveIntegerField(),
        blank=True,
        null=True
    )
    destination_prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    destination_ports = ArrayField(
        base_field=models.PositiveIntegerField(),
        blank=True,
        null=True
    )
    action = models.CharField(
        max_length=30,
        choices=ActionChoices
    )
    description = models.CharField(
        max_length=500,
        blank=True
    )

    class Meta:
        ordering = ('access_list', 'index')
        unique_together = ('access_list', 'index')

    def __str__(self):
        return f'{self.access_list}: Rule {self.index}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_demo:accesslistrule', args=[self.pk])

    def get_protocol_color(self):
        return ProtocolChoices.colors.get(self.protocol)

    def get_action_color(self):
        return ActionChoices.colors.get(self.action)