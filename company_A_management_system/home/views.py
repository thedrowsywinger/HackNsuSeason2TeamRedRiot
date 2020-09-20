from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from company_A_app.models import ProfileModel

from home.forms import CompanyRepresentativeSignupForm

from django.http import HttpResponse

# Create your views here.
def HomeView(request):

    if 'logging_in' in request.POST:

        email = request.POST.get('email')
        password = request.POST.get('password')

        current_user = User.objects.filter(email=email)
        
        if current_user.count() > 0:

            current_user = User.objects.get(email=email)
            current_user_username=current_user.username

            user = authenticate(request, username=current_user_username, password=password)
            login(request, user)
            return redirect('company_A_app:dashboard')
        
        else:
            print("No user found")
            return HttpResponse("You are still not a verified user of this system or you just don't exist. Perhaps this is your first time?")

    if 'signing_up' in request.POST:
        print("Am I here")

        data_for_signup = {
			'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'email' : request.POST['company_email'],
			'password1' : request.POST['password1'],
			'password2' : request.POST['password2']
		}

        data_for_profile = {
            'first_name' : request.POST['first_name'],
			'last_name' : request.POST['last_name'],
			'company_email' : request.POST['company_email'],
            'company_role' : request.POST['company_role']
        }

        verifying_signup = CompanyRepresentativeSignupForm(data_for_signup)

        if verifying_signup.is_valid():
            print("Looks good mate")
            verifying_signup.save()
            current_user = User.objects.get(email=request.POST['company_email'])
            current_user.username = str(request.POST['first_name']+"_"+request.POST['last_name'])
            current_user.save()
            print("This is : ", current_user.first_name)
            current_user.is_active = False
            current_user.save()
            model = ProfileModel(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                company_email = request.POST['company_email'],
                company_role = request.POST['company_role'],
                user = current_user
            )
            model.save()
        else:
            print(verifying_signup.errors)

        

    return render(request, "home/home.html")


def LogoutView(request):

	logout(request)
    
	return redirect('home:home')