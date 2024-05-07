from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from app import db
from app.models import Wiki, Resposta

class WikiForm(FlaskForm):
    nickname= StringField('Nickname',validators=[DataRequired()])
    titulo = StringField('Titulo',validators=[DataRequired()])
    mensagem = StringField('Mensagem',validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        wiki = Wiki (
            nickname = self.nickname.data,
            titulo = self.titulo.data,
            mensagem = self.mensagem.data,
        )

        db.session.add(wiki)
        db.session.commit()

class RespostaForm(FlaskForm):
    nickname= StringField('Nickname',validators=[DataRequired()])
    resposta = StringField("Comentario",validators=[DataRequired()])
    btnSubmitt = SubmitField('Comentar')

    def save(self, wiki_id):
        resposta = Resposta(
            resposta=self.resposta.data,
            nickname = self.nickname.data,
            wiki_id=wiki_id
        )

        db.session.add(resposta)
        db.session.commit()