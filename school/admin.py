from django.contrib import admin
from school.models import Student, Curse, Registration

# ------------------------ STUDENTS ---------------------------------
class Students(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'rg',
        'cpf',
        'birth_date'
    )
    list_display_links = ('id', 'name')
    search_fields = ('name')
    list_per_page = 20
    
admin.site.register(Student, Students)

# ------------------------ CURSES ---------------------------------

class Curses(admin.ModelAdmin):
    list_display = (
        'id',
        'cod_curse',
        'description',
    )
    list_display_links = ('id', 'cod_curse')
    search_fields = ('cod_curse')
    
admin.site.register(Curse, Curses)

# ------------------------ REGISTRATIONS ---------------------------------

class Registrations(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'curse',
        'period',
    )
    list_display_links = ('id')
    
admin.site.register(Registration, Registrations)
        
