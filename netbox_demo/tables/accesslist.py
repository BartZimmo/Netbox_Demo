import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn

from ..models import AccessList, AccessListRule

### Create table with following settings
# linkify = Create a hyperlink on the name
# default action = Also, recall that the default_action field on the AccessList model is a choice field, with a color assigned to each choice.
#                    To display these values, we'll use NetBox's ChoiceFieldColumn class.
# rule_count = counter how many rule that are linked 

class AccessListTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = AccessList
        fields = ('pk', 'id', 'name', 'rule_count', 'default_action', 'comments', 'actions')
        default_columns = ('name', 'rule_count', 'default_action')

## Model -> tabel is part of this model
## fields = available field to show in the table
## default_c = the columns that are enabled by default

#----------------------------





class AccessListRuleTable(NetBoxTable):
    access_list = tables.Column(
        linkify=True
    )
    index = tables.Column(
        linkify=True
    )
    protocol = ChoiceFieldColumn()
    action = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = AccessListRule
        fields = (
            'pk', 'id', 'access_list', 'index', 'source_prefix', 'source_ports', 'destination_prefix',
            'destination_ports', 'protocol', 'action', 'description', 'actions',
        )
        default_columns = (
            'access_list', 'index', 'source_prefix', 'source_ports', 'destination_prefix',
            'destination_ports', 'protocol', 'action', 'actions',
        )