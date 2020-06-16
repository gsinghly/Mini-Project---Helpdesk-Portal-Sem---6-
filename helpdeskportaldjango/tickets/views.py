from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from vanilla import ListView, UpdateView, CreateView

from tickets.forms import TicketForm
from tickets.models import Ticket
from django.core.mail import send_mail
from django.core.mail import EmailMessage


class TicketListView(ListView):
    model = Ticket
    queryset = Ticket.objects.filter(public=True)


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        message = "{name} / {email} : ".format(
        name=form.cleaned_data.get('title'),
        email=form.cleaned_data.get('description'))
        message += "\n\nPriority:{0}".format(form.cleaned_data.get('urgency'))
        message +="\n"
        message += "Please wait while your complaint is being processed. Do not reply to this mail, if you have any queries please contact the administrator"
        rece=form.cleaned_data.get('email')
        email = EmailMessage('Your complaint has been successfully registered!!!',message,to=[rece])
        email.send()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tickets:list')


class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.public and request.user != self.object.created_by:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tickets:list')
