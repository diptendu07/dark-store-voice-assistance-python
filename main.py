from query_handler import load_data, show_inventory, show_product_sales_report, show_sales_report
from voice_input import get_voice_input

def main():
    df = load_data()
    query = get_voice_input().lower()
    print(f"[DEBUG] Recognized query: {query}")

    result = "Sorry, I didn't understand the request."
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]

    # Inventory check logic
    if "inventory" in query and "of" in query:
        product = None
        month = None

        if " in " in query:
            parts = query.split(" in ")
            if len(parts) == 2:
                product_part = parts[0].split(" of ")
                if len(product_part) == 2:
                    product = product_part[1].strip()
                    month = parts[1].strip().lower()
        else:
            product = query.split("of")[-1].strip()

        if product:
            if month and month.lower() in months:
                result = show_inventory(product, df, month)
            else:
                result = show_inventory(product, df)

    # Sales report logic
    elif "sales report" in query:
        product_specific = False
        product = None
        month = None

        if " of " in query and " for the month of " in query:
            parts = query.split(" for the month of ")
            if len(parts) == 2:
                month = parts[1].strip()
                product_part = parts[0].split(" of ")
                if len(product_part) == 2:
                    product = product_part[1].strip()
                    product_specific = True

        elif " of " in query and " in " in query:
            parts = query.split(" in ")
            if len(parts) == 2:
                month = parts[1].strip()
                product_part = parts[0].split(" of ")
                if len(product_part) == 2:
                    product = product_part[1].strip()
                    product_specific = True

        if product_specific and product and month:
            if month.lower() in months and product.lower() not in months:
                result = show_product_sales_report(product, month, df)
            else:
                result = "Please specify both a valid product and month."
        else:
            for month in months:
                if month in query:
                    result = show_sales_report(month, df)
                    break
            else:
                result = "Please specify a valid month for the sales report."

    print("\nResult:\n", result)

if __name__ == "__main__":
    main()
