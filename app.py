import requests


url = 'https://invoice-generator.com'

headers = {
    "logo": "http://invoiced.com/img/logo-invoice.png",
    "from": "Invoiced\n701 Brazos St\nAustin, TX 78748",
    "to": "Johnny Appleseed",
    "currency": "usd",
    "number": "INV-0001",
    "payment_terms": "Auto-Billed - Do Not Pay",
    "items": [
        {
            "name": "Subscription to Starter Pro Pack",
            "quantity": 1,
            "unit_cost": 16
        }
    ],
    "fields": {
        "tax": "%"
    },
    "tax": 5,
    "notes": "Thanks for being an awesome customer!",
    "terms": "No need to submit payment. You will be auto-billed for this invoice."
}

response = requests.post(url, json = headers)

print("Status code: ", response.status_code)

with open('invoice.pdf', 'wb') as f:
    f.write(response.content)