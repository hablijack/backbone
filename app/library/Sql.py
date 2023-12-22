from datetime import datetime as dt

class Sql():

    def generate_poweropti_insert_stmt(self, watt):
        insert_stmt = 'INSERT INTO "poweropti" ("timestamp","watt") VALUES (\'{}\', {});'
        return insert_stmt.format(dt.now(), watt)

    def generate_solarpanel_insert_stmt(self, temp, status, power):
        insert_stmt = 'INSERT INTO "solarpanels" ("timestamp","temperature","status","power") VALUES (\'{}\', {}, {}, {});'
        return insert_stmt.format(dt.now(), temp, status, power)

    def generate_zoe_insert_stmt(self, battery_level, total_mileage):
        insert_stmt = 'INSERT INTO "zoe" ("timestamp","battery_level","total_mileage") VALUES (\'{}\', {}, {});'
        return insert_stmt.format(dt.now(), battery_level, total_mileage)

    def generate_solarpanel_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS solarpanels_index ON solarpanels (timestamp);'

    def generate_zoe_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS zoe_index ON zoe (timestamp);'

    def generate_poweropti_index_stmt(self):
        return 'CREATE INDEX IF NOT EXISTS poweropti_index ON poweropti (timestamp);'

    def generate_zoe_table_stmt(self):
        return 'CREATE TABLE IF NOT EXISTS "zoe" ("id" BIGSERIAL NOT NULL,"timestamp" TIMESTAMP WITH TIME ZONE NOT NULL,"battery_level" FLOAT NOT NULL,"total_mileage" FLOAT NOT NULL,PRIMARY KEY ("id"));'

    def generate_poweropti_table_stmt(self):
        return 'CREATE TABLE IF NOT EXISTS "poweropti" ("id" BIGSERIAL NOT NULL,"timestamp" TIMESTAMP WITH TIME ZONE NOT NULL,"watt" FLOAT NOT NULL,PRIMARY KEY ("id"));'

    def generate_solarpanel_table_stmt(self):
        return 'CREATE TABLE IF NOT EXISTS "solarpanels" ("id" BIGSERIAL NOT NULL,"timestamp" TIMESTAMP WITH TIME ZONE NOT NULL,"temperature" FLOAT NOT NULL,"status" INT NOT NULL,"power" FLOAT NOT NULL,PRIMARY KEY ("id"));'

    def generate_solarpanel_cleanup_stmt(self):
        return 'DELETE FROM solarpanels WHERE timestamp < now() - interval \'1 days\';'
    
    def generate_zoe_cleanup_stmt(self):
        return 'DELETE FROM zoe WHERE timestamp < now() - interval \'1 days\';'

    def generate_poweropti_cleanup_stmt(self):
        return 'DELETE FROM poweropti WHERE timestamp < now() - interval \'1 days\';'

    def generate_solarpanel_last_entry_query(self):
        return 'SELECT temperature, power FROM solarpanels ORDER BY "timestamp" DESC LIMIT 1;'

    def generate_solarpanel_all_entries_query(self):
        return 'SELECT temperature, timestamp, power FROM solarpanels WHERE DATE(timestamp) = current_date order by timestamp ASC;'

    def generate_poweropti_last_entry_query(self):
        return 'SELECT watt FROM poweropti ORDER BY "timestamp" DESC LIMIT 1;'

    def generate_zoe_last_entry_query(self):
        return 'SELECT battery_level, total_mileage FROM zoe ORDER BY "timestamp" DESC LIMIT 1;'