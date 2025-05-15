from utilities.choices import ChoiceSet

class ActionChoices(ChoiceSet):
    key = 'AccessListRule.action'

    CHOICES = [
        ('permit', 'Permit', 'green'),
        ('deny', 'Deny', 'red'),
        ('reject', 'Reject (Reset)', 'orange'),
    ]

class ProtocolChoices(ChoiceSet):

    CHOICES = [
        ('tcp', 'TCP', 'blue'),
        ('udp', 'UDP', 'orange'),
        ('icmp', 'ICMP', 'purple'),
    ]