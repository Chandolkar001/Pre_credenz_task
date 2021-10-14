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
		options  = request.POST.get('choice')
		print(options)
		if options == '1':
			rest = extract_num(userinput)
		elif options == '2':
			rest = extract_date(userinput)
		elif options == '3':
			rest = extract_quote(userinput)
		elif options == '4':
			resttemp  = IPvalidatar(userinput)
			if resttemp == 0:
				rest = 'Invalid'
			elif resttemp == 1:
				rest = 'Valid class A'
			elif resttemp == 2:
				rest = 'Valid class B'
			elif resttemp == 3:
				rest = 'Valid class C'
		elif options == '5':
			resttemp = MACvalidatar(userinput)
			if resttemp == 1:
				rest = 'Valid'
			else:
				rest = 'Invalid'
		elif options == '6':
			rest = Cam_to_Sna(userinput)
		print(rest)
		mval = options
		return render(request, 'textform/main.html', {"linknum": rest, "option":mval})
	

	return render(request, 'textform/main.html')

def logout(request):
	auth.logout(request)
	messages.info(request, 'You have logged out successfully')
	return redirect('login')



def extract_num(uinput):
    pattern = re.compile(r'\d{3,}')
    matches = pattern.findall(uinput)
    return matches

def extract_date(userinput):
    pattern = re.compile(r'(19|20\d\d)+[-](0[1-9]|1[0-2])[-](0[1-9]|[1-2][0-9]|3[0-1])')
    matches = pattern.findall(userinput)
    return matches

def extract_quote(userinput):
    initlist = []
    pattern = re.compile(r"(['])([a-zA-Z0-9_.+-;,]+)(['])")
    matches = pattern.finditer(userinput)
    for m in matches:
        x = m.group(2)
        initlist.append(x)
    return initlist

def IPvalidatar(userinput):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
    mess = pattern.finditer(userinput)
    message = bool(pattern.findall(userinput))
    if message == False:
        result = 0
    else:
        for m in mess:
            pick = int(m.group(2))
            if pick > 0 and pick < 127:
                result = 1
            elif pick >= 128 and pick <= 191:
                result = 2
            elif pick >= 192 and pick <= 223:
                result = 3
    
    return result 

def MACvalidatar(userinput):
    pattern = re.compile(r"^([0-9A-Fa-f]{2}[:-])" +"{5}([0-9A-Fa-f]{2})|" +"([0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4}\\." +"[0-9a-fA-F]{4})$")
    message = bool(pattern.findall(userinput))
    if message == True:
        result = 1
    else:
        result = 2
    return result

def Cam_to_Sna(userinput):
  userinput = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', userinput)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', userinput).lower()