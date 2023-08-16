from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField() 

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEL = (
        ('B', "Básico"),
        ('I', "Intermediário"),
        ('A', "Avançado"),
    )
    
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
        # black = False - Precisa ter um valor (não pode ser vazio)
        # null = False - não pode ser nulo .
        # default="B" - valor padrão = B

    def __str__(self):
        return self.descricao


class Matricula(models.Model): 
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', "Noturno")
    )

    # criar chave estrangeira
    # caso o aluno seja deletado, a matricula será também
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')