from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer,BigInteger, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
session = sessionmaker(bind=engine)



class sale(Base):
    __tablename__ ='sales'

    sale_day = Column(Date)
    sector = Column(String)
    property_type = Column(String)
    rooms = Column(Integer)
    floor = Column(Integer)
    sqrm = Column(Integer)
    price = Column(BigInteger)
    Trend_of_change= Column(String)


    def __init__(self, sale_day, sector, property_type, rooms, floor, sqrm, price, Trend_of_change ):
        self.sale_day = sale_day
        self.sector = sector
        self.property_type = property_type
        self.rooms = rooms
        self.floor = floor
        self.sqrm = sqrm
        self.price = price
        self.Trend_of_change= Trend_of_change


