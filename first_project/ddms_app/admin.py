from django.contrib import admin

# Register your models here.
from .models import Record
from .models import Baby
from .models import Arrival
from .models import Departure
from .models import TodoItem
from .models import Sitter_on_duty
from .models import *

# Register your models here.
admin.site.register(Record)
admin.site.register(Baby)
admin.site.register(Arrival)
admin.site.register(Departure)
admin.site.register(TodoItem)
admin.site.register(Sitter_on_duty)
admin.site.register(Assign)
admin.site.register(Monthlypay)
admin.site.register(Dailypay)
admin.site.register(Sitter_payment)
admin.site.register(Dollstal)
admin.site.register(Dollpay)
admin.site.register(Procurement)
admin.site.register(Issue)

