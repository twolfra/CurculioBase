from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('insert_relation.html')

@main.route('/submit', methods=['POST'])
def submit():
    host = request.form.get('host')
    parasite = request.form.get('parasite')
    # Here you'd insert into the database (we'll add this in a later step)
    return f"Received: Host = {host}, Parasite = {parasite}"
