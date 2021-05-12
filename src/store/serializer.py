from rest_framework import serializers
from .models import Company, CompanyAccount, CompanyBank
from .models import Employee, EmployeeBank, EmployeeSalary
from .models import Medicine, MedicalDetail
from .models import Customer, CustomerRequest
from .models import Bill, BillDetail

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = '__all__'
    
    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['company']= CompanySerializer(instance.company).data
        return response


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"

    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['company']= CompanySerializer(instance.company).data
        return response


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
    
    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['company']= CompanySerializer(instance.company).data
        return response


class MedicalMasterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetail
        fields = '__all__'
    
    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['medicine']= MedicineSerializer(instance.medicine).data
        return response

class MedicalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetail
        fields = '__all__'
    


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
    
    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['customer']= CustomerSerializer(instance.customer).data
        return response

class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetail
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = '__all__'

    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['employee']= CompanySerializer(instance.employee).data
        return response

class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'
    
    def to_representation(self,instance):
        response= super().to_representation(instance)
        response['employee']= CompanySerializer(instance.employee).data
        return response
