from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    license_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.id}'
    


class Medicine(models.Model):
    name = models.CharField(max_length=50)
    medical_type = models.CharField(max_length=50)
    buy_price = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    sell_price =models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    C_GST = models.CharField(max_length=50)
    S_GST = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=50)
    shelf_no = models.CharField(max_length=50)
    exp_date = models.DateField()
    mfg_date = models.DateField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    in_stock_total = models.IntegerField(default=0)
    qty_in_strip = models.IntegerField(default=0)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

    def __str__(self):
        return self.name
    

class MedicalDetail(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    salt_name= models.CharField(max_length=50)
    salt_qty = models.IntegerField(default=0)
    salt_qty_type = models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add= True)
    description = models.CharField(max_length=50)
    objects = models.Manager()




class Employee(models.Model):
    name = models.CharField(max_length=50)
    employee =models.CharField(max_length=50)
    joining_date = models.DateField()
    phone = models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()



class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

class Bill(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

class BillDetail(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medical = models.ForeignKey(Medicine,on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    added_on = models.DateField(auto_now_add= True)
    objects = models.Manager()

class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    medicine_details = models.CharField(max_length=50)
    status = models.BooleanField(default=0)
    added_on = models.DateField()
    objects = models.Manager()

class CompanyAccount(models.Model):
    Transaction_Type = [
        (0,'DEBIT'),
        (1,'CREDIT')
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.PositiveIntegerField(choices=Transaction_Type, default=0)
    transaction_amount = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    transaction_date = models.DateField()
    payment_mode = models.CharField(max_length=20)
    objects = models.Manager()

class CompanyBank(models.Model):
    bank_account_no = models.CharField(max_length=20)
    IFSC= models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    objects = models.Manager()

class EmployeeBank(models.Model):
    bank_account_no = models.CharField(max_length=20)
    IFSC= models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    objects = models.Manager()