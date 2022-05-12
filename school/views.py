from rest_framework import viewsets
from school.models import Registration, Student, Curse
from serializer import StudentSerializer, CurseSerializer, RegistrationSerializer

# ------------------------ STUDENTS VIEWSET ---------------------------------
class StudentViewSet (viewsets.ModelViewSet):
   """Exibindo todos os alunos e alunas"""
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

# ------------------------ CURSE VIEWSET ---------------------------------
class CurseViewSet (viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
    
# ------------------------ REGISTRATION VIEWSET ---------------------------------    
class RegistrationViewSet (viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
        