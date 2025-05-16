from django import forms

from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelMultipleChoiceField

from ...models import AccessList, AccessListRule, ActionChoices, ProtocolChoices

## Filterform for AccessListRule
## We're using Django's ModelMultipleChoiceField class for this field instead of NetBox's DynamicModelChoiceField because REST API endpoint for the model.
## Once we implement a REST API in step nine, you're free to revisit this form and change access_list to a DynamicModelChoiceField.

class AccessListRuleFilterForm(NetBoxModelFilterSetForm):
    model = AccessListRule
    access_list = forms.ModelMultipleChoiceField(
        queryset=AccessList.objects.all(),
        required=False
    )
    index = forms.IntegerField(
        required=False
    )
    protocol = forms.MultipleChoiceField(
        choices=ProtocolChoices,
        required=False
    )
    action = forms.MultipleChoiceField(
        choices=ActionChoices,
        required=False
    )