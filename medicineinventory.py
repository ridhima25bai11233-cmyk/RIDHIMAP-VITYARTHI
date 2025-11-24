# MEDICINE INVENTORY MANAGEMENT SYSTEM


inventory = []


#search

def find_by_batch(batch_no):
    """Return a medicine record by batch number, or None."""
    for item in inventory:
        if item["batch_no"] == batch_no:
            return item
    return None


def find_by_name(name):
    """Return list of medicines matching given name (case-insensitive)."""
    name = name.strip().lower()
    return [item for item in inventory if item["name"].lower() == name]


# input

def input_int(prompt):
    value = input(prompt).strip()
    if value.isdigit():
        return int(value)
    return None


def input_float(prompt):
    value = input(prompt).strip()
    # Allow digits + one decimal point
    if value.replace('.', '', 1).isdigit():
        return float(value)
    return None


# adding

def add_medicine():
    print("\n--- ADD NEW MEDICINE ---")

    name = input("Enter medicine name: ").strip().title()

    # Unique batch number
    while True:
        batch_str = input("Enter batch number: ").strip()
        if not batch_str.isdigit():
            print("Batch number must be a number.")
            continue

        batch_no = int(batch_str)

        if find_by_batch(batch_no):
            print("This batch number already exists. Try a different one.")
        else:
            break

    company = input("Enter company name: ").strip().title()

    quantity = input_int("Enter quantity: ")
    if quantity is None or quantity <= 0:
        print("Invalid quantity. Must be a positive number.")
        return

    price = input_float("Enter price: ")
    if price is None or price <= 0:
        print("Invalid price. Must be a positive number.")
        return

    expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()

    new_item = {
        "name": name,
        "batch_no": batch_no,
        "company": company,
        "quantity": quantity,
        "price": price,
        "expiry": expiry
    }

    inventory.append(new_item)
    print("Medicine '{name}' (Batch {batch_no}) added successfully.")


# update

def update_quantity():
    print("\n--- UPDATE MEDICINE QUANTITY ---")

    batch_no = input_int("Enter batch number to update: ")
    if batch_no is None:
        print("Invalid input.")
        return

    record = find_by_batch(batch_no)
    if not record:
        print("No medicine found with this batch number.")
        return

    new_qty = input_int(f"Current quantity: {record['quantity']}. Enter new quantity: ")
    if new_qty is None or new_qty < 0:
        print("Invalid quantity.")
        return

    record["quantity"] = new_qty
    print(f"Quantity updated for Batch {batch_no}.")


#order

def order_medicine():
    print("\n--- ORDER MEDICINE ---")

    batch_no = input_int("Enter batch number to order: ")
    if batch_no is None:
        print("Invalid input.")
        return

    record = find_by_batch(batch_no)
    if not record:
        print("Batch not found.")
        return

    print(f"Available stock for {record['name']}: {record['quantity']}")

    qty = input_int("Enter quantity to order: ")
    if qty is None or qty <= 0:
        print("Invalid quantity.")
        return

    if qty > record["quantity"]:
        print("Insufficient stock. Order cannot be placed.")
        return

    total_amount = qty * record["price"]
    record["quantity"] -= qty

    print("\n--- ORDER SUMMARY ---")
    print(f"Medicine     : {record['name']}")
    print(f"Batch Number : {batch_no}")
    print(f"Quantity     : {qty}")
    print(f"Unit Price   : Rs. {record['price']}")
    print(f"Total Amount : Rs. {total_amount}")
    print(f"Remaining Stock: {record['quantity']}")


#delete
def delete_medicine():
    print("\n--- DELETE MEDICINE RECORD ---")

    batch_no = input_int("Enter batch number to delete: ")
    if batch_no is None:
        print("Invalid input.")
        return

    original_size = len(inventory)
    inventory[:] = [item for item in inventory if item["batch_no"] != batch_no]

    if len(inventory) < original_size:
        print("Record deleted successfully.")
    else:
        print("Batch number not found.")


# display

def display_inventory():
    print("\n--- CURRENT INVENTORY ---")

    if not inventory:
        print("No medicine records found.")
        return

    print("-" * 70)
    print(f"{'BATCH':<8} | {'NAME':<20} | {'COMPANY':<15} | {'QTY':<5} | {'PRICE':<7} | EXPIRY")
    print("-" * 70)

    for item in inventory:
        print(f"{item['batch_no']:<8} | "
              f"{item['name']:<20} | "
              f"{item['company']:<15} | "
              f"{item['quantity']:<5} | "
              f"{item['price']:<7.2f} | "
              f"{item['expiry']}")

    print("-" * 70)
    print(f"Total Records: {len(inventory)}")


#main

def main():
    # Optional starter data
    inventory.extend([
        {"name": "PainRelief", "batch_no": 101, "company": "HealthCorp", "quantity": 200, "price": 2.5, "expiry": "2025-05-10"},
        {"name": "ColdCure",   "batch_no": 102, "company": "Medico",     "quantity": 120, "price": 1.9, "expiry": "2024-12-15"}
    ])

    while True:
        print("\n==============================")
        print("   PHARMACY INVENTORY MENU   ")
        print("==============================")
        print("1. Add Medicine")
        print("2. Update Quantity")
        print("3. Order Medicine (Sale)")
        print("4. Delete Record")
        print("5. View Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_medicine()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            order_medicine()
        elif choice == "4":
            delete_medicine()
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1–6.")


if __name__ == "__main__":
    main()
