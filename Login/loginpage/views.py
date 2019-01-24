from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import User
import logging

log = logging.getLogger(__name__)

# Create your views here.
def loginpage_view(request):
    log.info('Entered loginpage_view')
    return render(request,'loginpage/MainPage.html')

def login_view(request):
    log.info('Entered login_view')
    return render(request,'loginpage/login.html')

def signup_view(request):
    log.info('Entered signup_view')
    return render(request, 'loginpage/signup.html')

def signup_success(request):
    log.info('Entered signup_success')
    return render(request, 'loginpage/SignupSuccess.html')

def signup(request):
    log.info('Entered signup')
    if request.method=='POST':
        try:
            User.objects.get(username = request.POST.get('username')) or User.objects.get(mailid = request.POST.get('mailid'))
            return render(request, 'loginpage/signup.html', {'UserAlreadyExist': True})
        except User.DoesNotExist:
            userObject = User()
            userObject.username = request.POST.get('username')
            userObject.password = request.POST.get('password')
            userObject.fullname = request.POST.get('fullname')
            userObject.email_id = request.POST.get('mailid')
            userObject.dob = request.POST.get('dob')
            userObject.save()
            log.info('Object saved')
            return render(request, 'loginpage/SignupSuccess.html')

def login(request):
    log.info('Entered login')
    if request.method=='POST':
        try:
            userobject = User.objects.get(username = request.POST.get('username'))
            if userobject.password == request.POST.get('password'):
                return render(request, 'loginpage/LoginSuccess.html')
            else:
                return render(request, 'loginpage/login.html', {'CredentialsIncorrect': True})
        except User.DoesNotExist:
            return render(request, 'loginpage/login.html', {'UsernameIncorrect': True})