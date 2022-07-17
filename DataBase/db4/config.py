from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db_url = "postgresql://tovezpxg:Ew-LecxihhBMy3SSg1zEitg9rZmDIqY9@abul.db.elephantsql.com/tovezpxg"

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')


SECRET_KEY = 'jvhsdIUY[kPOI_(pnv[awurugg37yPOugp(7T-ouhy{76'

REMEMBER_COOKIE_DURATION = timedelta(days=0)

SQLALCHEMY_TRACK_MODIFICATIONS = False