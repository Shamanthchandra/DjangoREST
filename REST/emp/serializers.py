from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Employee
        fields = ['emp_id', 'firstname', 'lastname', 'designation', 'department', 'age']
        #read_only_fields = ['emp_id']

    #def validate_id(self,value):
     #  qs = Employee.objects.filter(emp_id__exact=value)
      # if qs.exists():
       #   raise serializers.ValidationError("EMP_ID must be unique")
       #return value