from django.forms import ModelForm
from citys.models import State

# Create the form class.
class StateForm(ModelForm):
    class Meta:
        model = State
        fields = '__all__'
