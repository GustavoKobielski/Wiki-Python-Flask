from app import db
from datetime import datetime

class Wiki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now())
    nickname = db.Column(db.String)
    titulo = db.Column(db.String)
    mensagem = db.Column(db.String)
    curtidas = db.Column(db.Integer, default=0)
    
    respostas = db.relationship("Resposta", back_populates="wiki")

class Resposta(db.Model):
    id_resposta = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    resposta = db.Column(db.String)
    
    wiki_id = db.Column(db.Integer, db.ForeignKey('wiki.id'))
    wiki = db.relationship("Wiki", back_populates="respostas", foreign_keys=[wiki_id], remote_side=[Wiki.id])




