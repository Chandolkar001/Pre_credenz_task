from django.http import request
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile
import re

def index(request):
	if request.method == 'POST':

		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		 
		if password1 != password2:
			messages.error(request, 'Password don\'t match.')
			return render(request, 'task3/home.html')
		
		email = request.POST.get('email')
		username = request.POST.get('username')
        

		pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
		mess = bool(pattern.findall(email))




		if User.objects.filter(email = email).exists():
			messages.error(request, 'This email already exists in the database')
			return render(request, 'textform/home.html')

		if mess == False:
			messages.error(request, 'The email entered is not of the preferred format. Please enter the email in proper format(eg abc@xyz.com, abc@xyz.gov, abc@xyz.org)')
			return render(request, 'textform/home.html')
        
		if User.objects.filter(username = username).exists():
			messages.error(request, 'This username already exists')
			return render(request, 'textform/home.html')
		

		newUser = User.objects.create_user(username = username, email = email, password = password1)

		profile = Profile(user = newUser)
        
		profile.save()
		

		messages.success(request, 'Your account has been created successfully')

		return redirect ('login')

	return render(request, 'textform/home.html')
		
def login(request):
	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(request, username = username, password = password)

		if user is not None:
			auth.login(request, user)
			return redirect('userHome')
		else:
			messages.error(request, 'Invalid credentials. ')
			return redirect('login')

	return render(request, 'textform/login.html')

def userHome(request):
	if request.method == 'POST':
		userinput = request.POST.get('userinput')
		options  = request.POST.get('')
	return render(request, 'textform/main.html')


def logout(request):
	auth.logout(request)
	messages.info(request, 'You have logged out successfully')
	return redirect('login')
