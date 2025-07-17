from flask import Flask
from routes.customer_routes import customer_n
from routes.product_routes import product_n
from routes.transaction_routes import transaction_n
from database import Base, engine
from models.customer import Customer
from models.product import Product
from models.transaction import Transaction

app = Flask(__name__)

app.register_blueprint(customer_n)
app.register_blueprint(product_n)
app.register_blueprint(transaction_n)

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run(debug=True)
