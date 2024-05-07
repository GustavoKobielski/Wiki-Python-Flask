from app import app, db
from flask import render_template, url_for, request, redirect

from sqlalchemy import desc

from app.forms import WikiForm, RespostaForm
from app.models import Wiki

@app.route('/')
def homepage():
    dados = Wiki.query.order_by(desc(Wiki.data_envio)).limit(5).all()
    context = {'dados': reversed(dados)}
    return render_template('index.html', context=context)


@app.route('/postar', methods=['GET', 'POST'])
def adicionarPostagem():
    form = WikiForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    return render_template('adicionarPostagem.html',context=context, form=form)


@app.route('/lista')
def listaPagina():
    dados = Wiki.query.all()

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
    dados = Wiki.query.order_by('titulo')

    if pesquisa:
        dados = dados.filter(Wiki.titulo==pesquisa)
    context = {'dados': dados.all()}

    return render_template('listapostagem.html',context=context)

@app.route('/lista/<int:id>', methods=['GET', 'POST'])
def contatoDetail(id):
    form = RespostaForm()
    obj = Wiki.query.get(id)
    
    if form.validate_on_submit():
        form.save(id)
        return redirect(url_for('listaPagina'))
    
    return render_template('contatoDetail.html', id=id, obj=obj, form=form)