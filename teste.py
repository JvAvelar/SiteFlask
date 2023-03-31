from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario
from comunidadeimpressionadora import bcrypt

#with app.app_context():
    #cria um novo banco de dados com as informações

    #database.drop_all()
    #database.create_all()

   #  usuario1 = Usuario(username='Vitor', email='jv@gmail.com', senha='123456')
   #  usuario2 = Usuario(username='Manu', email='manu@hotmail.com', senha='654321')
   #  usuario3 = Usuario(username='Laura', email='laura@hotmail.com', senha='748596')
   #
   # # armazena as informações no banco de dados
   #
   #  database.session.add(usuario1)
   #  database.session.add(usuario2)
   #  database.session.add(usuario3)
   #
   # # salva todas informações no banco de dados
   #  database.session.commit()


#with app.app_context():

 #   usuario = Usuario.query.filter_by(id=2).first()
  #  print(usuario.senha)
    #senha = '654321'
   # print(bcrypt.check_password_hash(usuario.senha, senha))


    # meus_usuarios = Usuario.query.all()
    # meus_usuarios = Usuario.query.first()
    # usuario2 = Usuario.query.filter_by(id=2).first()
    #
    #
    # print(meus_usuarios)
#
#     primeiro_usuario = meus_usuarios[0] #pega o primeiro usuario da lista no banco de dados
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.username)


