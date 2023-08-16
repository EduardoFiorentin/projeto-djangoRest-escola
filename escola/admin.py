from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
# Register your models here.

# Aqui serão registrados os models que devem ser mostrados na página de admin do django

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento') # Quais dados são mostrados 
    list_display_links = ('id', 'nome') # campos que podem ser alterados
    search_fields = ('nome',) # o que pode ser pesquisado 
    list_per_page = 20 # quantos itens aparecem por página 

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)