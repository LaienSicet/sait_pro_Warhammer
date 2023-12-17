from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'style': 'color: #3e0d4a;'
                                                                                     ' background: #cccaca;'}))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'style': 'color: #3e0d4a;'
                                                                                          ' background: #cccaca;'}))



