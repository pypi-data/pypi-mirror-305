from flask import Flask, jsonify

class CurrencyAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.currency_dict = self.load_currency_data()

    def load_currency_data(self):
        # Hardcoded currency data
        return [
            {
            "Country": "Albania",
            "Symbol": "Lek",
            "Code": "ALL"
            },
            {
            "Country": "Armenia",
            "Symbol": "Դ",
            "Code": "AMD"
            },
            {
            "Country": "Australia",
            "Symbol": "$",
            "Code": "AUD"
            },
            {
            "Country": "Austria",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Azerbaijan",
            "Symbol": "₼",
            "Code": "AZN"
            },
            {
            "Country": "Bahrain",
            "Symbol": ".د.ب",
            "Code": "BHD"
            },
            {
            "Country": "Bangladesh",
            "Symbol": "৳",
            "Code": "BDT"
            },
            {
            "Country": "Barbados",
            "Symbol": "BD$",
            "Code": "BBD"
            },
            {
            "Country": "Belarus",
            "Symbol": "Br.",
            "Code": "BYN"
            },
            {
            "Country": "Belgium",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Bosnia and Herzegovina",
            "Symbol": "KM",
            "Code": "BAM"
            },
            {
            "Country": "Botswana",
            "Symbol": "P",
            "Code": "BWP"
            },
            {
            "Country": "Brazil",
            "Symbol": "R$",
            "Code": "BRL"
            },
            {
            "Country": "Brunei",
            "Symbol": "B$",
            "Code": "BND"
            },
            {
            "Country": "Bulgaria",
            "Symbol": "лв",
            "Code": "BGN"
            },
            {
            "Country": "Canada",
            "Symbol": "$",
            "Code": "CAD"
            },
            {
            "Country": "Cayman Islands",
            "Symbol": "CI$",
            "Code": "KYD"
            },
            {
            "Country": "China",
            "Symbol": "CN¥",
            "Code": "CNY"
            },
            {
            "Country": "Croatia",
            "Symbol": "kn",
            "Code": "HRK"
            },
            {
            "Country": "Cyprus",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Czech Republic",
            "Symbol": "Kč",
            "Code": "CZK"
            },
            {
            "Country": "Denmark",
            "Symbol": "kr.",
            "Code": "DKK"
            },
            {
            "Country": "Ecuador",
            "Symbol": "$",
            "Code": "USD"
            },
            {
            "Country": "Egypt",
            "Symbol": "E£",
            "Code": "EGP"
            },
            {
            "Country": "Estonia",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Ethiopia",
            "Symbol": "Br",
            "Code": "ETB"
            },
            {
            "Country": "Finland",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "France",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Georgia",
            "Symbol": "₾",
            "Code": "GEL"
            },
            {
            "Country": "Germany",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Ghana",
            "Symbol": "GH₵",
            "Code": "GHS"
            },
            {
            "Country": "Greece",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Grenada",
            "Symbol": "EC$",
            "Code": "XCD"
            },
            {
            "Country": "Guam",
            "Symbol": "$",
            "Code": "USD"
            },
            {
            "Country": "Hong Kong",
            "Symbol": "HK$",
            "Code": "HKD"
            },
            {
            "Country": "Hungary",
            "Symbol": "Ft",
            "Code": "HUF"
            },
            {
            "Country": "Iceland",
            "Symbol": "kr",
            "Code": "ISK"
            },
            {
            "Country": "India",
            "Symbol": "₹",
            "Code": "INR"
            },
            {
            "Country": "Indonesia",
            "Symbol": "Rp",
            "Code": "IDR"
            },
            {
            "Country": "Iran",
            "Symbol": "﷼",
            "Code": "IRR"
            },
            {
            "Country": "Ireland",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Israel",
            "Symbol": "₪",
            "Code": "ILS"
            },
            {
            "Country": "Italy",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Jamaica",
            "Symbol": "JA$",
            "Code": "JMD"
            },
            {
            "Country": "Japan",
            "Symbol": "JP¥",
            "Code": "JPY"
            },
            {
            "Country": "Jordan",
            "Symbol": "JD",
            "Code": "JOD"
            },
            {
            "Country": "Kazakhstan",
            "Symbol": "₸",
            "Code": "KZT"
            },
            {
            "Country": "Kenya",
            "Symbol": "KSh",
            "Code": "KES"
            },
            {
            "Country": "Kyrgyzstan",
            "Symbol": "лв",
            "Code": "KGS"
            },
            {
            "Country": "Latvia",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Lebanon",
            "Symbol": "L£",
            "Code": "LBP"
            },
            {
            "Country": "Lithuania",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Luxembourg",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Macao (SAR)",
            "Symbol": "MOP$",
            "Code": "MOP"
            },
            {
            "Country": "Macedonia (FYROM)",
            "Symbol": "ден",
            "Code": "MKD"
            },
            {
            "Country": "Malawi",
            "Symbol": "MK",
            "Code": "MWK"
            },
            {
            "Country": "Malaysia",
            "Symbol": "RM",
            "Code": "MYR"
            },
            {
            "Country": "Maldives",
            "Symbol": "Rf",
            "Code": "MVR"
            },
            {
            "Country": "Malta",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Mauritius",
            "Symbol": "Rs",
            "Code": "MUR"
            },
            {
            "Country": "Mexico",
            "Symbol": "MX$",
            "Code": "MXN"
            },
            {
            "Country": "Monaco",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Namibia",
            "Symbol": "N$",
            "Code": "NAD"
            },
            {
            "Country": "Nepal",
            "Symbol": "Rs",
            "Code": "NPR"
            },
            {
            "Country": "Netherlands",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "New Zealand",
            "Symbol": "$",
            "Code": "NZD"
            },
            {
            "Country": "Nicaragua",
            "Symbol": "C$",
            "Code": "NIO"
            },
            {
            "Country": "Niger",
            "Symbol": "CFA",
            "Code": "XOF"
            },
            {
            "Country": "Nigeria",
            "Symbol": "₦",
            "Code": "NGN"
            },
            {
            "Country": "Northern Cyprus",
            "Symbol": "₺",
            "Code": "TRY"
            },
            {
            "Country": "Norway",
            "Symbol": "kr",
            "Code": "NOK"
            },
            {
            "Country": "Oman",
            "Symbol": "ريال",
            "Code": "OMR"
            },
            {
            "Country": "Pakistan",
            "Symbol": "Rs",
            "Code": "PKR"
            },
            {
            "Country": "Palestinian Territory, Occupied",
            "Symbol": "£P",
            "Code": "PS"
            },
            {
            "Country": "Philippines",
            "Symbol": "₱",
            "Code": "PHP"
            },
            {
            "Country": "Poland",
            "Symbol": "zł",
            "Code": "PLN"
            },
            {
            "Country": "Portugal",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Puerto Rico",
            "Symbol": "$",
            "Code": "USD"
            },
            {
            "Country": "Qatar",
            "Symbol": "QR",
            "Code": "QAR"
            },
            {
            "Country": "Romania",
            "Symbol": "lei",
            "Code": "RON"
            },
            {
            "Country": "Russia",
            "Symbol": "₽",
            "Code": "RUB"
            },
            {
            "Country": "Rwanda",
            "Symbol": "RF",
            "Code": "RWF"
            },
            {
            "Country": "Saudi Arabia",
            "Symbol": "SR",
            "Code": "SAR"
            },
            {
            "Country": "Serbia",
            "Symbol": "РСД",
            "Code": "RSD"
            },
            {
            "Country": "Singapore",
            "Symbol": "S$",
            "Code": "SGD"
            },
            {
            "Country": "Slovakia",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Slovenia",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "South Africa",
            "Symbol": "R",
            "Code": "ZAR"
            },
            {
            "Country": "South Korea",
            "Symbol": "₩",
            "Code": "KRW"
            },
            {
            "Country": "Spain",
            "Symbol": "€",
            "Code": "EUR"
            },
            {
            "Country": "Sri Lanka",
            "Symbol": "Rs",
            "Code": "LKR"
            },
            {
            "Country": "Sweden",
            "Symbol": "kr",
            "Code": "SEK"
            },
            {
            "Country": "Switzerland",
            "Symbol": "CHF",
            "Code": "CHF"
            },
            {
            "Country": "Taiwan",
            "Symbol": "NT$",
            "Code": "TWD"
            },
            {
            "Country": "Tanzania",
            "Symbol": "TSh",
            "Code": "TZS"
            },
            {
            "Country": "Thailand",
            "Symbol": "฿",
            "Code": "THB"
            },
            {
            "Country": "Trinidad and Tobago",
            "Symbol": "TT$",
            "Code": "TTD"
            },
            {
            "Country": "Turkey",
            "Symbol": "₺",
            "Code": "TRY"
            },
            {
            "Country": "Uganda",
            "Symbol": "USh",
            "Code": "UGX"
            },
            {
            "Country": "Ukraine",
            "Symbol": "₴",
            "Code": "UAH"
            },
            {
            "Country": "United Arab Emirates",
            "Symbol": "د.إ",
            "Code": "AED"
            },
            {
            "Country": "United Kingdom",
            "Symbol": "£",
            "Code": "GBP"
            },
            {
            "Country": "United States of America",
            "Symbol": "$",
            "Code": "USD"
            },
            {
            "Country": "United States Virgin Islands",
            "Symbol": "$",
            "Code": "USD"
            },
            {
            "Country": "Vietnam",
            "Symbol": "₫",
            "Code": "VND"
            },
            {
            "Country": "Zambia",
            "Symbol": "ZK",
            "Code": "ZMW"
            }
        ]
    
    def get_currency_by_country(self, country):
        """Get currency details for a specific country."""
        for currency in self.currency_dict:
            if currency["Country"].lower() == country.lower():
                return currency
        return {"error": "Country not found"}

    def get_all_currencies(self):
        """Get all currency details."""
        return self.currency_dict

    def run(self, **kwargs):
        self.app.run(**kwargs)

# If you want to run the Flask app, you can still do that
if __name__ == '__main__':
    api = CurrencyAPI()
    api.run(debug=True)
