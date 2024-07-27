from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class SigninForm(AuthenticationForm):
	class Meta:
		pass

class SignupForm(UserCreationForm):
	class Meta:
		pass