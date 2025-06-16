import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    try:
        df = pd.read_csv('data/BigBasketProducts.csv')
    except FileNotFoundError:
        return pd.DataFrame()

    # Rename for compatibility
    df.rename(columns={'product': 'product_name', 'sale_price': 'sales_amount'}, inplace=True)

    # Simulate missing fields
    np.random.seed(42)
    df['units_sold'] = np.random.randint(10, 1000, size=len(df))
    df['stock'] = df['units_sold'] + np.random.randint(50, 300, size=len(df))
    df['order_date'] = pd.to_datetime(
        pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 180, size=len(df)), unit='D')
    )

    return df

def show_inventory(product_name, df, month=None):
    if df.empty:
        return "Data could not be loaded. Please check the CSV path."

    filtered = df[df['product_name'].str.lower().str.contains(product_name.lower(), na=False)]

    if filtered.empty:
        return f"No inventory found for '{product_name}'."

    if month:
        month = month.lower()
        filtered = filtered[filtered['order_date'].dt.month_name().str.lower() == month]
        if filtered.empty:
            return f"No inventory records found for '{product_name}' in {month.capitalize()}."

    total_stock = filtered['stock'].sum()
    total_units_sold = filtered['units_sold'].sum()
    net_inventory = total_stock - total_units_sold

    # Plotting
    plt.figure(figsize=(6, 5))
    plt.bar(['Total Stock', 'Units Sold', 'Net Inventory'],
            [total_stock, total_units_sold, net_inventory],
            color=['blue', 'red', 'green'])
    title = f"Inventory Summary for {product_name.title()}"
    if month:
        title += f" in {month.capitalize()}"
    plt.title(title)
    plt.ylabel("Units")
    plt.tight_layout()
    plt.show()

    return (
        f"{title}:\n"
        f"----------------------------------------\n"
        f"Total Stock Received: {total_stock}\n"
        f"Total Units Sold: {total_units_sold}\n"
        f"Net Inventory in Stock: {net_inventory}\n"
        f"----------------------------------------"
    )

def show_sales_report(month_name, df):
    if df.empty:
        return "Data could not be loaded. Please check the CSV path."

    df = df[df['order_date'].notna()]
    month_name = month_name.lower()
    df_month = df[df['order_date'].dt.month_name().str.lower() == month_name]

    if df_month.empty:
        return f"No sales data found for the month of {month_name.capitalize()}."

    summary = (
        df_month.groupby('product_name')
        .agg(
            total_units_sold=('units_sold', 'sum'),
            total_sales_amount=('sales_amount', 'sum')
        )
        .reset_index()
    )

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(summary['product_name'], summary['total_units_sold'], color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.title(f"Total Units Sold per Product in {month_name.capitalize()}")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.show()

    return (
        f"Sales Report for {month_name.capitalize()}:\n\n"
        + summary.to_string(index=False)
    )

def show_product_sales_report(product_name, month_name, df):
    if df.empty:
        return "Data could not be loaded. Please check the CSV path."
    
    month_name = month_name.lower()
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    if month_name not in months:
        return f"Invalid month: {month_name.capitalize()}. Please specify a valid month."
    
    df_filtered = df[
        (df['product_name'].str.lower().str.contains(product_name.lower())) &
        (df['order_date'].dt.month_name().str.lower() == month_name)
    ]

    if df_filtered.empty:
        return f"No sales found for {product_name} in {month_name.capitalize()}."

    total_units = df_filtered['units_sold'].sum()
    total_stock = df_filtered['stock'].sum()
    net_inventory = total_stock - total_units
    total_sales = df_filtered['sales_amount'].sum()

    # Pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(
        [total_units, max(net_inventory, 0)],
        labels=['Sold', 'Remaining'],
        autopct='%1.1f%%',
        colors=['orange', 'green']
    )
    plt.title(f"Sales Distribution for {product_name.title()} in {month_name.capitalize()}")
    plt.tight_layout()
    plt.show()

    return (
        f"Sales Report for {product_name.title()} in {month_name.capitalize()}:\n"
        f"----------------------------------------\n"
        f"Total Units Sold: {total_units}\n"
        f"Total Sales Amount: ₹{total_sales:.2f}\n"
        f"----------------------------------------"
    )
