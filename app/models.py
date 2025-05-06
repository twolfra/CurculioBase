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

