from admin import admin_bp
from admin import admin_bp
from flask import render_template, session, redirect


@admin_bp.route('/')
def admin():
    if 'usuario' not in session:
        return redirect('/entrar')
    return render_template('admin.html')