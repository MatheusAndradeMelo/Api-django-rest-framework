from ast import Expression
from rest_framework import viewsets, generics
from school.models import Registration, Student, Curse
from serializer import StudentSerializer, CurseSerializer, RegistrationSerializer, ListStudentRegistrationSerializer, ListStudentsEnrolledInACurseSerializer
import serializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# ------------------------ STUDENTS VIEWSET ---------------------------------
class StudentViewSet (viewsets.ModelViewSet):
   """Exibindo todos os alunos e alunas"""
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated]

# ------------------------ CURSE VIEWSET ---------------------------------
class CurseViewSet (viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curse.objects.all()
    serializer_class = CurseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
# ------------------------ REGISTRATION VIEWSET ---------------------------------    
class RegistrationViewSet (viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
# ------------------------ LIST STUDENT REGISTRATIONS VIEWSET ---------------------------------
class ListStudentRegistrationsViewSet (generics.ListAPIView):
        """Listando as matriculas de um aluno ou aluna"""
        def get_queryset(self):
            queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
            return queryset
        serializer_class = ListStudentRegistrationSerializer
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]
        authentication_classes = [BasicAuthentication]
        permission_classes = [IsAuthenticated]
        
# ------------------------- LIST OF STUDENTS ENROLLED IN A CURSE VIEWSET ---------------------------
class ListStudentsEnrolledInACurseViewSet (generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Registration.objects.filter(curse_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsEnrolledInACurseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
