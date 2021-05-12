from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializer import CompanySerializer, CompanyBankSerializer, CompanyAccountSerializer
from .serializer import EmployeeSerializer,EmployeeBankSerializer, EmployeeSalarySerializer
from .serializer import MedicineSerializer, MedicalDetailSerializer
from .serializer import CustomerSerializer, CustomerRequestSerializer
from .serializer import BillSerializer, BillDetailSerializer
from .models import Company, CompanyBank, CompanyAccount
from .models import Employee, EmployeeBank, EmployeeSalary
from .models import Medicine, MedicalDetail
from .models import Customer, CustomerRequest
from .models import Bill, BillDetail


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 

from rest_framework import generics

# Create your views here.
class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = CompanySerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=Company.objects.all()
            company=get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class=CompanySerializer
    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name=name)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        company_bank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(company_bank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)
    
    def create(self,request):
        try:
            serializer = CompanyBankSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def retrieve(self,request, pk=None):
        queryset= CompanyBank.objects.all()
        company_bank= get_object_or_404(queryset,pk=pk)
        serializer = CompanyBankSerializer(company_bank)
        return Response(serializer.data)


    def update(self,request, pk=None):
        queryset= CompanyBank.objects.all()
        company_bank= get_object_or_404(queryset,pk=pk)
        serializer = CompanyBankSerializer(company_bank, data=request.data, context={"request":request})
        serializer.is_valid()
        serializer.save()
        dict_response = {"error": False, "message": "success", "data": serializer.data}
        
        return Response(dict_response)

class CompanyAccountViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        queryset = CompanyAccount.objects.all()
        serializer = CompanyAccountSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)
    
    def create(self,request):
        try:
            serializer = CompanyAccount(data=request.data,context={"request":request})
            serializer.is_valid(rais_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def retrieve(self,request, pk=None):
        queryset= CompanyAccount.objects.all()
        company_bank= get_object_or_404(queryset,pk=pk)
        serializer = CompanyBankSerializer(company_bank)
        dict_response = {"error": False, "message": "success", "data": serializer.data}
        return Response(dict_response)

    def update(self,request, pk=None):
        queryset= CompanyAccount.objects.all()
        company_account= get_object_or_404(queryset,pk=pk)
        serializer = CompanyAccountSerializer(company_account, data=request.data, context={"request":request})
        serializer.is_valid()
        serializer.save()
        dict_response = {"error": False, "message": "success", "data": serializer.data}
        
        return Response(dict_response)



class MedicineViewSet(viewsets.ViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Medicine.objects.all()
        serializer = MedicineSerializer(queryset, many=True, context={"request": request})

        medicine_data =serializer.data
        newmedicinelist=[]
# adding extra key for medicine details in medicine
        for medicine in medicine_data:
            medicine_details= MedicalDetail.objects.filter(medicine=medicine['id'])
            medicine_datails_serializers=MedicalDetailSerializer(medicine_details,many=True)
            medicine['medicine_details']=medicine_datails_serializers.data
            newmedicinelist.append(medicine)




        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = MedicineSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def retrieve(self,request, pk=None):
        queryset= Medicine.objects.all()
        medicine= get_object_or_404(queryset,pk=pk)
        serializer = MedicineSerializer(medicine)
        serializer_data =serializer.data
        medicine_details= MedicalDetail.objects.filter(medicine=serializer_data["id"])
        medicine_details_serializers=MedicalDetailSerializer(medicine_details,many=True)
        serializer_data["medicine_details"]=medicine_details_serializers.data
        dict_response = {"error": False, "message": "success", "data": serializer_data}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Medicine.objects.all()
            medicine=get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(medicine, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
class MedicineDetailViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = MedicineDetail.objects.all()
        serializer = MedicineDetailSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = MedicineDetailSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    
    def update(self,request,pk=None):
        try:
            queryset=MedicineDetail.objects.all()
            medicine_detail=get_object_or_404(queryset, pk=pk)
            serializer = MedicineDetailSerializer(medicine_detail, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
class EmployeeViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = EmployeeSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=Employee.objects.all()
            employee=get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    

class EmployeeBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = EmployeeBank.objects.all()
        serializer = EmployeeBankSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = EmployeeBankSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=EmployeeBank.objects.all()
            employee_bank=get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializer(employee_bank, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)

class EmployeeSalaryViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = EmployeeSalary.objects.all()
        serializer = EmployeeSalarySerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = EmployeeSalarySerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=EmployeeSalary.objects.all()
            employee_salary=get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializer(employee_salary, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)

class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = CustomerSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=Customer.objects.all()
            customer=get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(customer, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)

class CustomerRequestViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = CustomerRequest.objects.all()
        serializer = CustomerRequestSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = CustomerRequestSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=EmployeeSalary.objects.all()
            customer_request=get_object_or_404(queryset, pk=pk)
            serializer = CustomerRequestSerializer(customer_request, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)

class BillViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = Bill.objects.all()
        serializer = BillSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = BillSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=Bill.objects.all()
            bill=get_object_or_404(queryset, pk=pk)
            serializer = BillSerializer(bill, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
        

class BillDetailViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = BillDetail.objects.all()
        serializer = BillDetailSerializer(queryset, many=True, context={"request": request})
        response_dict = {"error": False, "message": "success", "data": serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer = BillDetailSerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
    
    def update(self,request,pk=None):
        try:
            queryset=BillDetail.objects.all()
            bill_detail=get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSalarySerializer(bill_detail, data=request.data, context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "success", "data": serializer.data}
        except:
            dict_response = {"error": True, "message": "error occurs"}
        return Response(dict_response)
        


company_list = CompanyViewSet.as_view({"get": "list"})
company_update = CompanyViewSet.as_view({"put": "update"})


