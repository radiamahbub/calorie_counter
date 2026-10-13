from django import forms 
from tracker.models import * 


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
        exclude = ['user', 'bmr']


class ConsumedCalorieForm(forms.ModelForm):
    class Meta:
        model = ConsumedCalorieModel
        fields = '__all__' 
        exclude = ['user'] 