# 🗂️ Data Engineer Mini Project — SQL + Python + Pandas
[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)]()
[![SQLite](https://img.shields.io/badge/SQLite-3.51-blue?logo=sqlite&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/pandas-2.2.2-yellow?logo=pandas&logoColor=white)]()
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.32-red?logo=databricks&logoColor=white)]()
[![ETL Pipeline](https://img.shields.io/badge/ETL%20Pipeline-Mini_Project-green)]()
[![ASTON Internship](https://img.shields.io/badge/ASTON-Data_Engineer-orange)]()

Мини-ETL: CSV → SQLite → SQL-запросы → pandas-анализ → отчёты.
Подготовка к стажировке ASTON Data Engineer.

---

## 🚀 Запуск
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/load_to_db.py
python src/analyze_sales.py
```

---

## 📁 Структура проекта
```plaintext
data-engineer-mini-project/
├── data/                # CSV и локальная БД (sales.db не пушим)
├── sql/                 # create_tables + учебные запросы
├── src/                 # Python-скрипты ETL и анализа
├── requirements.txt     # зависимости проекта
└── README.md            # описание проекта
```
---

## 💡 Пример SQL-запроса
```sql
-- Топ клиентов по выручке
SELECT c.customer_name, SUM(p.price * oi.quantity) AS total_spent
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN products p     ON p.product_id  = oi.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC;
```
---

## 🧰 Технологии

SQLite3 — локальная база данных

SQLAlchemy — подключение к БД

pandas — анализ данных

Python 3.12 — основной язык проекта

Jupyter / VSCode — для визуализации и интерактивного анализа

---

## 📊 Результат

✅ 5 строк объединённых данных
✅ Автоматическое вычисление выручки
✅ CSV-отчёт: data/full_sales_join.csv
✅ Готовая структура для мини-ETL-проекта

---

## 📷 Пример вывода Python-анализа (pandas)

✅ Всего строк: 5

💰 Доход по клиентам:
customer_name
Andrey    210.0
Lera       40.0
Name: line_total, dtype: float64

📦 Доход по категориям:
category
Apparel        195.0
Supplements     55.0
Name: line_total, dtype: float64

🏙️ Доход по городам:
city
Moscow    210.0
Perm       40.0
Name: line_total, dtype: float64

✅ Отчёт сохранён в data/full_sales_join.csv

---

**[Андрей Крылов](https://github.com/Akchemp)**
📧 [ak.chemp@gmail.com](mailto:ak.chemp@gmail.com)

---
