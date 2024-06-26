
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ForgotPasswordForm
from .forms import ResetPasswordForm
from .forms import AddRecordForm
from .models import Record
from .models import Baby
from .forms import AddBabyForm
from .models import Arrival
from .forms import ArrivalForm
from .models import Departure
from .forms import DepartureForm
from .models import TodoItem
from .forms import TodoForm
from .models import Sitter_on_duty
from .forms import Sitter_on_dutyForm
from .models import *
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'index.html')




class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')   

    def form_invalid(self, form):
         
        form.add_error(None, "Username does not match password")
        return super().form_invalid(form)


@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')



def forgot(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
 
            messages.success(request, 'Instructions to reset your password have been sent to your email.')
            return redirect('reset_password')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot.html', {'form': form})

def forgot(request):
    return render(request, 'forgot.html')

def reset_password(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
 
            messages.success(request, 'Password reset successfully!')
            return redirect('login')  
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})

def regester(request):
    return render(request, 'regester.html')



def add_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_record')   
    else:
        form = AddRecordForm()
    return render(request, 'add_record.html', {'form': form})

def record_list(request):
    records = Record.objects.all()
    return render(request, 'record_list.html', {'records': records})

    



def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        if request.method == 'POST':
            delete_it.delete()
            messages.success(request, 'Record deleted successfully')
            return redirect('record_list')
        else:
            messages.warning(request, 'Are you sure you want to delete this record?')
            return redirect('record_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('record_list')

def edit_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record_list')   
    else:
        form = AddRecordForm(instance=record)
    return render(request, 'edit_record.html', {'form': form})
 

def add_baby(request):
    if request.method == 'POST':
        form = AddBabyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_baby')   
    else:
        form = AddBabyForm()
    return render(request, 'add_baby.html', {'form': form})


def baby_list(request):
    records = Baby.objects.all()
    return render(request, 'baby_list.html', {'records': records})



def delete_baby(request, pk):
    if request.user.is_authenticated:
        delete_it = Baby.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfully')
         
        return redirect('baby_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('baby_list')



def edit_baby(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id)
    if request.method == 'POST':
        form = AddBabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return redirect('baby_list')   
    else:
        form = AddBabyForm(instance=baby)
    return render(request, 'edit_baby.html', {'form': form})




def add_arrival(request):
    if request.method == 'POST':
        form = ArrivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_arrival')  
    else:
        form = ArrivalForm()
    return render(request, 'add_arrival.html', {'form': form})


def arrival_list(request):
    records = Arrival.objects.all()
    return render(request, 'arrival_list.html', {'records': records})


def delete_arrival(request, pk):
    if request.user.is_authenticated:
        delete_it = Arrival.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('arrival_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('arrival_list')



def edit_arrival(request, arrival_id):
    arrival = get_object_or_404(Arrival, id=arrival_id)
    if request.method == 'POST':
        form = ArrivalForm(request.POST, instance=arrival)
        if form.is_valid():
            form.save()
            return redirect('arrival_list')   
    else:
        form = ArrivalForm(instance=arrival)
    return render(request, 'edit_arrival.html', {'form': form})





def add_departure(request):
    if request.method == 'POST':
        form = DepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_departure')   
    else:
        form = DepartureForm()
    return render(request, 'add_departure.html', {'form': form})


def departure_list(request):
    records = Departure.objects.all()
    return render(request, 'departure_list.html', {'records': records})


def delete_departure(request, pk):
    if request.user.is_authenticated:
        delete_it = Departure.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('departure_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('departure_list')



def edit_departure(request, departure_id):
    departure = get_object_or_404(Departure, id=departure_id)
    if request.method == 'POST':
        form = DepartureForm(request.POST, instance=departure)
        if form.is_valid():
            form.save()
            return redirect('departure_list')  
    else:
        form = DepartureForm(instance=departure)
    return render(request, 'edit_departure.html', {'form': form})

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, "todo_list.html", {"items": items})

def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_todo")
    else:
        form = TodoForm()
    return render(request, "add_todo.html", {"form": form})

def update_todo(request, pk):
    item = get_object_or_404(TodoItem, id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm(instance=item)
    return render(request, "update_todo.html", {"form": form})





def delete_todo(request, pk):
    if request.user.is_authenticated:
        delete_it = TodoItem.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('todo_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('todo_list')

   



def sitter_on_duty(request):
    if request.method == 'POST':
        form = Sitter_on_dutyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitter_on_duty')   
    else:
        form = Sitter_on_dutyForm()
    return render(request, 'sitter_on_duty.html', {'form': form})

def duty_list(request):
    records = Sitter_on_duty.objects.all()
    return render(request, 'duty_list.html', {'records': records})



def delete_duty(request, pk):
    if request.user.is_authenticated:
        delete_it = Sitter_on_duty.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('duty_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('duty_list')



def edit_duty(request, pk):
    duty = get_object_or_404(Sitter_on_duty, id=pk)
    if request.method == 'POST':
        form = Sitter_on_dutyForm(request.POST, instance=duty)
        if form.is_valid():
            form.save()
            return redirect('duty_list')   
    else:
        form =  Sitter_on_dutyForm(instance=duty)
    return render(request, 'edit_duty.html', {'form': form})



def add_assign(request):
    if request.method == 'POST':
        form = AssignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_assign')   
    else:
        form =  AssignForm()
    return render(request, 'add_assign.html', {'form': form})

def assign_list(request):
    records = Assign.objects.all()
    return render(request, 'assign_list.html', {'records': records})



def delete_assign(request, pk):
    if request.user.is_authenticated:
        delete_it = Assign.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('assign_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('assign_list')



def edit_assign(request, pk):
    assign = get_object_or_404(Assign, id=pk)
    if request.method == 'POST':
        form = AssignForm(request.POST, instance=assign)
        if form.is_valid():
            form.save()
            return redirect('assign_list')   
    else:
        form =  AssignForm(instance=assign)
    return render(request, 'edit_assign.html', {'form': form})


def payments(request):
    return render(request, 'payments.html')


    

def add_monthly(request):
    if request.method == 'POST':
        form = MonthlypayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_monthly')   
    else:
        form =  MonthlypayForm()
    return render(request, 'add_monthly.html', {'form': form})

def monthly_list(request):
    records = Monthlypay.objects.all()
    return render(request, 'monthly_list.html', {'records': records})



def delete_monthly(request, pk):
    if request.user.is_authenticated:
        delete_it = Monthlypay.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('monthly_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('monthly_list')



def edit_monthly(request, pk):
    monthlypay = get_object_or_404(Monthlypay, id=pk)
    if request.method == 'POST':
        form = MonthlypayForm(request.POST, instance=monthlypay)
        if form.is_valid():
            form.save()
            return redirect('monthly_list')   
    else:
        form =  MonthlypayForm(instance=monthlypay)
    return render(request, 'edit_monthly.html', {'form': form})


def add_daily(request):
    if request.method == 'POST':
        form = DailypayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_daily')   
    else:
        form =  DailypayForm()
    return render(request, 'add_daily.html', {'form': form})

def daily_list(request):
    records = Dailypay.objects.all()
    return render(request, 'daily_list.html', {'records': records})



def delete_daily(request, pk):
    if request.user.is_authenticated:
        delete_it = Dailypay.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('daily_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('daily_list')



def edit_daily(request, pk):
    dailypay = get_object_or_404(Dailypay, id=pk)
    if request.method == 'POST':
        form = DailypayForm(request.POST, instance=dailypay)
        if form.is_valid():
            form.save()
            return redirect('daily_list')   
    else:
        form =  DailypayForm(instance=dailypay)
    return render(request, 'edit_daily.html', {'form': form})



def babies_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Baby.objects.filter(
            first_name__icontains=search_query
        ) | Baby.objects.filter(
            last_name__icontains=search_query
        ) | Baby.objects.filter(
            age__icontains=search_query
        ) | Baby.objects.filter(
            gender__icontains=search_query
        )
    else:
        records = Baby.objects.all()

    return render(request, 'baby_list.html', {'records': records, 'user': request.user})






def monthlys_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Monthlypay.objects.filter(
            departure__arrival__first_name__icontains=search_query
        ) | Monthlypay.objects.filter( 
            departure__arrival__last_name__icontains=search_query
        ) | Monthlypay.objects.filter(
            departure__period_stayed__icontains=search_query
        ) | Monthlypay.objects.filter(
            amount_paid__icontains=search_query
        ) | Monthlypay.objects.filter(
            balance__icontains=search_query
        )
    else:
        records = Monthlypay.objects.all()

    return render(request, 'monthly_list.html', {'records': records, 'user': request.user})


def dailys_list(request):
 
    search_query = request.GET.get('search', '')
 
    if search_query:
         
        records = Dailypay.objects.filter(
            departure__arrival__first_name__icontains=search_query
        ) | Dailypay.objects.filter(
            departure__arrival__last_name__icontains=search_query
        ) | Dailypay.objects.filter(
            departure__period_stayed__icontains=search_query
        ) | Dailypay.objects.filter(
            amount_paid__icontains=search_query
        ) | Dailypay.objects.filter(
            balance__icontains=search_query
        )
    else:
 
        records = Dailypay.objects.all()

    return render(request, 'daily_list.html', {'records': records, 'user': request.user})


def dutys_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Sitter_on_duty.objects.filter(
            record__first_name__icontains=search_query
        ) | Sitter_on_duty.objects.filter( 
            record__last_name__icontains=search_query
        ) | Sitter_on_duty.objects.filter(
            sitter_number__icontains=search_query
        )  
    else:
        records =  Sitter_on_duty.objects.all()

    return render(request, 'duty_list.html', {'records': records, 'user': request.user})


def arrivals_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Arrival.objects.filter(
            first_name__icontains=search_query
        ) | Arrival.objects.filter(
            last_name__icontains=search_query
        ) | Arrival.objects.filter(
            period_of_stay__icontains=search_query
        ) | Arrival.objects.filter(
            payment_status__icontains=search_query
        )
    else:
        records = Arrival.objects.all()

    return render(request, 'arrival_list.html', {'records': records, 'user': request.user})


def departures_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Departure.objects.filter(
            arrival__first_name__icontains=search_query
        ) | Departure.objects.filter(
            arrival__last_name__icontains=search_query
        ) | Departure.objects.filter(
            time_out__icontains=search_query
        ) | Departure.objects.filter(
            period_stayed__icontains=search_query
        ) | Departure.objects.filter(
            payment_status__icontains=search_query
        )
    else:
        records = Departure.objects.all()

    return render(request, 'departure_list.html', {'records': records, 'user': request.user})


def rege_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Record.objects.filter(
            first_name__icontains=search_query
        ) | Record.objects.filter(
            last_name__icontains=search_query
        ) | Record.objects.filter(
            sitter_number__icontains=search_query
        ) | Record.objects.filter(
            gender__icontains=search_query
        )
    else:
        records = Record.objects.all()

    return render(request, 'record_list.html', {'records': records, 'user': request.user})



def give_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Assign.objects.filter(
            sitter_on_duty__record__first_name__icontains=search_query
        ) | Assign.objects.filter(
            sitter_on_duty__record__last_name__icontains=search_query
        ) | Assign.objects.filter(
            baby_assigned__first_name__icontains=search_query
        ) | Assign.objects.filter(
            baby_assigned__last_name__icontains=search_query
        )
    else:
        records =  Assign.objects.all()

    return render(request, 'assign_list.html', {'records': records, 'user': request.user})


def add_sitter_pay(request):
    if request.method == 'POST':
        form = Sitter_paymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_sitter_pay')
    else:
        form =  Sitter_paymentForm()

    return render(request, 'add_sitter_pay.html', {'form': form})

 
def sitter_pay_list(request):
    records = Sitter_payment.objects.all()
    return render(request, 'sitter_pay_list.html', {'records': records})


def delete_sitterpay(request, pk):
    if request.user.is_authenticated:
        delete_it = Sitter_payment.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('sitter_pay_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('sitter_pay_list')



def edit_sitterpay(request, pk):
    sitter_pay = get_object_or_404(Sitter_payment, id=pk)
    if request.method == 'POST':
        form = Sitter_paymentForm(request.POST, instance=sitter_pay)
        if form.is_valid():
            form.save()
            return redirect('sitter_pay_list') 
    else:
        form =  Sitter_paymentForm(instance=sitter_pay)
    return render(request, 'edit_sitter_pay.html', {'form': form})

def search_pay_sitter(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Sitter_payment.objects.filter(
            sitter_on_duty__record__first_name__icontains=search_query
        ) | Sitter_payment.objects.filter(
            sitter_on_duty__record__last_name__icontains=search_query
        ) | Sitter_payment.objects.filter(
            number_of_babies_attended_to__icontains=search_query
        ) 
    else:
        records =  Sitter_payment.objects.all()

    return render(request, 'sitter_pay_list.html', {'records': records, 'user': request.user})


def add_dollstal(request):
    if request.method == 'POST':
        form = DollstalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_dollstal')
    else:
        form =  DollstalForm()

    return render(request, 'add_dollstal.html', {'form': form})
 
def dollstal_list(request):
    records = Dollstal.objects.all()
    return render(request, 'dollstal_list.html', {'records': records})


def delete_dollstal(request, pk):
    if request.user.is_authenticated:
        delete_it = Dollstal.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('dollstal_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('dollstal_list')



def edit_dollstal(request, pk):
    dolls = get_object_or_404(Dollstal, id=pk)
    if request.method == 'POST':
        form = DollstalForm(request.POST, instance=dolls)
        if form.is_valid():
            form.save()
            return redirect('dollstal_list')   
    else:
        form =  DollstalForm(instance=dolls)
    return render(request, 'edit_dollstal.html', {'form': form})

def dollstal_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Dollstal.objects.filter(
            name__icontains=search_query
        ) | Dollstal.objects.filter(
            price__icontains=search_query
        )  
    else:
        records =  Dollstal.objects.all()

    return render(request, 'dollstal_list.html', {'records': records, 'user': request.user})


def add_paydoll(request):
    if request.method == 'POST':
        form = PaydollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_paydoll')
    else:
        form =  PaydollForm()

    return render(request, 'add_paydoll.html', {'form': form})

 
def paydoll_list(request):
    records = Dollpay.objects.all()
    return render(request, 'paydoll_list.html', {'records': records})


def delete_paydoll(request, pk):
    if request.user.is_authenticated:
        delete_it = Dollpay.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('paydoll_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('paydoll_list')



def edit_paydoll(request, pk):
    paydolls = get_object_or_404(Dollpay, id=pk)
    if request.method == 'POST':
        form = PaydollForm(request.POST, instance=paydolls)
        if form.is_valid():
            form.save()
            return redirect('paydoll_list')  
    else:
        form = PaydollForm(instance=paydolls)
    return render(request, 'edit_paydoll.html', {'form': form})

def paydoll_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        records = Dollpay.objects.filter(
            dollstall__name__icontains=search_query
        ) | Dollpay.objects.filter(
            dollstall__price__icontains=search_query
        ) | Dollpay.objects.filter(
            arrival__first_name__icontains=search_query
        ) | Dollpay.objects.filter(
            arrival__last_name__icontains=search_query
        )
    else:
        records =  Dollpay.objects.all()

    return render(request, 'paydoll_list.html', {'records': records, 'user': request.user})



def products(request):
    return render(request, 'products.html' )



def add_procure(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_procure')
    else:
        form =  ProcurementForm()

    return render(request, 'add_procure.html', {'form': form})

def procure_list(request):
    records = Procurement.objects.all()
    return render(request, 'procure_list.html', {'records': records})


def delete_procure(request, pk):
    if request.user.is_authenticated:
        delete_it = Procurement.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('procure_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('procure_list')



def edit_procure(request, pk):
    procure = get_object_or_404(Procurement, id=pk)
    if request.method == 'POST':
        form = ProcurementForm(request.POST, instance=procure)
        if form.is_valid():
            form.save()
            return redirect('procure_list')  # Redirect to the record list page after editing
    else:
        form = ProcurementForm(instance=procure)
    return render(request, 'edit_procure.html', {'form': form})


def add_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_issue')
    else:
        form =  IssueForm()

    return render(request, 'add_issue.html', {'form': form})

def issue_list(request):
    records = Issue.objects.all()
    return render(request, 'issue_list.html', {'records': records})


def delete_issue(request, pk):
    if request.user.is_authenticated:
        delete_it = Issue.objects.get(id = pk)
        delete_it.delete()
        messages.success(request, 'Record deleted successfuly')
        return redirect('issue_list')
    else:
        messages.success(request, "You must be logged in to delete!")
        return redirect('issue_list')



def edit_issue(request, pk):
    issue = get_object_or_404(Issue, id=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_list')   
    else:
        form = IssueForm(instance=issue)
    return render(request, 'edit_issue.html', {'form': form})