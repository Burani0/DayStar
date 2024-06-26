from django.urls import path
from django.contrib.auth import views as auth_views
from ddms_app import views 
from ddms_app.views import forgot
from django.contrib import admin
from .import views
from .views import *
from .views import regester
from .views import add_record
from .views import record_list
from .views import delete_record
from .views import edit_record
from .views import add_baby
from .views import baby_list
from .views import delete_baby
from .views import edit_baby
from .views import add_arrival
from .views import arrival_list
from .views import delete_arrival
from .views import edit_arrival
from .views import add_departure
from .views import departure_list
from .views import delete_departure
from .views import edit_departure
from . views import *
from .views import CustomLoginView





aap_name="ddms_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'assets/index.html'), name= 'logout'),
    path('forgot-password/', forgot, name='forgot'),
    path('admin/', admin.site.urls),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('regester/', views.regester, name='regester'),
    path('payments/', views.payments, name='payments'),
    path('add_record/', views.add_record, name='add_record'),
    path('list/', views.record_list, name='record_list'),
    path('delete_record/<str:pk>/', views.delete_record, name='delete_record'),
    path('edit/<int:record_id>/', views.edit_record, name='edit_record'),
    path('add_baby/', views.add_baby, name='add_baby'),
    path('baby_list/', views.baby_list, name='baby_list'),
    path('delete_baby/<int:pk>/', delete_baby, name='delete_baby'),
    path('edit_baby/<int:baby_id>/', views.edit_baby, name='edit_baby'),
    path('add_arrival/', views.add_arrival, name='add_arrival'),
    path('arrival_list/', views.arrival_list, name='arrival_list'),
    path('delete_arrival/<str:pk>/', views.delete_arrival, name='delete_arrival'),
    path('edit_arrival/<int:arrival_id>/', views.edit_arrival, name='edit_arrival'),
    path('add_departure/', views.add_departure, name='add_departure'),
    path('departure_list/', views.departure_list, name='departure_list'),
    path('delete_departure/<str:pk>/', views.delete_departure, name='delete_departure'),
    path('edit_departure/<int:departure_id>/', views.edit_departure, name='edit_departure'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path("add_todo/", views.add_todo, name="add_todo"),
    path("update_todo/<int:pk>/", views.update_todo, name="update_todo"),
    path("delete_todo/<int:pk>/", views.delete_todo, name="delete_todo"),
    path("sitter_on_duty/", views.sitter_on_duty, name="sitter_on_duty"),
    path("duty_list/", views.duty_list, name="duty_list"),
    path('delete_duty/<int:pk>/', views.delete_duty, name='delete_duty'),
    path('edit_duty/<int:pk>/', views.edit_duty, name='edit_duty'),
    path('add_assign/', views.add_assign, name='add_assign'),
    path('edit_assign/<int:pk>/', views.edit_assign, name='edit_assign'),
    path('assign_list/', views.assign_list, name='assign_list'),
    path('delete_assign/<int:pk>/', views.delete_assign, name='delete_assign'),
    path('add_monthly/', views.add_monthly, name='add_monthly'),
    path('delete_monthly/<int:pk>/', views.delete_monthly, name='delete_monthly'),
    path('monthly/', views.monthly_list, name='monthly_list'),
    path('edit_monthly/<int:pk>/', views.edit_monthly, name='edit_monthly'),
    path('add_daily/', views.add_daily, name='add_daily'),
    path('daily_list/' ,views.daily_list, name='daily_list'),
    path('delete_daily/<int:pk>/', views.delete_daily, name='delete_daily'),
    path('edit_daily/<int:pk>/', views.edit_daily, name='edit_daily'),
    path('babies/', views.babies_list, name='babies_list'),
    path('monthlys/', views.monthlys_list, name='monthlys_list'),
    path('dailys/', views.dailys_list, name='dailys_list'),
    path('arrivals/', views.arrivals_list, name='arrivals_list'),
    path('departures/', views.departures_list, name='departures_list'),
    path('dutys/',views.dutys_list, name='dutys_list'),
    
    path('rege/', views.rege_list, name='rege_list'),
    path('give/', views.give_list, name='give_list'),
    path('create/', views.add_sitter_pay, name='add_sitter_pay'),
    path('list_attendance/', views.sitter_pay_list, name='sitter_pay_list'),
    path('delete_sitterpay/<int:pk>/', views.delete_sitterpay, name='delete_sitterpay'),
    path('edit_sitterpay/<int:pk>/', views.edit_sitterpay, name='edit_sitterpay'),
    path('search_pay_sitter/', views.search_pay_sitter, name='search_pay_sitter'),


    path('add_dollstal/', views.add_dollstal, name='add_dollstal'),
    path('dollstal/', views.dollstal_list, name='dollstal_list'),
    path('delete_dollstal/<int:pk>/', views.delete_dollstal, name='delete_dollstal'),
    path('edit_dollstal/<int:pk>/', views.edit_dollstal, name='edit_dollstal'),
    path('dollstal_search/', views.dollstal_search, name='dollstal_search'),


    path('add_paydoll/', views.add_paydoll, name='add_paydoll'),  # URL for adding a Dollpay
    path('list_dollpay/', views.paydoll_list, name='paydoll_list'),  # URL for listing all Dollpay records
    path('delete_paydoll/<int:pk>/', views.delete_paydoll, name='delete_paydoll'),  # URL for deleting a Dollpay
    path('edit_paydoll/<int:pk>/', views.edit_paydoll, name='edit_paydoll'),  # URL for editing a Dollpay
    path('paydoll_search/', views.paydoll_search, name='paydoll_search'),


     
    path('products/', views.products, name='products'),


    path('add_procure/', views.add_procure, name='add_procure'),
    path('procure_list/', views.procure_list, name='procure_list'),
    path('delete_procure/<int:pk>/', views.delete_procure, name='delete_procure'),
    path('edit_procure/<int:pk>/', views.edit_procure, name='edit_procure'),
 
    path('add_issue/', views.add_issue, name='add_issue'),  # Ensure this line is present
    path('issue_list/', views.issue_list, name='issue_list'),
    path('edit_issue/<int:id>/', views.edit_procure, name='edit_issue'),
    path('delete_issue/<int:id>/', views.delete_procure, name='delete_issue'),
 
    

    
    
]
