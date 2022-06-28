from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
# , Customers, Categories, Products, Invoices, InvoicesProducts


db = "sqlite"
SQLALCHEMY_DATABASE_URI = f"{db}:////Users/hamed/Documents/pyjobs/MobileCRM/backend/db/mobileCRM1.sqlite"
engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # connect_args={"check_same_thread": False},
    # poolclass=StaticPool,
    echo=False,
)


Session = sessionmaker(engine)
# dbsession = Session()

# Base.metadata.create_all(engine)