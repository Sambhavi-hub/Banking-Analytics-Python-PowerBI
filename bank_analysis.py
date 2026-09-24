import pandas as pd

# File paths
bank_file = "data/raw/bank_data.csv"
customer_file = "data/raw/customer_data.csv"
transaction_file = "data/raw/transaction_data.csv"

# Load datasets
bank_df = pd.read_csv(bank_file)
customer_df = pd.read_csv(customer_file)
transaction_df = pd.read_csv(transaction_file)

# Basic information
print("\n========== BANK DATA ==========")
print("Shape:", bank_df.shape)
print("\nColumns:")
print(bank_df.columns.tolist())
print("\nFirst 5 rows:")
print(bank_df.head())

print("\n========== CUSTOMER DATA ==========")
print("Shape:", customer_df.shape)
print("\nColumns:")
print(customer_df.columns.tolist())
print("\nFirst 5 rows:")
print(customer_df.head())

print("\n========== TRANSACTION DATA ==========")
print("Shape:", transaction_df.shape)
print("\nColumns:")
print(transaction_df.columns.tolist())
print("\nFirst 5 rows:")
print(transaction_df.head())

# ==========================================
# DATA QUALITY CHECK
# ==========================================

print("\n\n========== DATA QUALITY CHECK ==========")

# Missing values
print("\n--- Missing Values ---")

print("\nBank Data:")
print(bank_df.isnull().sum())

print("\nCustomer Data:")
print(customer_df.isnull().sum())

print("\nTransaction Data:")
print(transaction_df.isnull().sum())


# Duplicate rows
print("\n--- Duplicate Rows ---")

print("Bank duplicates:", bank_df.duplicated().sum())
print("Customer duplicates:", customer_df.duplicated().sum())
print("Transaction duplicates:", transaction_df.duplicated().sum())


# Unique IDs
print("\n--- Unique IDs ---")

print("Unique Branch IDs:", bank_df["Branch_ID"].nunique())
print("Unique Customer IDs:", customer_df["Customer_ID"].nunique())
print("Unique Transaction IDs:", transaction_df["Transaction_ID"].nunique())


# Customer transactions
print("\n--- Customer Transaction Check ---")

transactions_per_customer = transaction_df["Customer_ID"].value_counts()

print("Customers with transactions:",
      transactions_per_customer.count())

print("Maximum transactions for one customer:",
      transactions_per_customer.max())


# Branch relationship check
print("\n--- Branch Relationship Check ---")

customer_branches = set(customer_df["Branch_ID"].dropna())
bank_branches = set(bank_df["Branch_ID"].dropna())

missing_branches = customer_branches - bank_branches

print("Customer branch IDs not found in bank data:",
      len(missing_branches))


# Transaction dates
print("\n--- Transaction Date Range ---")

transaction_df["Transaction_Date"] = pd.to_datetime(
    transaction_df["Transaction_Date"]
)

print("Earliest transaction:",
      transaction_df["Transaction_Date"].min())

print("Latest transaction:",
      transaction_df["Transaction_Date"].max())

      # ==========================================
# FURTHER DATA INVESTIGATION
# ==========================================

print("\n\n========== FURTHER DATA INVESTIGATION ==========")

# Customer type distribution
print("\n--- Customer Type Distribution ---")
print(customer_df["Customer_Type"].value_counts(dropna=False))


# City distribution
print("\n--- City Distribution ---")
print(customer_df["City"].value_counts(dropna=False))


# Age statistics
print("\n--- Age Statistics ---")
print(customer_df["Age"].describe())


# Bank revenue statistics
print("\n--- Firm Revenue Statistics ---")
print(bank_df["Firm_Revenue"].describe())


# Check transaction customers exist in customer table
print("\n--- Transaction Customer Relationship ---")

transaction_customers = set(transaction_df["Customer_ID"])
customer_ids = set(customer_df["Customer_ID"])

missing_customers = transaction_customers - customer_ids

print("Transaction Customer IDs not found in customer data:",
      len(missing_customers))


# Account types
print("\n--- Account Types ---")
print(transaction_df["Account_Type"].value_counts())


# Investment types
print("\n--- Investment Types ---")
print(transaction_df["Investment_Type"].value_counts())


# Check numeric statistics
print("\n--- Transaction Statistics ---")
print(
    transaction_df[
        ["Total_Balance", "Transaction_Amount", "Investment_Amount"]
    ].describe()
)


# Check unusual profit margins
print("\n--- Profit Margin Check ---")
print("Minimum profit margin:",
      bank_df["Profit_Margin"].min())

print("Maximum profit margin:",
      bank_df["Profit_Margin"].max())

print("Negative profit margins:",
      (bank_df["Profit_Margin"] < 0).sum())

# ==========================================
# PROFIT MARGIN VALIDATION
# ==========================================

