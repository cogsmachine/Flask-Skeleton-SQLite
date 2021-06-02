from flask import Blueprint, render_template, request, redirect, url_for, flash

from application import db
from application.models import Message

main_bp = Blueprint(
    'main', __name__,
    template_folder='templates',
)

@main_bp.route('/')
def home():
    return redirect(url_for('main.contact'))

@main_bp.route('/contact/')
def contact():
    return render_template('contact.html')


@main_bp.route('/contact/', methods=['POST'])
def contact_post():
    
    name = request.form.get('name')
    message = request.form.get('message')
    
    if len(name)==0 or len(message)==0:
        flash('Name or Message must be not be empty')
        
        return redirect(url_for('main.contact'))
    
    new_message = Message(name = name, message = message)
    
    db.session.add(new_message)
    db.session.commit()
    
    return redirect(url_for('main.show_messages'))

@main_bp.route('/messages/')
def show_messages():
    rows = Message.query.all()
    return render_template('messages.html',
                            rows=rows)

