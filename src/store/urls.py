from django.urls import path, include

from rest_framework import routers
from .views import CompanyViewSet, CompanyBankViewSet, CompanyAccountSerializer
from .views import CustomerViewSet, CompanyAccountViewSet
from .views import MedicineDetailViewSet, MedicineViewSet
from .views import EmployeeViewSet,EmployeeBankViewSet, EmployeeSalaryViewSet
from .views import CustomerViewSet, CustomerRequestViewSet
from .views import BillDetailViewSet, BillViewSet


route= routers.DefaultRouter()
route.register("company",CompanyViewSet, basename="company")
route.register("company-bank",CompanyBankViewSet, basename="company-bank")
route.register("customer", CustomerViewSet, basename="customer")
route.register("medicine", MedicineViewSet, basename="medicine")
route.register("employee", EmployeeViewSet, basename="employee")
route.register("customer", CustomerViewSet, basename="customer")
route.register("bill",BillViewSet, basename="bill")


urlpatterns = [

]+ route.urls