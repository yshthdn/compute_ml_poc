import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))
print('basedir... ' + basedir)

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'compute.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:compute2019@compute.cbdmgixmjdpo.us-east-2.rds.amazonaws.com:3306/testdb1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Earth@88@localhost:3306/testdb1'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin2019@testdb1.cluster-cbdmgixmjdpo.us-east-2.rds.amazonaws.com:3306/testdb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

