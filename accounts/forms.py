from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, MinLengthValidator
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9]+$',
                message='Логин должен содержать только латиницу и цифры'
            ),
            MinLengthValidator(6, message='Логин должен быть не менее 6 символов')
        ]
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8, message='Пароль должен быть не менее 8 символов')]
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput
    )
    fio = forms.CharField(
        label='ФИО',
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s]+$',
                message='ФИО должно содержать только кириллицу и пробелы'
            )
        ]
    )
    phone = forms.CharField(
        label='Телефон',
        validators=[
            RegexValidator(
                regex=r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                message='Телефон должен быть в формате 8(XXX)XXX-XX-XX'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': '8(XXX)XXX-XX-XX'})
    )
    email = forms.EmailField(
        label='Email',
        validators=[forms.EmailField.default_validators[0]]
    )
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'fio', 'phone']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                fio=self.cleaned_data['fio'],
                phone=self.cleaned_data['phone']
            )
        return user