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
    gender = forms.ChoiceField(choices=GENDER, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Gender"}),label="")
    location = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}), label="")
    next_of_kin = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Next Of Kin", "class":"form-control"}), label="")
    next_of_kin_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Next Of Kin Contact", "class":"form-control"}), label="")
    NIN_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"NIN number", "class":"form-control"}), label="")
    recommenders_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Recommender's Name", "class":"form-control"}), label="")
    # recommenders_phone =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Recommender's Contact", "class":"form-control"}), label="")
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
    PERIOD = (
        ('Halfday', 'Halfday'),
        ('Fullday', 'Fullday'),
        
    ) 
    STATUS = (
        ('Pending', 'Pending'),
        ('Cleared', 'Cleared'),
        ('Partial', 'Partial'),
    )  


    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
    last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    name_person = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Person", "class":"form-control"}), label="")
    person_contact = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Number", "class":"form-control"}), label="")
    time_in = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder':'Time in','class': 'form-control'}),required=True,input_formats=['%Y-%m-%d %H:%M:%S']),
 
    period_of_stay = forms.ChoiceField(choices=PERIOD, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Period of Stay"}), label="")
    payment_status = forms.ChoiceField(choices=STATUS, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Payment Status"}), label="")

    # payment_status=forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Payment Status ',"class":"form-check-input"}), label="")
    
    class Meta:
        model = Arrival
        fields = '__all__'


class DepartureForm(forms.ModelForm):
    PERIOD = (
        ('Halfday', 'Halfday'),
        ('Fullday', 'Fullday'),
        
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Cleared', 'Cleared'),
        ('Partial', 'Partial'),
    )
     
    name_person = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Person", "class":"form-control"}), label="")
    person_contact = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Number", "class":"form-control"}), label="")
    time_out = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder':'Time out','class': 'form-control'}),required=True,input_formats=['%Y-%m-%d %H:%M:%S']),
     
    period_stayed = forms.ChoiceField(choices=PERIOD, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Period of Stay"}), label="")
    payment_status = forms.ChoiceField(choices=STATUS, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Payment Status"}), label="")
    comment = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder":"comment"}), label="")


    class Meta:
        model = Departure
        fields = ['arrival', 'name_person','person_contact', 'period_stayed', 'payment_status', 'comment']

    def __init__(self, *args, **kwargs):
        super(DepartureForm, self).__init__(*args, **kwargs)
        self.fields['arrival'].queryset = Arrival.objects.all()
        self.fields['arrival'].empty_label = "--select baby--"
        self.fields['arrival'].widget.attrs.update({
            'class': 'form-control'
        })




class TodoForm(forms.ModelForm):
    task = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class": "form-control", "placeholder":"Event"}),label="")

    class Meta:
        model = TodoItem
        fields = ["task", "is_completed"]



class Sitter_on_dutyForm(forms.ModelForm):
    sitter_number =forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Sitter Number", "class":"form-control"}), label="")
    time_in = forms.DateTimeField(label='', widget=forms.DateTimeInput(attrs={'placeholder':'Time in','class': 'form-control'}),required=True,input_formats=['%Y-%m-%d %H:%M:%S']),

    class Meta:
        model = Sitter_on_duty
        fields = ['record', 'sitter_number']
         
 

    def __init__(self, *args, **kwargs):
        super(Sitter_on_dutyForm, self).__init__(*args, **kwargs)
        self.fields['record'].queryset = Record.objects.all()
        self.fields['record'].empty_label = "--select sitter--"
        self.fields['record'].widget.attrs.update({
            'class': 'form-control'
        })
      



    

class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ['sitter_on_duty', 'baby_assigned']


    def __init__(self, *args, **kwargs):
        super(AssignForm, self).__init__(*args, **kwargs)
        self.fields['sitter_on_duty'].queryset = Sitter_on_duty.objects.all()
        self.fields['sitter_on_duty'].empty_label = "--select sitter--"
        self.fields['sitter_on_duty'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['baby_assigned'].queryset = Arrival.objects.all()
        self.fields['baby_assigned'].empty_label = "--select baby--"
        self.fields['baby_assigned'].widget.attrs.update({
            'class': 'form-control'
        })



class MonthlypayForm(forms.ModelForm):
    
    amount_paid = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Paid", "class":"form-control"}), label="")
    balance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Balance", "class":"form-control"}), label="")
     
    class Meta:
        model = Monthlypay
        fields = ['departure' , 'amount_paid', 'balance']

    def __init__(self, *args, **kwargs):
        super(MonthlypayForm, self).__init__(*args, **kwargs)
        self.fields['departure'].queryset = Departure.objects.all()
        self.fields['departure'].empty_label = "--select baby--"
        self.fields['departure'].widget.attrs.update({
            'class': 'form-control'
        })




class DailypayForm(forms.ModelForm):
     
    amount_paid = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Paid", "class":"form-control"}), label="")
    balance = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Balance", "class":"form-control"}), label="")

    class Meta:
        model = Dailypay
        fields = ['departure', 'amount_paid', 'balance']

    def __init__(self, *args, **kwargs):
        super(DailypayForm, self).__init__(*args, **kwargs)
        self.fields['departure'].queryset = Departure.objects.all()
        self.fields['departure'].empty_label = "--select baby--"
        self.fields['departure'].widget.attrs.update({
            'class': 'form-control'
        })




class Sitter_paymentForm(forms.ModelForm):
#     first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="" )
#     last_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Surname", "class":"form-control"}), label="")
    number_of_babies_attended_to = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Number of Babies Attended To", "class":"form-control"}), label="")
    # amount_per_baby = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Amount Per Baby", "class":"form-control"}), label="")

    class Meta:
        model =  Sitter_payment
        fields = ['sitter_on_duty', 'number_of_babies_attended_to']


    def __init__(self, *args, **kwargs):
        super(Sitter_paymentForm, self).__init__(*args, **kwargs)
        self.fields['sitter_on_duty'].queryset = Sitter_on_duty.objects.all()
        self.fields['sitter_on_duty'].empty_label = "--select sitter--"
        self.fields['sitter_on_duty'].widget.attrs.update({
            'class': 'form-control'
        })
     
class DollstalForm(forms.ModelForm):
    name = forms.CharField(required=True , widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Doll Brand"}), label="")
    price = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Price"}), label="")
    amount_in_stock = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Amount in Stock"}),label="")

    class Meta:
        model = Dollstal
        fields = "__all__"


class PaydollForm(forms.ModelForm):
    amount_bought = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Amount Bought"}),label="")
    class Meta:
        model = Dollpay
        fields = ['dollstal', 'arrival', 'amount_bought' ,  ]

    def __init__(self, *args, **kwargs):
        super(PaydollForm, self).__init__(*args, **kwargs)
        self.fields['dollstal'].queryset = Dollstal.objects.all()
        self.fields['dollstal'].empty_label = "--select doll--"
        self.fields['dollstal'].widget.attrs.update({
            'class': 'form-control'
        })
        
        self.fields['arrival'].queryset = Arrival.objects.all()
        self.fields['arrival'].empty_label = "--select baby--"
        self.fields['arrival'].widget.attrs.update({
            'class': 'form-control'
        })


class ProcurementForm(forms.ModelForm):
    name = forms.CharField(required=True , widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Item"}), label="")
    quantity = forms.IntegerField(required=True , widget=forms.widgets.TextInput(attrs={'class': 'form-control', "placeholder":"Quantity"}), label="")

    class Meta:
        model = Procurement
        fields = "__all__"

        





 



