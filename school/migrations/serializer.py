from rest_framework import serializers
from school.models import Student, Curse, Registration

# ------------------------ STUDENTS SERIALIZER ---------------------------------
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'birth_date']
        

# ------------------------ CURSE SERIALIZER ---------------------------------        
class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = '__all__'
        
# ------------------------ REGISTRATION SERIALIZER ---------------------------------
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = [] # it's a some thing that "fields = '__all__'" but you can put a variable that you don't want to show, like [ 'id' ].

# ------------------------ LIST STUDENT REGISTRATIONS SERIALIZER ---------------------------------
class ListStudentRegistrationSerializer(serializers.ModelSerializer):
    curse = serializers.ReadOnlyField(source='curse.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['curse', 'period']
        
    def get_period(self, obj):
        return obj.get_period_display()
    

# ------------------------- LIST OF STUDENTS ENROLLED IN A CURSE ---------------------------
class ListStudentsEnrolledInACurseSerializer (serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='students.name')
    class Meta:
        model = Registration
        fields = ['student_name']
        
