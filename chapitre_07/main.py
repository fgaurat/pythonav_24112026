from customer_dao import CustomerDAO
from pathlib import Path

def main():
    root_path = Path(".")
    db_file = root_path / "chapitre_07"/ "customers.db"
    dao = CustomerDAO(db_file)

    customers = dao.findAll()
    # for customer in customers:
    #     print(customer)
if __name__=='__main__':
    main()
