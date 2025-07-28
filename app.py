from flask import Flask, render_template
from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='.')
app = Flask(__name__)

# 产品数据（包含设备展示）
products = [
    {"id": 1, "name": "速冻甜玉米粒", "images": ["product1_1.jpg", "product1_2.jpg", "product1_3.jpg"]},
    {"id": 2, "name": "甜玉米棒",    "images": ["product2_1.jpg", "product2_2.jpg", "product2_3.jpg"]},
    {"id": 3, "name": "糯玉米棒",    "images": ["product3_1.jpg", "product3_2.jpg", "product3_3.jpg"]},
    {"id": 4, "name": "甜青豆",      "images": ["product4_1.jpg", "product4_2.jpg", "product4_3.jpg"]},
    {"id": 5, "name": "毛豆",        "images": ["product5_1.jpg", "product5_2.jpg", "product5_3.jpg"]},
    {"id": 6, "name": "花生",        "images": ["product6_1.jpg", "product6_2.jpg", "product6_3.jpg"]},
    {"id": 7, "name": "什锦菜",      "images": ["product7_1.jpg", "product7_2.jpg", "product7_3.jpg"]},
    {"id": 8, "name": "设备展示",    "images": ["equipment2.jpg", "equipment3.jpg","equipment4.jpg","equipment5.jpg","equipment6.jpg","equipment7.jpg","equipment8.jpg"]}
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
