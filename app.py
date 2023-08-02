"""Flask app for Cupcakes"""

from flask import Flask,render_template, redirect, flash, session, request, jsonify
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickenz"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route("/")
def start():
    """Render landing page"""  
    return render_template("start.html",
        title = "Cupcakes",
        header = "Cupcakes")
        
@app.route("/api/cupcakes", methods = ['GET'])
def all_cupcakes():
    return {"cupcakes":serialize_cupcake_list(Cupcake.query.all())}

@app.route("/api/cupcakes/<cupcake_id>", methods = ['GET'])
def one_cupcake(cupcake_id):
    return {"cupcake":serialize_cupcake(Cupcake.query.get_or_404(cupcake_id))}
        
@app.route("/api/cupcakes", methods = ['POST'])
def add_cupcake():
    new_cupcake = Cupcake(flavor = request.json["flavor"],
                          size = request.json["size"],
                          rating = request.json["rating"],
                          image = request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    return {"cupcake":serialize_cupcake(new_cupcake)}, 201

@app.route("/api/cupcakes/<cupcake_id>", methods = ['PATCH'])
def patch_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]
    cupcake.image = request.json["image"]
    
    db.session.commit()
    return {"cupcake":serialize_cupcake(cupcake)}

@app.route("/api/cupcakes/<cupcake_id>", methods = ['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return {"message": "Deleted"}