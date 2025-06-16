
# 📦 Dark Store Inventory & Sales Analytics Assistant

A voice-enabled Python application that helps **Dark Store operators** and **retail analytics teams** query inventory and sales reports interactively from a CSV database.  
Now enhanced with **interactive charts and visual analytics** using `Matplotlib`.

---

## 🧠 Features

- 🎙️ **Voice Recognition**: Ask your queries naturally via microphone (e.g., "Show me the inventory of Avocado in March").
- 📊 **Sales Reports**:
  - General monthly sales summaries.
  - Product-wise sales breakdown for a given month.
- 📦 **Inventory Tracking**:
  - Real-time inventory calculation based on total stock and units sold.
  - Supports month-specific inventory insights.
  - 📉 **Now with pie/bar charts** for inventory visualization.

---

## 🗂️ Project Structure

```
dark-store-analytics/
│
├── data/
│   └── BigBasketProducts.csv       # Your source dataset
│
├── main.py                         # Application entry point
├── query_handler.py                # Business logic for sales & inventory
├── voice_input.py                  # Speech-to-text module
└── README.md                       # Project documentation

```

---

## 🎤 Sample Queries You Can Ask
```
| Intent                 | Example Query                                      |
| ---------------------- | -------------------------------------------------- |
| Inventory (General)    | "Show me the inventory of Garlic Oil"              |
| Inventory (Monthly)    | "What is the inventory of Garlic Oil in February?" |
| Sales Report (General) | "Show me the sales report for March"               |
| Sales Report (Product) | "Give me the sales report of Garlic Oil in March"  |
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- Microphone input supported
- Install Python packages:

```bash
pip install pandas matplotlib speechrecognition
```

For microphone input:
```bash
pip install pyaudio
```

> **Note:** On some systems, installing `pyaudio` may require additional setup or using `pipwin`:
```bash
pip install pipwin
pipwin install pyaudio
```

---

### ▶️ How to Run

```bash
python main.py
```

Then speak your query clearly when prompted. Example:
> "Show me the inventory of Banana in July"

---

## 🧮 CSV Format Requirements

This app works with both clean retail CSVs or partial datasets (e.g., BigBasketProducts.csv).

If your file does not contain units_sold, stock, or order_date, they will be auto-generated for demonstration purposes.
```
| Required Columns               | Description         |
| ------------------------------ | ------------------- |
| `product_name` or `product`    | Name of the product |
| `sales_amount` or `sale_price` | Revenue per product |


Auto-generated fields:

stock: Total quantity stocked

units_sold: Quantity sold

order_date: Simulated from a rolling 6-month window
```
---

## 📈 Output Example

```
Inventory Summary for Garlic Oil in March:
----------------------------------------
Total Stock Received: 520
Total Units Sold: 340
Net Inventory in Stock: 180
----------------------------------------

```

Chart Output:

📊 Bar chart of product-wise sales per month.

📉 Pie chart of sold vs remaining inventory for product/month.

Charts will auto-display in a window during execution.

---

## 👨‍💼 Target Use Case

- Dark Stores and Micro Fulfillment Centers
- Retail businesses with rapid stock turnover
- Data teams needing fast insight into inventory and product performance

---

## 🛡️ Author & Support

Developed by [DIPTENDU LODH]. For support or integration inquiries, please reach out via [diptendulodh@gmail.com].
