from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base



engine=create_engine('postgresql://postgres:aryan%400907@localhost:5432/pizza_delivery')   



Base=declarative_base()

Session=sessionmaker()


