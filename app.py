from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()


# Adding data to DB
# user = User()
# user.id = 1
# user.username = 'Nishant Nawarkhede'
#
# session.add(user)
# session.commit()


# Retrieving data from DB
all_users = session.query(User).all()
for user in all_users:
    print '%s %s' % (user.id, user.username)

session.close()g