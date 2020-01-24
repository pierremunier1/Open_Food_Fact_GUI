from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

import config
from base import Base


class Sqlconnection:
    """setup the connection to the database."""

    def __init__(self):
        """initalizing variables and connect to the database."""
        self.variable_table_product = config.TABLE_PRODUCT
        self.variable_table_category = config.TABLE_CATEGORY
        self.variable_table_store = config.TABLE_STORE
        self.db_infos_user = config.USER
        self.db_infos_pwd = config.PWD
        self.db_infos_db = config.DB
        self.engine = create_engine(
            """mysql+mysqlconnector://
                {username}:{password}@localhost/{database}""".format(
                username=self.db_infos_user,
                password=self.db_infos_pwd,
                database=self.db_infos_db,
            )
        )
        self.session = sessionmaker(self.engine)
        self.engine.connect()
        self.metadata = MetaData(self.engine)

    def table_initializing(self):
        """generate database schema."""

        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
