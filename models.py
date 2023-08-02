"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    app.app_context().push()
    
class Cupcake(db.Model):
    """Cupcake model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String(50),
                     nullable=False)
    size = db.Column(db.String(50),
                     nullable=False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.String(255), 
                     nullable=False, 
                     default = "https://tinyurl.com/demo-cupcake")
                     
def serialize_cupcake(cupcake):
    return {
        "id" : cupcake.id,
        "flavor" : cupcake.flavor,
        "size" : cupcake.size,
        "rating" : cupcake.rating,
        "image" : cupcake.image
        }
        
def serialize_cupcake_list(cupcakes):
    cupcake_list = []
    for cupcake in cupcakes:
        cupcake_list.append(serialize_cupcake(cupcake))
    return cupcake_list