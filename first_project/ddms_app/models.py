from django.db import models
from django.utils import timezone


from django.utils.timezone import datetime
# Create your models here.



class Record(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    location = models.CharField(max_length=30)
    next_of_kin = models.CharField(max_length=50)
    next_of_kin_phone = models.CharField(max_length=15)
    NIN_number = models.CharField(max_length=30)
    recommenders_name = models.CharField(max_length=50)
    recommenders_phone = models.CharField(max_length=15)
    religion = models.CharField(max_length=20)
    level_of_education = models.CharField(max_length=20)
    sitter_number = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Define the Sitter_on_duty model with a ForeignKey to Record
class Sitter_on_duty(models.Model):
    # Reference to a Record
    record = models.ForeignKey(
        Record,
        on_delete=models.CASCADE,  # Deleting the Record deletes the Sitter_on_duty
        related_name='sitters',    # Allows reverse lookup
        null=True,                 # Sitter_on_duty may not always have a Record
        blank=True                 # Allows for flexibility
    )

    
    sitter_number = models.CharField(max_length=4 ,blank=True, null=True)
    time_in = models.DateTimeField(auto_now_add=True , blank=True, null=True)

    def __str__(self):
        if self.record:
            # Separating the fields but through the ForeignKey
            return f' {self.record.first_name} {self.record.last_name} '
        return f'Sitter-on_duty'





        


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
    STATUS = (
        ('Pending', 'Pending'),
        ('Cleared', 'Cleared'),
        ('Partial', 'Partial'),
    )
 
    first_name = models.CharField(max_length=50, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    name_person = models.CharField(max_length=50, blank=True, null=True)
    person_contact = models.CharField(max_length=50, blank=True, null=True)
    time_in = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    period_of_stay = models.CharField(max_length=20, blank=True, null=True, choices=PERIOD)
 
    payment_status = models.CharField(max_length=20, blank=True, null=True, choices=STATUS )
     
    


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Departure(models.Model):
    PERIOD = (
        ('Halfday', 'Halfday'),
        ('Fullday', 'Fullday'),
        
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Cleared', 'Cleared'),
        ('Partial', 'Partial'),
    )
    arrival = models.ForeignKey(
        Arrival,
        on_delete=models.CASCADE,
        related_name='departures',
        null=True,
        blank=True
    )

    
 
    name_person = models.CharField(max_length=50, blank=True, null=True)
    person_contact = models.CharField(max_length=50, blank=True, null=True)
    time_out = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    period_stayed = models.CharField(max_length=20, blank=True, null=True, choices=PERIOD)
    payment_status = models.CharField(max_length=20, blank=True, null=True, choices=STATUS)


    def __str__(self):
        if self.arrival:
            return (
                f'{self.arrival.first_name} '
                f'{self.arrival.last_name}' 
                f'{self.period_stayed}'
            )
        return (
            f'Departure {self.name_person} '
            f'{self.person_contact}'
            f'{self.time_out}'
            f'{self.period_stayed}'
            f'{self.payment_status}'
            
        )


class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task



# class Sitter_on_duty(models.Model):
#     first_name = models.CharField(max_length=50, blank=True,null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     sitter_number = models.IntegerField(blank=True, null=True)
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


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
    departure = models.ForeignKey(
        Departure,
        on_delete=models.CASCADE,  # Deleting the Record deletes the Sitter_on_duty
        related_name='mpays',    # Allows reverse lookup
        null=True,                 # Sitter_on_duty may not always have a Record
        blank=True                 # Allows for flexibility
    )
     
     
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(null=True, blank=True)


    def __str__(self):
        if self.departure:
            # Separating the fields but through the ForeignKey
            return f' {self.departure.first_name} {self.departure.last_name} '
        return f'Monthlypay'

class Dailypay(models.Model):
    departure = models.ForeignKey(
        Departure,
        on_delete=models.CASCADE,  # Deleting the Record deletes the Sitter_on_duty
        related_name='sitters',    # Allows reverse lookup
        null=True,                 # Sitter_on_duty may not always have a Record
        blank=True                 # Allows for flexibility
    )
     
     
    amount_paid = models.CharField(max_length=50, blank=True, null=True)
    balance = models.IntegerField(null=True, blank=True)


    def __str__(self):
        if self.departure:
            # Separating the fields but through the ForeignKey
            return f' {self.departure.first_name} {self.departure.last_name} '
        return f'Dailypay'



class Sitter_payment(models.Model):
    sitter_on_duty = models.ForeignKey(
        Sitter_on_duty,
        on_delete=models.CASCADE,
        related_name='sitters',
        null=True,
        blank=True
    )

    number_of_babies_attended_to = models.IntegerField()
    amount_per_baby = models.DecimalField(default=3000, max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.number_of_babies_attended_to * self.amount_per_baby

    def __str__(self):
        if self.sitter_on_duty:
            return (
                f'Sitter_payment: {self.sitter_on_duty.first_name} '
                f'{self.sitter_on_duty.last_name} - Number of Babies: '
                f'{self.number_of_babies_attended_to} - Amount per Baby: {self.amount_per_baby} - Total Amount: {self.total}'
            )
        return (
            f'Sitter_payment - Number of Babies: {self.number_of_babies_attended_to} '
            f'- Amount per Baby: {self.amount_per_baby}'
            f'- Total Amount: {self.total}'
            
        )



class Dollstal(models.Model):
    name = models.CharField(max_length=50, blank=True,null=True)
    price = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return f'{self.name} {self.price}'


class Dollpay(models.Model):
    dollstal = models.ForeignKey(
        Dollstal,
        on_delete=models.CASCADE,
        related_name='dollpays',
        null=True,
        blank=True
    )
    arrival = models.ForeignKey(
        Arrival,
        on_delete=models.SET_NULL,  # If the Arrival record is deleted, set to null
        related_name='pricedoll',  # Allows reverse lookup
        null=True,
        blank=True
    )
    def __str__(self):
        dollname = f'{self.dollstal.name} {self.dollstal.price}'
        baby_name = f'{self.arrival.first_name} {self.arrival.last_name}'
        return f'Dollpay'
    



    