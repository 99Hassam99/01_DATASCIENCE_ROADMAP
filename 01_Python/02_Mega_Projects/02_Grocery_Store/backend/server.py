from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET']) # restful APi
def get_products():
    products = products_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/deleteProducts', methods=['POST'])
def delete_product():
    products = products_dao.delete_product(connection, request.form['product_id'])
    response=jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



if __name__ == '__main__':
    print('Starting Python Flask server for grocery store Management system.')
    app.run(port=5000,  debug=True)
    print('ss')