from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curso
        fields =  '__all__' # usar todos os campos disponíveis no modelo 

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Matricula
        exclude = [] # substitui o fields, colocando apenas o que não é pra comstrar na lista 


# listar todas matriculas dos alunos 
class ListaMatriculAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    # Mostrar o nome do aluno ao invés do id
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
