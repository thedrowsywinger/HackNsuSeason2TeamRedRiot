from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from accounts.models import ProfileModel

from accounts.forms import CompanyRepresentativeSignupForm

from django.http import HttpResponse



def SigningUpCompanyRepresentativesView(request):

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
            # current_user.is_active = False
            # current_user.save()
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

    return render(request, "accounts/signup.html")



def LoggingInCompanyRepresentativesView(request):

    if 'logging_in' in request.POST:

        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email)
        current_user = User.objects.get(email=email)
        current_user_username=current_user.username

        user = authenticate(request, username=current_user_username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("You have been logged in")
        else:
            print("No user found")
            return HttpResponse("You are still not a verified user of this system")

    return render(request, "accounts/login.html")


def LogoutView(request):

	logout(request)
    
	return redirect('home:home')