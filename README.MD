
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
│   └── dark_store_data.csv        # Your source dataset
│
├── main.py                        # Application entry point
├── query_handler.py               # Business logic for sales & inventory
├── voice_input.py                 # Speech-to-text module
└── README.md                      # Project documentation
```

---

## 🎤 Sample Queries You Can Ask

| Intent                 | Example Query                                       |
|-----------------------|-----------------------------------------------------|
| Inventory (General)   | "Show me the inventory of Avocado"                  |
| Inventory (Monthly)   | "What is the inventory of Milk in February?"        |
| Sales Report (General)| "Show me the sales report for June"                 |
| Sales Report (Product)| "Give me the sales report of Eggs for the month of May" |

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

Make sure your `dark_store_data.csv` includes at least the following columns:

| Column         | Description                       |
|----------------|-----------------------------------|
| product_name   | Name of the product               |
| order_date     | Date of stock entry/sale (dd/mm/yyyy) |
| stock          | Quantity stocked in               |
| units_sold     | Quantity sold                     |
| sales_amount   | Revenue generated                 |

---

## 📈 Output Example

```
Inventory Summary for Avocado in March:
----------------------------------------
Total Stock Received: 250
Total Units Sold: 160
Net Inventory in Stock: 90
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
