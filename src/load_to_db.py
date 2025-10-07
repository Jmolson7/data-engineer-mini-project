import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "sales.db"

def run_schema_sql(engine, sql_text: str):
    with engine.begin() as conn:
        backend = engine.url.get_backend_name()
        if backend == "sqlite":
            raw = conn.connection  # DBAPI connection
            raw.executescript(sql_text)
        else:
            for stmt in sql_text.split(";"):
                s = stmt.strip()
                if s:
                    conn.exec_driver_sql(s)

def main():
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products  = pd.read_csv(DATA_DIR / "products.csv")
    orders    = pd.read_csv(DATA_DIR / "orders.csv")
    items     = pd.read_csv(DATA_DIR / "order_items.csv")

    engine = create_engine(f"sqlite:///{DB_PATH}")

    schema_sql = (BASE_DIR / "sql" / "create_tables.sql").read_text(encoding="utf-8")
    run_schema_sql(engine, schema_sql)

    with engine.begin() as conn:
        customers.to_sql("customers", conn, if_exists="append", index=False)
        products.to_sql("products", conn, if_exists="append", index=False)
        orders.to_sql("orders", conn, if_exists="append", index=False)
        items.to_sql("order_items", conn, if_exists="append", index=False)

    with engine.connect() as conn:
        total_orders = conn.execute(text("SELECT COUNT(*) FROM orders")).scalar_one()
        total_items  = conn.execute(text("SELECT COUNT(*) FROM order_items")).scalar_one()

    print(f"✅ Загрузка завершена. Заказов: {total_orders}, позиций: {total_items}")
    print(f"📦 База данных: {DB_PATH}")

if __name__ == "__main__":
    main()
