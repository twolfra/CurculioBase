from flask import Blueprint, render_template, request, redirect
from .models import Relation, Parasite, Host, db
from sqlalchemy.orm import joinedload


def na_if_blank(value):
    return value.strip() if value and value.strip() else "n.a."


main = Blueprint('main', __name__)

@main.route('/insert', methods=['GET', 'POST'])
def insert_form():
    hosts = Host.query.order_by(Host.dwc_genus).all()
    parasites = Parasite.query.order_by(Parasite.dwc_genus).all()

    if request.method == 'POST':
        relation = Relation(
            host_id=request.form.get('host_ID'),       # corrected key
            parasite_id=request.form.get('parasite_ID'),  # corrected key
            citation_key=na_if_blank(request.form.get('citation_key')),
            L_parasitic_mode=na_if_blank(request.form.get('L_parasitic_mode')),
            L_host_organ=na_if_blank(request.form.get('L_host_organ')),
            A_parasitic_mode=na_if_blank(request.form.get('A_parasitic_mode')),
            A_host_organ=na_if_blank(request.form.get('A_host_organ')),
            credibility=na_if_blank(request.form.get('credibility')),
            comment=na_if_blank(request.form.get('comment')),
            entry_source=na_if_blank(request.form.get('entry_source')),
            entry_by=na_if_blank(request.form.get('entry_by')),
        )
        db.session.add(relation)
        db.session.commit()
        return redirect('/relations')

    return render_template('insert_relation.html', hosts=hosts, parasites=parasites)


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

    """gives search output"""

    results = None

    if request.method == 'POST':
        host_name = request.form.get('host_name')
        parasite_name = request.form.get('parasite_name')

        query = Relation.query.join(Relation.host).join(Relation.parasite)

        if host_name:
            query = query.filter(Host.host_name.ilike(f"%{host_name}%"))
        if parasite_name:
            query = query.filter(Parasite.parasite_name.ilike(f"%{parasite_name}%"))

        results = query.options(
            db.joinedload(Relation.host),
            db.joinedload(Relation.parasite)
        ).all()


    return render_template('search.html', results=results)


@main.route('/interaction/<int:interaction_id>')
def detail(interaction_id):
    relation = Relation.query.get_or_404(interaction_id)
    return render_template('detail.html', relation=relation)

@main.route('/add-parasite', methods=['GET', 'POST'])
def add_parasite():

    if request.method == 'POST':
        
        parasite = Parasite(
            parasite_name = request.form.get('parasite_name'),
            parasite_species_name=na_if_blank(request.form.get('species_name')),
            dwc_genus=na_if_blank("dwc_genus"),
            dwc_subgenus=na_if_blank(request.form.get('dwc_subgenus')),
            dwc_specificEpithet=na_if_blank(request.form.get('dwc_specificEpithet')),
            dwc_infraspecificEpithet=na_if_blank(request.form.get('dwc_infraspecificEpithet')),
            dwc_scientificNameAuthorship=na_if_blank(request.form.get('dwc_scientificNameAuthorship')),
            dwc_tribe=na_if_blank(request.form.get('dwc_tribe')),
            supertribe=na_if_blank(request.form.get('supertribe')),
            dwc_subfamily=na_if_blank(request.form.get('dwc_subfamily')),
            dwc_family=na_if_blank(request.form.get('dwc_family')),
            dwc_superfamily=na_if_blank(request.form.get('dwc_superfamily')),
            dwc_order=na_if_blank(request.form.get('dwc_order')),
            entry_source=na_if_blank(request.form.get('entry_source')),
            entry_by=na_if_blank(request.form.get('entry_by')),
        )
        db.session.add(parasite)
        db.session.commit()
        return redirect('/add-parasite')

    return render_template('add_parasite.html')


@main.route('/add-host', methods=['GET', 'POST'])
def add_host():

    if request.method == 'POST':

        host = Host(
            host_name = request.form.get('host_name'),
            host_species_name = request.form.get('species_name'),
            dwc_genus=request.form.get('dwc_genus'),
            dwc_subgenus=na_if_blank(request.form.get('dwc_subgenus')),
            dwc_specificEpithet=na_if_blank(request.form.get('dwc_specificEpithet')),
            dwc_infraspecificEpithet=na_if_blank(request.form.get('dwc_infraspecificEpithet')),
            dwc_scientificNameAuthorship=na_if_blank(request.form.get('dwc_scientificNameAuthorship')),
            dwc_tribe=na_if_blank(request.form.get('dwc_tribe')),
            supertribe=na_if_blank(request.form.get('supertribe')),
            dwc_subfamily=na_if_blank(request.form.get('dwc_subfamily')),
            dwc_family=na_if_blank(request.form.get('dwc_family')),
            dwc_superfamily=na_if_blank(request.form.get('dwc_superfamily')),
            dwc_order=na_if_blank(request.form.get('dwc_order')),
            dwc_vernacularName=na_if_blank(request.form.get('dwc_vernacularName')),
            entry_source=na_if_blank(request.form.get('entry_source')),
            entry_by=na_if_blank(request.form.get('entry_by')),
        )
        db.session.add(host)
        db.session.commit()
        return redirect('/add-host')

    return render_template('add_host.html')



@main.route('/parasites')
def list_parasites():
    parasites = Parasite.query.all()
    return render_template('list_parasites.html', parasites=parasites)


@main.route('/hosts')
def list_hosts():
    hosts = Host.query.order_by(Host.dwc_genus).all()
    return render_template('list_hosts.html', hosts=hosts)





