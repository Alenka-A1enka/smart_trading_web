from .models import CustomSettings
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

class CustomSettingsForm(ModelForm):
    class Meta:
        model = CustomSettings
        fields = ['user_name', 'company_ticker', 'company_name', 'time_laps_list']

        widgets = {
            'company_ticker': TextInput(attrs=
            {
                'hidden': 'true',
                'class': 'form_control',
                'id': 'input1',
            }),
            'user_name': TextInput(attrs={
                'hidden': 'true',
                'class': 'form_control',
                'id': 'input2',
            }),
            # 'neuro_methods_list': TextInput(attrs=
            # {
            #     'hidden': 'true',
            #     'class': 'form_control',
            #     'id': 'input2'
            # }),
            'time_laps_list': TextInput(attrs=
            {
                'hidden': 'true',
                'class': 'form_control',
                'value': '1H',
                'id': 'input3',
            }),
            # 'news_source_list': TextInput(attrs=
            # {
            #     'class': 'form_control',
            #     'id': 'input4'
            # }),
        }



