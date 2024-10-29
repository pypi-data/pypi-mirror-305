# -*- coding: utf-8 -*-
from sqlalchemy import create_engine


def insert_(sqlite_path, df, table_name):
    try:
        if not df.empty:
            # Create SQLAlchemy engine
            engine = create_engine(f'sqlite:///{sqlite_path}', echo=True)
            # Use pandas to_sql method to insert data
            df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=1000, method='multi')
            return 'Data inserted successfully'
        else:
            return f"{table_name} is None"
    except Exception as e:
        return f"Error inserting data: {e}"
