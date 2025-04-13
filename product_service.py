from flask import Flask, request, jsonify

app = Flask(__name__)

products = []

@app.route('/add_product', methods=['POST'])
def add_product():
    product = request.json
    products.append(product)
    return jsonify({"message": "Product added successfully!"})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)