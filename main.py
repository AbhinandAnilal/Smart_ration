from flask import Flask
from public import public
from admin import admin
from gov import gov
from shop import shop
from api import api
app=Flask(__name__)
app.secret_key="prayulla"
app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(gov)
app.register_blueprint(shop)
app.register_blueprint(api)
app.run(debug=True,port=5077,host="0.0.0.0")