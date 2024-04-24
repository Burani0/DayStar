from django.db import models
from django.utils import timezone


from django.utils.timezone import datetime
# Create your models here.


class Record(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    created_at =models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField( )
    gender = models.CharField(max_length=10, choices=GENDER)
    location = models.CharField(max_length=30)
    next_of_kin = models.CharField(max_length=50)
    next_of_kin_phone = models.CharField(max_length=15)
    NIN_number = models.IntegerField(default=0)
    recommenders_name = models.CharField(max_length=50)
    recommenders_phone = models.CharField(max_length=15)
    religion = models.CharField(max_length=20)
    level_of_education = models.CharField(max_length=20 )
    sitter_number = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")



        


class Baby(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    created_at =models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True,null=True)
    Surname = models.CharField(max_length=30, blank=True,null=True)
    gender = models.CharField(max_length=10, blank=True,null=True, choices=GENDER)
    age = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    mother_name = models.CharField(max_length=50, blank=True,null=True)
    mother_phone = models.CharField(max_length=15, blank=True,null=True)
    father_name = models.CharField(max_length=50, blank=True,null=True)
    father_phone = models.CharField(max_length=15, blank=True,null=True)
    any_allegies = models.CharField(max_length=50, blank=True,null=True)
    any_ongoing_medication = models.CharField(max_length=50, blank=True,)
    language_understood = models.CharField(max_length=50, blank=True,null=True)


    def __str__(self):
        return (f'Baby:{self.first_name}')


class Arrival(models.Model):
 
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    name_person = models.CharField(max_length=50, blank=True, null=True)
    person_contact = models.CharField(max_length=50, blank=True, null=True)
    time_in = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    period_of_stay = models.CharField(max_length=20, blank=True, null=True)

 
    payment_status = models.CharField(max_length=20, blank=True, null=True, )
    sitter_assigned = models.CharField(max_length=20, blank=True, null=True)
    


    def __str__(self):
        return (f'Arrival:{self.first_name}')


class Departure(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    name_person = models.CharField(max_length=50, blank=True, null=True)
    person_contact = models.CharField(max_length=50, blank=True, null=True)
    time_out = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    period_stayed = models.CharField(max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return (f'Departure:{self.first_name}')


class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task



class Sitter_on_duty(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    sitter_number = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return (f'Sitter_on_duty:{self.first_name}')


class Assign(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)  
    last_name = models.CharField(max_length=50, blank=True, null=True)
    sitter_number = models.IntegerField(null=True, blank=True)
    baby_assigned = models.CharField(max_length=50, blank=True, null=True   )
     

    def __str__(self):
        return (f'Assign:{self.first_name}')


class Monthlypay(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True, null=True)
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(null=True, blank=True)
    days_attended = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (f'Monthlypay:{self.first_name}')


class Dailypay(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    shift_attended = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True, null=True)
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return (f'Dailypay:{self.first_name}')




    



    