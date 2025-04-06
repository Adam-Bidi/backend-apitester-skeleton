import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

# Vérifier si le serveur est actif
@app.route('/api/alive', methods=['GET'])
def alive():
    return jsonify({"message": "Alive"}), 200

# Liste de toutes les associations
@app.route('/api/associations', methods=['GET'])
def get_associations():
    associations = list(associations_df['id']) # On transforme la Series en liste
    return jsonify(associations), 200

# Détails d'une association
@app.route('/api/association/<int:id>', methods=['GET'])
def get_association_details(id):
    association = associations_df[associations_df['id'] == id] # On applique un masque pour filtrer les associations
    if association.empty:
        return jsonify({"error": "Association not found"}), 404
    return jsonify(dict(association.iloc[0])), 200 # Même si association est un DataFrame, on le transforme en Series avec iloc[0] puis en dictionnaire

# Liste de tous les événements
@app.route('/api/evenements', methods=['GET'])
def get_evenements():
    evenements = list(evenements_df['id'])
    return jsonify(evenements), 200

# Détails d'un événement
@app.route('/api/evenement/<int:id>', methods=['GET'])
def get_evenement_details(id):
    evenement = evenements_df[evenements_df['id'] == id]
    if evenement.empty:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(dict(evenement.iloc[0])), 200

# Liste des événements d'une association
@app.route('/api/association/<int:id>/evenements', methods=['GET'])
def get_association_evenements(id):
    evenements = evenements_df[evenements_df['association_id'] == id]
    return jsonify(evenements.to_dict(orient='records')), 200 # to_dict(orient='records') permet de retourner une liste vide si evenements est vide

# Liste des associations par type
@app.route('/api/associations/type/<type>', methods=['GET'])
def get_associations_by_type(type):
    filtered_associations = associations_df[associations_df['type'].str.lower() == type.lower()]
    return jsonify(filtered_associations.to_dict(orient='records')), 200


if __name__ == '__main__':
    app.run(debug=False)
