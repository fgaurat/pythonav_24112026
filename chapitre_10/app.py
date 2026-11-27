from flask import Flask,render_template
from customer_dao import CustomerDAO
from  pathlib import Path
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name=""):
    return render_template('hello.html',the_name=name)

@app.route("/")
def customers():
    root_path = Path(".")
    db_file = root_path / "customers.db"
    dao = CustomerDAO(db_file)

    # # customers = dao.findAll()
    customers = dao.findAll()
    # customers=[]
    return render_template('customers.html',customers=customers)