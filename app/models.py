from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Relation(db.Model):
    __tablename__ = 'relations'

    #These lines define Python-level relationships in your SQLAlchemy models.
    #They don’t affect the database schema directly
    #they create helper properties for navigating your data
    #they enable me to access host and parasite tables through this table

    host = db.relationship('Host', backref='relations')
    parasite = db.relationship('Parasite', backref='relations')

    #database schema:
    interaction_id = db.Column(db.Integer, primary_key=True)

    host_id = db.Column(db.Integer, db.ForeignKey('hosts.host_ID'), nullable=False) # The foreign key ensures that each relation must reference an existing host and parasite.
    parasite_id = db.Column(db.Integer, db.ForeignKey('parasites.parasite_ID'), nullable=False)

    # Ich brauche keine host oder parasite names in dieser tabelle. wegen der foreign keys kann ich
    # automatisch auf diese spalten in den anderen Tabellen zugreifen

    #host_name = db.Column(db.String(100))
    #parasite_name = db.Column(db.String(100))
    #host_species_name = db.Column(db.String(100))
    #parasite_species_name = db.Column(db.String(100))
    citation_key = db.Column(db.String(200))
    L_parasitic_mode = db.Column(db.String(100))
    L_host_organ = db.Column(db.String(100))
    A_parasitic_mode = db.Column(db.String(100))
    A_host_organ = db.Column(db.String(100))
    credibility = db.Column(db.String(100))
    comment = db.Column(db.Text)
    entry_source = db.Column(db.String(100))
    entry_by = db.Column(db.String(100))



class Parasite(db.Model):
    __tablename__ = 'parasites'

    parasite_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parasite_name = db.Column(db.String(100))
    parasite_species_name = db.Column(db.String(100), nullable=False)
    dwc_genus = db.Column(db.String(100), nullable=False)
    dwc_subgenus = db.Column(db.String(100))
    dwc_specificEpithet = db.Column(db.String(100), nullable=False)
    dwc_infraspecificEpithet = db.Column(db.String(100))
    dwc_scientificNameAuthorship = db.Column(db.String(200))

    dwc_tribe = db.Column(db.String(100), nullable=False)
    supertribe = db.Column(db.String(100))
    dwc_subfamily = db.Column(db.String(100), nullable=False)
    dwc_family = db.Column(db.String(100), nullable=False)
    dwc_superfamily = db.Column(db.String(100), nullable=False)
    dwc_order = db.Column(db.String(100), nullable=False)

    entry_source = db.Column(db.String(200))
    entry_by = db.Column(db.String(100))


class Host(db.Model):
    __tablename__ = 'hosts'

    host_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)

    host_name = db.Column(db.String(100))
    host_species_name = db.Column(db.String(100), nullable=False)
    dwc_genus = db.Column(db.String(100), nullable=False)
    dwc_subgenus = db.Column(db.String(100))
    dwc_specificEpithet = db.Column(db.String(100))
    dwc_infraspecificEpithet = db.Column(db.String(100))
    dwc_scientificNameAuthorship = db.Column(db.String(200))

    dwc_tribe = db.Column(db.String(100), nullable=False)
    supertribe = db.Column(db.String(100))
    dwc_subfamily = db.Column(db.String(100), nullable=False)
    dwc_family = db.Column(db.String(100), nullable=False)
    dwc_superfamily = db.Column(db.String(100), nullable=False)
    dwc_order = db.Column(db.String(100), nullable=False)

    dwc_vernacularName = db.Column(db.String(200))
    entry_source = db.Column(db.String(200))
    entry_by = db.Column(db.String(100))


