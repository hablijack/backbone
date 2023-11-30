from pypika import PostgreSQLQuery, Table, Column, Index
from datetime import datetime as dt

class Sql():

    def generate_solarpanel_insert_stmt(self, temp, status, power):
        solarpanels = Table('solarpanels')
        query = PostgreSQLQuery \
            .into(solarpanels) \
            .columns('timestamp', 'temperature', 'status', 'power') \
            .insert(dt.now(), temp, status, power)
        return query.get_sql()

    def generate_zoe_insert_stmt(self, battery_level, total_mileage):
        zoe = Table('zoe')
        query = PostgreSQLQuery \
            .into(zoe) \
            .columns('timestamp', 'battery_level', 'total_mileage') \
            .insert(dt.now(), battery_level, total_mileage)
        return query.get_sql()

    def generate_solarpanel_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS solarpanels_index ON solarpanels (timestamp);'

    def generate_solarpanel_table_stmt(self):
        return PostgreSQLQuery \
            .create_table('solarpanels') \
            .if_not_exists() \
            .columns(
                Column('id', 'BIGSERIAL', nullable=False),
                Column('timestamp', 'TIMESTAMP WITH TIME ZONE', nullable=False),
                Column('temperature', 'FLOAT', nullable=False),
                Column('status', 'INT', nullable=False),
                Column('power', 'FLOAT', nullable=False)) \
            .primary_key('id').get_sql()
