from datetime import datetime

from sqlalchemy import values
from sqlalchemy.ext.automap import automap_base

from models import create_new_engine, create_new_session

def get_categories(engine, session):
    # Автоматическое сопоставление таблиц с существующей схемой базы данных
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    # Получаем таблицу Category
    Categories = Base.classes.category


    # Получение всех записей из таблицы Categories
    categories = session.query(Categories).all()
    
    
    # Парсинг категорий
    wastes = []
    incomes = []
    for category in categories:
        if category.name:
            if category.type == 1:
                incomes.append(category.name)
            elif category.type == 2:
                wastes.append(category.name)

    return {"wastes": wastes, "incomes":incomes}

def insert_transaction (engine, session, note, type, amount, 
                        date_time, category_id, wallet_id, transfer_wallet_id=-1,
                         debt_id=0, debt_trans_id=0,
                        account_id=1, fee_id=0, subcategory_id=0, memo=None, trans_amount=0):
    Base = automap_base()
    Base.prepare(engine, reflect=True)



    if not type in [0, 1, 2]:
        raise ValueError
    
    
    amount = amount * 100
    # Получаем таблицу trans
    Transaction = Base.classes.trans
    new_transaction = Transaction(note=note, memo=memo, type=type, amount=amount, 
                                  date_time=date_time, account_id=account_id,
                                  fee_id=fee_id, category_id=category_id, subcategory_id=subcategory_id,
                                  wallet_id=wallet_id, trans_amount=trans_amount, transfer_wallet_id=transfer_wallet_id,
                                  debt_id=debt_id, debt_trans_id=debt_trans_id)
    session.add(new_transaction)
    session.commit()
    



if __name__ == "__main__":
    engine = create_new_engine("backup_20240903_012508.db")
    session = create_new_session(engine)
    current_time = datetime.now()
    insert_transaction(engine=engine, session=session, note="Тестовая транзакция", type=1, amount=1,
                       date_time=current_time.timestamp(), category_id=30, wallet_id=1)