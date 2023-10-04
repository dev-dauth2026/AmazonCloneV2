from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *
from .utils import password_reset_token
from django.conf import settings
from django.core.mail import send_mail

class SignUpView(generic.CreateView):
    template_name="accounts/signup.html"
    form_class=CustomerRegistrationForm
    success_url=reverse_lazy('shop:home')

    # def get_context_data(self,**kwargs):
    #     context=super().get_context_data(**kwargs)
    #     return context
    
    def form_valid(self,form):
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            email =form.cleaned_data.get("email")
            user= User.objects.create_user(username,email,password)
            form.instance.user=user
            login(self.request,user)
            return super().form_valid(form)
        else:

            return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        

class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return render(request,template_name='accounts/logout.html')
    
class LoginView(generic.FormView):
    template_name="accounts/login.html"
    form_class=CustomerLoginForm
    success_url= reverse_lazy('shop:home')

    def form_valid(self, form):
        if form.is_valid():
            uname= form.cleaned_data.get("username")
            pword= form.cleaned_data['password'] 
            usr= authenticate(username=uname, password=pword) 

            if usr is not None and Customer.objects.filter(user=usr).exists():
                login(self.request,usr)

            else:
                return render(self.request, self.template_name,{'form':self.form_class, "error":"Invalid Credential"})


            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form)) 
    
    def get_success_url(self):
        if "next" in self.request.GET:
            next_url=self.request.GET.get("next")
            return next_url
        else:
            return self.success_url



class PasswordForgotView(generic.FormView):
    template_name = "accounts/forgotpassword.html"
    form_class = PasswordForgotForm
    success_url = "/accounts/passwordforgot/?m=s"

    def form_valid(self, form):
        if form.is_valid():

            # get email from user
            email = form.cleaned_data.get("email")
            # get current host ip/domain
            url = self.request.META['HTTP_HOST']
            # get customer and then user
            customer = Customer.objects.get(user__email=email)
            user = customer.user
            # send mail to the user with email
            text_content = 'Please Click the link below to reset your password. '
            html_content = url + "/accounts/password-reset/" + email +\
                "/" + password_reset_token.make_token(user)+ "/"
            send_mail(
                'Password Reset Link | Amazon Clone',
                text_content + html_content,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return super().form_valid(form)
        
        else:

            return self.render_to_response(self.get_context_data(form=form))
    # def get_context_data(self,**kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['bcontact']=BusinessContact.objects.all().order_by("id")
    #     context['btime']=BusinessTime.objects.all().order_by("id")

    #     return context
    


class PasswordResetView(generic.FormView):
    template_name = "accounts/passwordreset.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy('accounts:login')

    def dispatch(self, request, *args, **kwargs):
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        token = self.kwargs.get("token")
        if user is not None and password_reset_token.check_token(user, token):
            pass
        else:
            return redirect(reverse("accounts:passworforgot") + "?m=e")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        
        if form.is_valid():
            password = form.cleaned_data['new_password']
            email = self.kwargs.get("email")
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            return super().form_valid(form)
        else:
            # Form is not valid, handle the error
            return self.render_to_response(self.get_context_data(form=form))

    # def get_context_data(self,**kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context['bcontact']=BusinessContact.objects.all().order_by("id")
    #     context['btime']=BusinessTime.objects.all().order_by("id")

    #     return context


class ProfileAccountView(generic.TemplateView):
    def get(self,request):
        return render(request,template_name='accounts/profile-account.html')
        
        