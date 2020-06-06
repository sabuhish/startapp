factories = '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# import databases

envsettings = os.getenv("settings")

if envsettings == "dev" or envsettings == "default":
    from core.settings.devsettings import DevSettings
    settings = DevSettings()

elif envsettings == "prod":
    from core.settings.prodsettings import ProdSettings
    settings= ProdSettings()
    
else:
    from core.settings.settings import BaseConfig
    settings = BaseConfig()




# engine = create_engine(
#     settings.DATABASE_URL, pool_pre_ping=True
# )
# Session : sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)



'''