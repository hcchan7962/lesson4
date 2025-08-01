import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('constituent_estates.db')

# Create a cursor object
cursor = conn.cursor()

# Create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS constituent_estates (
    c_estate TEXT,
    e_estate TEXT,
    pc_addr TEXT,
    pe_addr TEXT,
    scp_mktc TEXT,
    scp_mkte TEXT,
    min_opdate INTEGER,
    max_opdate INTEGER,
    blgcount INTEGER,
    pc_dev TEXT,
    pe_dev TEXT,
    facilities_c TEXT,
    facilities_e TEXT,
    url TEXT
    
);
'''

# Execute the create table query
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")