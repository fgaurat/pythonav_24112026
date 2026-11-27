import sqlite3

from customer import Customer

class CustomerDAO:
    
    
    def __init__(self,db_file):
        self._con = sqlite3.connect(db_file)

    def findAllOld(self):
        all_customers = []
        cur = self._con.cursor()
        sql = "SELECT * FROM customers_tbl"
        res = cur.execute(sql)
        
        for row in res.fetchall():
            cust = Customer(*row)
            all_customers.append(cust)
        
        return all_customers

    def findAll(self):
        cur = self._con.cursor()
        sql = "SELECT * FROM customers_tbl"
        res = cur.execute(sql)
        
        for row in res.fetchall():
            cust = Customer(*row)
            yield cust
        
    
    def __del__(self):
        self._con.close()