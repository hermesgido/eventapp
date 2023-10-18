from django import forms
from .models import Event, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        # Add Bootstrap classes to form widgets
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VenueForm, self).__init__(*args, **kwargs)

        # Add Bootstrap classes to form widgets
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
