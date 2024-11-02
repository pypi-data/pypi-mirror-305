# Currency API

A RESTful API that provides currency symbols and codes for various countries.

## Installation

1. Clone the repository:
   git clone https://github.com/preetham-1811/currency-api.git
   cd currency-api

2. Install the required dependencies:
    pip install -r requirements.txt

Usage

To run the API, create an instance of CurrencyAPI and call the run method:

from currency_api import CurrencyAPI

api = CurrencyAPI()
api.run()


API Endpoints
-GET /currency/<country>: Retrieve currency information for a specific country.
-GET /currencies: Retrieve a list of all available currencies.