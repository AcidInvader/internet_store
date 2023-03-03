from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        # указываем базовую модель
        model = ShopUser
        # поля которые необходимо вывести на странице
        fields = ('имя пользователя', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username',
                  'first_name',
                  'email',
                #   'telephone',
                  'password1',
                  'password2',
                  'age',
                  'avatar'
                  )
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-conttrol'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        
        return data

