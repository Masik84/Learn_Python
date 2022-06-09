from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# скопировать url с elephantsql.com и вписать postgresql вместо postgres
engine = create_engine('postgresql://qpgmaudp:MZ8uVCK-n1p3LIJqQow8E5yWoapR4lTH@abul.db.elephantsql.com/qpgmaudp')
db_session = scoped_session(sessionmaker(bind=engine))


Base = declarative_base()
Base.query = db_session.query_property()
