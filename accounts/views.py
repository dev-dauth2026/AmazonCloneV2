from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import SignupForm

class SignUpView(generic.CreateView):
    form_class = SignupForm

    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('shop:home') 

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    # model = User
    # template_name = 'accounts/signup.html'
    # fields = ['username', 'password']  # Specify the fields you want in the form
    # success_url = reverse_lazy('home')  


    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     user = form.save(commit=False)
    #     user.set_password(form.cleaned_data['password'])  # Set the password
    #     user.save()
    #     return response
    # def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data(form=form))

class LoginView(generic.FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('shop/home')  

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogoutView(generic.RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
