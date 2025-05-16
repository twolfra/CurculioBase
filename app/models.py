from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Relation(db.Model):
    interaction_id = db.Column(db.Integer, primary_key=True)
    host_species_name = db.Column(db.String(100), nullable=False)
    parasite_species_name = db.Column(db.String(100), nullable=False)

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


