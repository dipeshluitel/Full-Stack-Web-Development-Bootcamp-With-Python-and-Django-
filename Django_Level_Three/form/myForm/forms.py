from django import forms
from django.core import validators
from myForm.models import User

#  custom Validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name must start with letter 'z' ")

class FormName(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # verify_mail = forms.EmailField()
    # text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Got you Bot!")
    #     return botcatcher

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_mail']

    #     if email != vmail:
    #         raise forms.ValidationError("Same email should be entered")
    
    class Meta:
        model = User
        fields = "__all__"