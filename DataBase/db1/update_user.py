from db import db_session
from db2.models import User

user = User.query.first()
user.salary = 2345
db_session.commit()