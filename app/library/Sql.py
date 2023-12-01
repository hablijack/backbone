from datetime import datetime as dt

class Sql():

    def generate_solarpanel_insert_stmt(self, temp, status, power):
        insert_stmt = 'INSERT INTO "solarpanels" ("timestamp","temperature","status","power") VALUES (\'{}\', {}, {}, {})'
        return insert_stmt.format(dt.now(), temp, status, power)

    def generate_zoe_insert_stmt(self, battery_level, total_mileage):
        insert_stmt = 'INSERT INTO "zoe" ("timestamp","battery_level","total_mileage") VALUES (\'{}\' {}, {})'
        return insert_stmt.format(dt.now(), battery_level, total_mileage)

    def generate_solarpanel_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS solarpanels_index ON solarpanels (timestamp);'

    def generate_zoe_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS zoe_index ON zoe (timestamp);'

    def generate_solarpanel_table_stmt(self):
        return 'CREATE TABLE IF NOT EXISTS "solarpanels" ("id" BIGSERIAL NOT NULL,"timestamp" TIMESTAMP WITH TIME ZONE NOT NULL,"temperature" FLOAT NOT NULL,"status" INT NOT NULL,"power" FLOAT NOT NULL,PRIMARY KEY ("id"))'

    def generate_zoe_table_stmt(self):
        return 'CREATE TABLE IF NOT EXISTS "zoe" ("id" BIGSERIAL NOT NULL,"timestamp" TIMESTAMP WITH TIME ZONE NOT NULL,"battery_level" FLOAT NOT NULL,"total_mileage" FLOAT NOT NULL,PRIMARY KEY ("id"))'
