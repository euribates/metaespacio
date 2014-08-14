from django.views.generic import CreateView, DetailView

from .models import Usuario
from .forms import UsuarioForm


class CreateUser(CreateView):
    model = Usuario
    form_class = UsuarioForm

    def form_valid(self, form):
        redirect_url = super(CreateUser, self).form_valid(form)
        self.object.is_active = False
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()
        return redirect_url


class DetailUser(DetailView):
    model = Usuario
    template_name = "registro/usuario_detalle.html"
