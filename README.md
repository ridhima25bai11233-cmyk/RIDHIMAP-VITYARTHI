This Medicine Inventory Management System is a command-line/desktop application designed to efficiently manage the stock of medicines in a pharmacy, clinic, or small hospital. The primary goal is to streamline inventory tracking, reduce manual errors, and provide timely alerts for low stock and expiring items, thereby ensuring effective supply chain management and patient safety.

The program allows users to perform CRUD (Create, Read, Update, Delete) operations on medicine records.

Features
The application provides the following core functionalities:

Add New Medicine: Input details for a new medicine, including name, batch number, manufacturer, quantity, price, and expiry date.

View Inventory: Display a complete list of all medicines currently in stock.

Search Medicine: Quickly find medicine records based on name, batch number, or ID.

Update Stock: Modify the quantity of an existing medicine record (e.g., after a purchase or sale).

Remove Medicine: Delete a record from the inventory.

Low Stock Alert: Automatically flag medicines when their quantity falls below a predefined threshold.

Expiry Alert: Generate a list of medicines nearing their expiration date (e.g., within the next 30/60 days).

Generate Report: Output a summary of the current inventory status (e.g., total stock value, expiring items).
Technologies/Tools Used
Category	Component	Description
Language	[e.g., Python / Java / C++]	The primary programming language used for the application logic.
Environment	[e.g., Visual Studio Code / Eclipse / NetBeans]	The Integrated Development Environment (IDE) used for development.
Version Control	Git/GitHub	Used for tracking changes and hosting the project repository.

Export to Sheets

Steps to Install & Run the Project
Follow these instructions to set up and execute the program locally.

1. Clone the Repository
Open your terminal or command prompt and clone the project:

Bash

git clone [Your Repository URL Here]
cd medicine-inventory-program
2. Set up the Environment
A. Install Dependencies
If using Python:

Bash

pip install -r requirements.txt
(Ensure the requirements.txt file exists and lists all necessary libraries.)

If using Java:

Ensure you have the Java Development Kit (JDK) [version number] installed.

[If necessary, list steps for including external JAR files, such as a database driver (e.g., JDBC connector).]

B. Database Setup
The program uses a [Database Type] database.

The initial database file/schema is located at [Path to Database File/Script, e.g., database/inventory.db].

[If an external database is used:] Create a database named [Database Name] and execute the schema script [Schema Script Name, e.g., create_tables.sql] to set up the necessary tables.

3. Run the Application
For Command-Line Interface (CLI) Applications:

Bash

[Command to execute the main file, e.g., python main.py]
For Compiled Applications (e.g., Java):

Bash

[Command to run the compiled application, e.g., java -jar inventory.jar]
The application should start, presenting the main menu or GUI interface.
Instructions for Testing
To ensure the system is working correctly, perform the following tests:

Basic CRUD Operations:

Add: Add a new medicine record (e.g., "Paracetamol", Qty: 50, Expiry: 2026-10-01). Verify it appears in the View Inventory list.

Update: Update the quantity of the record you just added (e.g., change Qty from 50 to 75). Verify the change is reflected.

Search: Search for the medicine by its name. Verify the single record is returned.

Remove: Delete the record. Verify it is no longer present in the inventory list.

Alert Functionality Testing:

Low Stock: Add a medicine with a quantity below the system's low-stock threshold (e.g., 5). Verify the medicine appears in the Low Stock Alert report.

Expiry Alert: Add a medicine with an expiry date within the next 30 days. Verify this item appears in the Expiry Alert report.

Error Handling:

Attempt to input invalid data types (e.g., text for quantity, or an incorrect date format). Verify that the program handles the input gracefully and displays an appropriate error message instead of crashing.


Conclusion:
This project successfully implements a  simple medicine shop inventory. it demonstrates how user can input,access,delete and search for a particular medicine.
