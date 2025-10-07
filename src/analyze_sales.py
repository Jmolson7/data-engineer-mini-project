import pandas as pd
from sqlalchemy import create_engine

# Подключение к локальной базе
engine = create_engine("sqlite:///data/sales.db")

# Загружаем таблицы
customers = pd.read_sql("SELECT * FROM customers", engine)
products  = pd.read_sql("SELECT * FROM products", engine)
orders    = pd.read_sql("SELECT * FROM orders", engine)
items     = pd.read_sql("SELECT * FROM order_items", engine)

# Объединяем таблицы в единый датафрейм
df = (
    items
    .merge(products, on="product_id")
    .merge(orders, on="order_id")
    .merge(customers, on="customer_id")
)

# Добавляем столбец с суммой строки (цена * количество)
df["line_total"] = df["price"] * df["quantity"]

print("✅ Всего строк:", len(df))

print("\n💰 Доход по клиентам:")
print(
    df.groupby("customer_name")["line_total"]
      .sum()
      .sort_values(ascending=False)
)

print("\n📦 Доход по категориям:")
print(
    df.groupby("category")["line_total"]
      .sum()
      .sort_values(ascending=False)
)

print("\n🏙️ Доход по городам:")
print(
    df.groupby("city")["line_total"]
      .sum()
      .sort_values(ascending=False)
)

# Сохраняем отчёт
df.to_csv("data/full_sales_join.csv", index=False)
print("\n✅ Отчёт сохранён в data/full_sales_join.csv")
