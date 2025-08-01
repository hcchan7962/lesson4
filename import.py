import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('constituent_estates.db')
cursor = conn.cursor()

# Read the CSV file with Big5 encoding
with open('CCI Estate for Opendata.csv', 'r', encoding='big5hkscs') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    # Prepare the insert statement
    insert_query = '''
    INSERT INTO Constituent_Estates (
        c_estate, e_estate, pc_addr, pe_addr, scp_mktc, scp_mkte, 
        min_opdate, max_opdate, blgcount, pc_dev, pe_dev, 
        facilities_c, facilities_e, url
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''

    # Insert each row into the database
    for row in reader:
        cursor.execute(insert_query, row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully.")