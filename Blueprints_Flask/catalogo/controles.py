from catalogo import catalogo_bp
from catalogo.dados import listar_cursos_ativos, obter_curso
from flask import render_template, request, session, redirect



@catalogo_bp.route('/')
def index():
    return render_template(
        'index.html',
        cursos=listar_cursos_ativos()
    )

@catalogo_bp.route('/sair')
def sair():
    session.clear()
    return redirect('/')
    

@catalogo_bp.route('/curso/<slug>')
def curso(slug):
    return render_template(
        'curso.html',
        curso=obter_curso(slug)
    )

@catalogo_bp.route('/entrar', methods=['GET', 'POST'])
def login():
    erros =[]
    if request.method == "POST":
        form = request.form
        usuario = form.get('usuario')
        senha = form.get('senha')
        if usuario == 'admin' and senha == 'teste':
            session['usuario'] = 'Adiministrador'
            return redirect('/admin')
            
        else:
            erros.append('Usuario e/ ou senha incorretos')

            
    return render_template('entrar.html' , erros = erros)