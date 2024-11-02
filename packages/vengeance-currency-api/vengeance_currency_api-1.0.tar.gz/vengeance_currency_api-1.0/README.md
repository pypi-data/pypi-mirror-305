# Vengeance World Currency API

Welcome to the **Currency API**, a powerful and easy-to-use RESTful API designed to provide comprehensive currency symbols and codes for various countries around the globe. This API is perfect for developers looking to integrate currency information into their applications.

## Features

- **Simple Integration**: Effortlessly integrate currency data into your applications.
- **Comprehensive Coverage**: Access currency information for numerous countries.
- **Lightweight**: Designed to be lightweight and fast, ensuring optimal performance.

## Installation

### Step 1: Clone the Repository

To get started, clone the repository to your local machine:

git clone https://github.com/preetham-1811/currency-api.git
cd currency-api

### Step 2: Install Dependencies

Next, install the required dependencies using pip:

pip install -r requirements.txt

## Usage

To run the API, follow these steps:

1. Import the `CurrencyAPI` class from the package.
2. Create an instance of the API.
3. Call the `run` method to start the server.

```python
from currency_api import CurrencyAPI

api = CurrencyAPI()
api.run()
```

Once the server is running, you can access the API endpoints.

## API Endpoints

### Get Currency Information for a Specific Country

- **Endpoint**: `GET /currency/<country>`
- **Description**: Retrieve detailed currency information (symbol and code) for a specific country.
- **Example**: 
   - Request: `/currency/Albania`
   - Response: `{ "symbol": "Lek", "code": "ALL" }`

### Retrieve a List of All Available Currencies

- **Endpoint**: `GET /currencies`
- **Description**: Get a comprehensive list of all available currencies along with their symbols and codes.
- **Response**:
   - Example Output: 
   ```json
   [
       { "country": "Albania", "symbol": "Lek", "code": "ALL" }
   ]
   ```

## Contributing

We welcome contributions! If you'd like to contribute to the Currency API, please fork the repository and submit a pull request. Your help in improving this API is greatly appreciated!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you have any questions or need support, feel free to open an issue on GitHub or reach out directly.

---

Feel free to adjust any sections or add more details specific to your project! This structure provides clear guidance and encourages engagement with the API.