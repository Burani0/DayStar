from django import forms
from .models import Record
from .models import Baby
from .models import Arrival
from .models import Departure
from .models import TodoItem
from .models import Sitter_on_duty
from .models import *

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Your Email Address')



class ResetPasswordForm(forms.Form):
    code = forms.CharField(label='6-digit Code', max_length=6, min_length=6)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")



# Create Add Record Form
class AddRecordForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    date_of_birth = forms.DateField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Date Of Birth", "class":"form-control"}), label="")
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Gender"}))
    location = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}), label="")
    next_of_kin = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Next Of Kin", "class":"form-control"}), label="")
    next_of_kin_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Next Of Kin Contact", "class":"form-control"}), label="")
    NIN_number = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"NIN number", "class":"form-control"}), label="")
    recommenders_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Recommender's Name", "class":"form-control"}), label="")
    recommenders_phone =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Recommender's Contact", "class":"form-control"}), label="")
    religion = forms.CharField( required=False, widget=forms.widgets.TextInput(attrs={"placeholder":" Religion", "class":"form-control"}), label="")
    level_of_education = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Education Background", "class":"form-control"}), label="")
    sitter_number =forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sitter Number", "class":"form-control"}), label="")
    phone_number =  forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sitter's Contact", "class":"form-control"}), label="")

 
    class Meta:
        model = Record
        exclude = ("user",)


class AddBabyForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Gender"}), label="")
    age = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
    location = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}), label="")
    mother_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mother's Name", "class":"form-control"}), label="")
    mother_phone = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mother's Contact", "class":"form-control"}), label="")
    father_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Name", "class":"form-control"}), label="")
    father_phone = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Father's Contact", "class":"form-control"}), label="")
    any_allegies = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Any Allegies", "class":"form-control"}), label="")
    any_ongoing_medication = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Any ongoing medical condition"}),label="")
    language_understood = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Languages Understood"}),label="")
    
    class Meta:
        model = Baby
        fields = '__all__'
        

    
class ArrivalForm(forms.ModelForm):

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    name_person = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Person", "class":"form-control"}), label="")
    person_contact = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Number", "class":"form-control"}), label="")
    time_in = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder':'Time in','class': 'form-control'}),required=True,input_formats=['%Y-%m-%d %H:%M:%S']),
    period_of_stay = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Period of Stay ',"class":"form-check-input"}), label="")
    payment_status=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Payment Status ',"class":"form-check-input"}), label="")
    
    class Meta:
        model = Arrival
        fields = '__all__'


class DepartureForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    name_person = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Person", "class":"form-control"}), label="")
    person_contact = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Number", "class":"form-control"}), label="")
    time_out = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder':'Time out','class': 'form-control'}),required=True,input_formats=['%Y-%m-%d %H:%M:%S']),
    period_stayed = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Period Stayed', 'class': 'form-control'}), label="")
    payment_status=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Payment Status ',"class":"form-check-input"}), label="")


    class Meta:
        model = Departure
        fields = '__all__'


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["task", "is_completed"]


class Sitter_on_dutyForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    sitter_number =forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sitter Number", "class":"form-control"}), label="")

    class Meta:
        model = Sitter_on_duty
        fields = "__all__"


# class AssignForm(forms.ModelForm):
#     sitter_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
     
#     baby_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Babies Assigned", "class":"form-control"}), label="")
   
#     class Meta:
#         model = Assign
#         fields = "__all__"

class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ['sitter_on_duty', 'baby_assigned']



class MonthlypayForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    payment_status = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Payment Status", "class":"form-control"}), label="")
    amount_paid = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Paid", "class":"form-control"}), label="")
    balance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Balance", "class":"form-control"}), label="")
     
    class Meta:
        model = Monthlypay
        fields = "__all__"


class DailypayForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    shift_attended = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Shift Attended", "class":"form-control"}), label="")

    payment_status = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Payment Status", "class":"form-control"}), label="")
    amount_paid = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Paid", "class":"form-control"}), label="")
    balance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Balance", "class":"form-control"}), label="")

    class Meta:
        model = Dailypay
        fields = "__all__"



class Sitter_paymentForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    number_of_babies_attended_to = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Number of Babies Attended To", "class":"form-control"}), label="")
    # amount_per_baby = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Per Baby", "class":"form-control"}), label="")

    class Meta:
        model =  Sitter_payment
        fields = "__all__"
     
        # model = BabyAttendance
        # fields = ['first_name', 'surname', 'number_of_babies_attended_to', 'amount_per_baby']



 



