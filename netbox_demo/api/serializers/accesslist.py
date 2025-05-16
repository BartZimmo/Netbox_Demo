from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer

from ...models import AccessList, AccessListRule
from .nested import *


class AccessListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_demo-api:accesslist-detail'
    )
    rule_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccessList
        fields = (
            'id', 'url', 'display', 'name', 'default_action', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated', 'rule_count',
        )

## Tip: The order in which fields are listed determines the order in which they appear in the object's API representation.

class AccessListRuleSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_demo-api:accesslistrule-detail'
    )
    access_list = NestedAccessListSerializer()
    # source_prefix = PrefixSerializer()
    # destination_prefix = PrefixSerializer()

    class Meta:
        model = AccessListRule
        fields = (
            'id', 'url', 'display', 'access_list', 'index', 'protocol', 'source_prefix', 'source_ports',
            'destination_prefix', 'destination_ports', 'action', 'tags', 'custom_fields', 'created',
            'last_updated',
        )