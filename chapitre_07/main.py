from customer_dao import CustomerDAO
from pathlib import Path

def main():
    root_path = Path(".")
    db_file = root_path / "chapitre_07"/ "customers.db"
    dao = CustomerDAO(db_file)

    # customers = dao.findAll()
    customers = list(dao.findAll())
    # c1 = next(customers)
    # c2 = next(customers)
    # c3 = next(customers)
    for customer in customers:
        print(customer)
if __name__=='__main__':
    main()