print("\n\n========== PROFIT MARGIN VALIDATION ==========")

# Calculate profit margin ourselves
bank_df["Calculated_Profit_Margin"] = (
    (bank_df["Firm_Revenue"] - bank_df["Expenses"])
    / bank_df["Firm_Revenue"]
) * 100

# Compare original vs calculated
bank_df["Margin_Difference"] = (
    bank_df["Profit_Margin"]
    - bank_df["Calculated_Profit_Margin"]
)

print("\n--- Profit Margin Comparison ---")

print(
    bank_df[
        [
            "Firm_Revenue",
            "Expenses",
            "Profit_Margin",
            "Calculated_Profit_Margin",
            "Margin_Difference"
        ]
    ].head(10)
)

# How different are they?
print("\n--- Difference Statistics ---")

print(
    bank_df["Margin_Difference"].describe()
)

# Count values that are approximately equal
close_values = (
    bank_df["Margin_Difference"].abs() < 0.01
).sum()

print("\nValues matching calculated margin:",
      close_values)

print("Total rows with revenue:",
      bank_df["Firm_Revenue"].notna().sum())

# ==========================================
# DATA CLEANING
# ==========================================

print("\n\n========== DATA CLEANING ==========")

# ----- CUSTOMER DATA -----

# Fill categorical missing values
customer_df["Customer_Type"] = customer_df["Customer_Type"].fillna("Unknown")
customer_df["City"] = customer_df["City"].fillna("Unknown")

# Create age groups
customer_df["Age_Group"] = pd.cut(
    customer_df["Age"],
    bins=[17, 29, 39, 49, 59, 69, 79],
    labels=[
        "18-29",
        "30-39",
        "40-49",
        "50-59",
        "60-69",
        "70-79"
    ]
)

# Give missing ages their own category
customer_df["Age_Group"] = customer_df["Age_Group"].cat.add_categories("Unknown")
customer_df["Age_Group"] = customer_df["Age_Group"].fillna("Unknown")

# Sort order for Age Groups
age_order = {
    "18-29": 1,
    "30-39": 2,
    "40-49": 3,
    "50-59": 4,
    "60-69": 5,
    "70-79": 6,
    "Unknown": 7
}

customer_df["Age_Group_Sort"] = customer_df["Age_Group"].map(age_order)

# ----- TRANSACTION DATA -----

# Convert transaction date to datetime
transaction_df["Transaction_Date"] = pd.to_datetime(
    transaction_df["Transaction_Date"]
)

# Create useful date columns
transaction_df["Year"] = transaction_df["Transaction_Date"].dt.year
transaction_df["Month"] = transaction_df["Transaction_Date"].dt.month
transaction_df["Month_Name"] = transaction_df["Transaction_Date"].dt.month_name()


# ----- BANK DATA -----

# Create calculated profit amount
bank_df["Calculated_Profit"] = (
    bank_df["Firm_Revenue"] - bank_df["Expenses"]
)

# Create calculated profit margin
bank_df["Calculated_Profit_Margin"] = (
    bank_df["Calculated_Profit"]
    / bank_df["Firm_Revenue"]
) * 100


# ==========================================
# SAVE CLEANED DATA
# ==========================================

customer_df.to_csv(
    "data/customer_cleaned.csv",
    index=False
)

transaction_df.to_csv(
    "data/transaction_cleaned.csv",
    index=False
)

bank_df.to_csv(
    "data/bank_cleaned.csv",
    index=False
)

print("\nCleaned datasets saved successfully!")

# ==========================================
# VALIDATE CLEANED DATA
# ==========================================

print("\n\n========== CLEANED DATA VALIDATION ==========")

# ----- MISSING VALUES -----

print("\n--- Bank Missing Values ---")
print(bank_df.isnull().sum())

print("\n--- Customer Missing Values ---")
print(customer_df.isnull().sum())

print("\n--- Transaction Missing Values ---")
print(transaction_df.isnull().sum())


# ----- SHAPES -----

print("\n--- Dataset Shapes ---")
print("Bank:", bank_df.shape)
print("Customer:", customer_df.shape)
print("Transaction:", transaction_df.shape)


# ----- DATA TYPES -----

print("\n--- Customer Data Types ---")
print(customer_df.dtypes)

print("\n--- Transaction Data Types ---")
print(transaction_df.dtypes)

print("\n--- Bank Data Types ---")
print(bank_df.dtypes)


# ----- NEW COLUMNS -----

print("\n--- New Columns ---")

print("Customer Age_Group:")
print(customer_df["Age_Group"].value_counts(dropna=False))

print("\nTransaction Years:")
print(transaction_df["Year"].value_counts().sort_index())

print("\nTransaction Months:")
print(transaction_df["Month"].value_counts().sort_index())


print("\n========== VALIDATION COMPLETE ==========")