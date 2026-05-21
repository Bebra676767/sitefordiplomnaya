from django import forms
from .models import Application
from core.models import Course

class ApplicationForm(forms.ModelForm):
    start_date = forms.DateField(
        label='Дата начала',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )
    
    class Meta:
        model = Application
        fields = ['course', 'start_date', 'payment_method']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()