from flask import Blueprint, render_template, request
from .models import db, Relation

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('insert_relation.html')

@main.route('/submit', methods=['POST'])
def submit():
    data = {
        'host_species_name': request.form.get('host'),
        'parasite_species_name': request.form.get('parasite'),
        'citation_key': request.form.get('citation_key'),
        'L_parasitic_mode': request.form.get('L_parasitic_mode'),
        'L_host_organ': request.form.get('L_host_organ'),
        'A_parasitic_mode': request.form.get('A_parasitic_mode'),
        'A_host_organ': request.form.get('A_host_organ'),
        'credibility': request.form.get('credibility'),
        'comment': request.form.get('comment'),
        'entry_source': request.form.get('entry_source'),
        'entry_by': request.form.get('entry_by'),
    }

    new_entry = Relation(**data)
    db.session.add(new_entry)
    db.session.commit()

    return "Entry saved successfully!"

@main.route('/relations')
def relations():
    all_relations = Relation.query.all()
    return render_template('relations.html', relations=all_relations)
