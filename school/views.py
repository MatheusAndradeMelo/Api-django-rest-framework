from rest_framework import viewsets
from school.models import Student, Curse
from serializer import StudentSerializer, CurseSerializer

class StudentViewSet (viewsets.ModelViewSet):
   """Exibindo todos os alunos e alunas"""
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   
class CurseViewSet (viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
        