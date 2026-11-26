from pprint import pprint
import csv
import sqlite3

def main():

    with sqlite3.connect(r'chapitre_07\customers.db') as db:
        
        sql_insert = r"""INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) 
        VALUES (?,?,?,?,?)
        """
        with open(r'chapitre_07\MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                del row['id']
                db.execute(sql_insert,list(row.values()))


if __name__=='__main__':
    main()
    # s = r'c:\toto\new_projetc'
    # print(s)

