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
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")



        


class Baby(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        
    )
    created_at =models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=30, blank=True,null=True)
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
    PERIOD = (
        ('Halfday', 'Halfday'),
        ('Fullday', 'Fullday'),
        
    )
 
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    name_person = models.CharField(max_length=50, blank=True, null=True)
    person_contact = models.CharField(max_length=50, blank=True, null=True)
    time_in = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    period_of_stay = models.CharField(max_length=20, blank=True, null=True, choices=PERIOD)
 
    payment_status = models.CharField(max_length=20, blank=True, null=True, )
     
    


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
        return f'{self.first_name} {self.last_name}'


class Assign(models.Model):
    # Foreign key pointing to Sitter_on_duty
    sitter_on_duty = models.ForeignKey(
        Sitter_on_duty,
        on_delete=models.CASCADE,
        related_name='assignments',
        null=True,
        blank=True
    )

    # Foreign key pointing to Arrival for baby_assigned
    baby_assigned = models.ForeignKey(
        Arrival,
        on_delete=models.SET_NULL,  # If the Arrival record is deleted, set to null
        related_name='assignments',  # Allows reverse lookup
        null=True,
        blank=True
    )

    def __str__(self):
        sitter_name = f'{self.sitter_on_duty.first_name} {self.sitter_on_duty.last_name}' if self.sitter_on_duty else 'No Sitter Assigned'
        baby_name = f'{self.baby_assigned.first_name} {self.baby_assigned.last_name}' if self.baby_assigned else 'No Baby Assigned'
        return f'Assign: {sitter_name} - Baby: {baby_name}'


class Monthlypay(models.Model):
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True, null=True)
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(null=True, blank=True)
    

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



class Sitter_payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_babies_attended_to = models.IntegerField()
    amount_per_baby = models.DecimalField(default=3000, max_digits=10, decimal_places=2)

    def total(self):
        return self.number_of_babies_attended_to * self.amount_per_baby

    def __str__(self):
        return f"{self.first_name} {self.surname}"







    



    