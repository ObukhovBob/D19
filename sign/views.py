import random
from string import hexdigits

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from Board import settings
from .models import BaseRegisterForm
from .models import OneTimeCode
from django.views import View

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = 'sign/signup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseRegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
        return redirect('code', request.POST['username'])

class GetCode(CreateView):
    template_name = 'sign/code.html'
    def get_context_data(self, **kwargs):
        name_user = self.kwargs.get('user')
        if not OneTimeCode.objects.filter(user=name_user).exists():
            code = ''.join(random.sample(hexdigits, 5))
            OneTimeCode.objects.create(user=name_user, code=code)
            user = User.objects.get(username=name_user)
            send_mail(subject=f'Код активации',
                      message=f'Код активации аккаунта: {code}',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[user.email,]
                      )
    def post(self, request, *args, **kwargs):
        if 'code_field' in request.POST:
            user = request.path.split('/')[-1]
            print(user)
            if OneTimeCode.objects.filter(code=request.POST['code_field'], user=user).exists():
                User.objects.filter(username=user).update(is_active=True)
                OneTimeCode.objects.filter(code=request.POST['code_field'], user=user).delete()
            else:
                return render(self.request, 'sign/invalid_code.html')
        return redirect('login')


