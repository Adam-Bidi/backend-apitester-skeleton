from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import pathlib as pl 


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 



if __name__ == '__main__':
    app.run(debug=False)
