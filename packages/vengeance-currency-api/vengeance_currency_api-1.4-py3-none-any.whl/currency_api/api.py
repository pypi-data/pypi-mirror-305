# currency_api/api.py

from flask import Flask, jsonify
import json
import os

class CurrencyAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.load_currency_data()
        self.setup_routes()

    def load_currency_data(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, 'currencies.json')
        
        with open(json_path, 'r', encoding='utf-8') as file:
            self.currency_data = json.load(file)
        self.currency_dict = {item["Country"]: {"symbol": item["Symbol"], "code": item["Code"]} for item in self.currency_data}


    def setup_routes(self):
        @self.app.route('/currency/<country>', methods=['GET'])
        def get_currency(country):
            currency = self.currency_dict.get(country)
            if currency:
                return jsonify({country: currency}), 200
            else:
                return jsonify({"error": "Country not found"}), 404

        @self.app.route('/currencies', methods=['GET'])
        def get_all_currencies():
            return jsonify(self.currency_dict), 200

    def run(self, **kwargs):
        self.app.run(**kwargs)
