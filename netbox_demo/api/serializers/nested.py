from rest_framework import serializers

from netbox.api.serializers import WritableNestedSerializer

from netbox_demo.models import AccessList, AccessListRule

class NestedAccessListSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_demo-api:accesslist-detail'
    )

    class Meta:
        model = AccessList
        fields = ('id', 'url', 'display', 'name')

class NestedAccessListRuleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_demo-api:accesslistrule-detail'
    )

    class Meta:
        model = AccessListRule
        fields = ('id', 'url', 'display', 'index')