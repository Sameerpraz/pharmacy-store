from django.contrib import admin
from .models import Employee, EmployeeBank, EmployeeSalary
from .models import Company, CompanyAccount, CompanyBank
from .models import Medicine, MedicalDetail
from .models import Customer, CustomerRequest
from .models import Bill, BillDetail
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class EmployeeBankAdmin(admin.ModelAdmin):
    list_display = ['id','bank_account_no','IFSC','employee']

class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ['id','employee','salary_date','salary_amount','added_on']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','license_no','address','contact_no','email']
    
class CompanyBankAdmin(admin.ModelAdmin):
    list_display = ['id','bank_account_no','IFSC','company']

class CompanyAccountAdmin(admin.ModelAdmin):
    list_display = ['id','company','transaction_type','transaction_amount','payment_mode']

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'medical_type']

class MedicineDetailAdmin(admin.ModelAdmin):
    list_display = ['id','medicine', 'salt_name','salt_qty', 'salt_qty_type']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeBank,EmployeeBankAdmin)
admin.site.register(EmployeeSalary,EmployeeSalaryAdmin)

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyBank,CompanyBankAdmin)
admin.site.register(CompanyAccount,CompanyAccountAdmin)

admin.site.register(Medicine,MedicineAdmin)
admin.site.register(MedicalDetail,MedicineDetailAdmin)

admin.site.register(Customer)
admin.site.register(CustomerRequest)

admin.site.register(Bill)
admin.site.register(BillDetail)