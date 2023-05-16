from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms import BooleanField
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user



class FormCriarConta(FlaskForm):
    nome = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Cadastre seu E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Cadastre sua Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_criar_conta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')

class FormLogin(FlaskForm):
    email = StringField('Seu E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Sua Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados')
    botao_login = SubmitField('Fazer Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('Seu E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])

    curso_excel = BooleanField('Excel')
    curso_vba = BooleanField('VBA')
    curso_powerbi = BooleanField('Power BI ')
    curso_sql = BooleanField('SQL')
    curso_python = BooleanField('Python')
    curso_powerpoint = BooleanField('Power Point ')
    curso_ppt = BooleanField('JavaScript')


    botao_editarperfil = SubmitField('Confirmar edição')
    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este E-mail')