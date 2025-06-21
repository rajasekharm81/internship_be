import models
from database import engine


print("dropping database ...")
print("database dropped")
print("creating database ...")
models.Base.metadata.create_all(bind=engine)
print("created database")
