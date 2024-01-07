from django.forms import ModelForm
from .models import Policy, Client, Claim

class PolicyForm(ModelForm):
    class Meta:
        model = Policy
        fields = ['policy_holder', 'coverage_details', 'start_date', 'end_date', 'clients']


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'address', 'contact']


class ClaimForm(ModelForm):
    class Meta:
        model = Claim
        fields = ['policy', 'client', 'status']

        