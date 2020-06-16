from django import forms

from tickets.models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('created_by', )
