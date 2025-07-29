from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 产品列表常量
PRODUCTS = [
    {"id": 1, "name": "速冻甜玉米粒", "images": ["product1_1.jpg", "product1_2.jpg", "product1_3.jpg"]},
    {"id": 2, "name": "甜玉米棒",    "images": ["product2_1.jpg", "product2_2.jpg", "product2_3.jpg"]},
    {"id": 3, "name": "糯玉米棒",    "images": ["product3_1.jpg", "product3_2.jpg", "product3_3.jpg"]},
    {"id": 4, "name": "甜青豆",      "images": ["product4_1.jpg", "product4_2.jpg", "product4_3.jpg"]},
    {"id": 5, "name": "毛豆",        "images": ["product5_1.jpg", "product5_2.jpg", "product5_3.jpg"]},
    {"id": 6, "name": "花生",        "images": ["product6_1.jpg", "product6_2.jpg", "product6_3.jpg"]},
    {"id": 7, "name": "什锦菜",      "images": ["product7_1.jpg", "product7_2.jpg", "product7_3.jpg"]},
    {"id": 8, "name": "设备展示",    "images": ["equipment1.jpg", "equipment2.jpg", "equipment3.jpg",
                                               "equipment4.jpg", "equipment5.jpg", "equipment6.jpg",
                                               "equipment7.jpg", "equipment8.jpg"]}
]

# ---------- 路由 ----------
@app.route('/')
def index():
    return render_template('index.html', active='index')

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS, active='products')

@app.route('/news')
def news():
    return render_template('news.html', active='news')

@app.route('/cooperation')
def cooperation():
    return render_template('cooperation.html', active='cooperation')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product.html', product=product, active='products')

@app.route('/tencent7849794202945294551.txt')
def tencent_verify():
    return send_from_directory('.', 'tencent7849794202945294551.txt')

if __name__ == '__main__':
    app.run(debug=True)