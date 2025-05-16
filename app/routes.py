from flask import Blueprint, render_template, request, redirect
from .models import db, Relation

main = Blueprint('main', __name__)

@main.route('/insert', methods=['GET'])
def insert_form():
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

@main.route('/delete/<int:interaction_id>', methods=['POST'])
def delete(interaction_id):
    relation = Relation.query.get_or_404(interaction_id)
    db.session.delete(relation)
    db.session.commit()
    return redirect('/relations')

@main.route('/edit/<int:interaction_id>', methods=['GET', 'POST'])
def edit(interaction_id):
    relation = Relation.query.get_or_404(interaction_id)

    if request.method == 'POST':
        relation.host_species_name = request.form['host']
        relation.parasite_species_name = request.form['parasite']
        relation.citation_key = request.form['citation_key']
        relation.L_parasitic_mode = request.form['L_parasitic_mode']
        relation.L_host_organ = request.form['L_host_organ']
        relation.A_parasitic_mode = request.form['A_parasitic_mode']
        relation.A_host_organ = request.form['A_host_organ']
        relation.credibility = request.form['credibility']
        relation.comment = request.form['comment']
        relation.entry_source = request.form['entry_source']
        relation.entry_by = request.form['entry_by']

        db.session.commit()
        return redirect('/relations')

    return render_template('edit_relation.html', relation=relation)

@main.route('/', methods=['GET', 'POST'])
def search():
    results = None

    if request.method == 'POST':
        host_query = request.form.get('host')
        parasite_query = request.form.get('parasite')

        query = Relation.query
        if host_query:
            query = query.filter(Relation.host_species_name.ilike(f"%{host_query}%"))
        if parasite_query:
            query = query.filter(Relation.parasite_species_name.ilike(f"%{parasite_query}%"))

        results = query.all()

    return render_template('search.html', results=results)

@main.route('/interaction/<int:interaction_id>')
def detail(interaction_id):
    relation = Relation.query.get_or_404(interaction_id)
    return render_template('detail.html', relation=relation)

