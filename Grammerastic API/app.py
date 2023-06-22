# 1. Library imports
from flask import Flask, jsonify, request
import pickle
import numpy as np
import pandas as pd
from happytransformer import HappyTextToText, TTSettings
from flask_cors import CORS, cross_origin

# 2. Create the app object
app = Flask(__name__)
happy_tt = pickle.load(open("happy_tt.pkl","rb"))
cors = CORS(app, origins=["http://127.0.0.1:5173/", "https://frontend-grammarastic.vercel.app/"])

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.route('/correct', methods = ['POST'] )
@cross_origin()
def correctOutput():
    request_data = request.get_json()
    data = request_data['message']
    args = TTSettings(num_beams=5, min_length=1)
    correctedOutput = happy_tt.generate_text(f'{data}', args=args)
    return jsonify( { 'message': correctedOutput.text } )

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    app.run()
    
#uvicorn app:app --reload