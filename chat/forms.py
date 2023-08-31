from django import forms
import os

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username', 'required': True}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'required': True}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1', 'required': True}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2', 'required': True}))


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': True}))

class ApiKeyForm(forms.Form):
    api_key = forms.CharField(
        label="API Key",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your API key"}),
    )
   
    # def save_api_key_to_env(self):
    #     api_key = self.cleaned_data['api_key']
    #     print(api_key)
    #     # Update the .env file
    #     env_file_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        
    #     try:
    #         with open(env_file_path, 'r') as env_file:
    #             lines = env_file.readlines()

    #         updated_lines = []
    #         api_key_exists = False

    #         for line in lines:
    #             if line.startswith('API_KEY='):
    #                 updated_lines.append(f'API_KEY={api_key}\n')
    #                 api_key_exists = True
    #             else:
    #                 updated_lines.append(line)

    #         if not api_key_exists:
    #             updated_lines.append(f'API_KEY={api_key}\n')

    #         with open(env_file_path, 'w') as env_file:
    #             env_file.writelines(updated_lines)

    #         return True  # Indicate success
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         return False  # Indicate failure