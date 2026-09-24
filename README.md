# Banking Analytics Dashboard

A data analytics project that combines Python and Power BI to analyze banking customers, transactions, investments, and branch performance.

The project focuses on data cleaning, data quality validation, exploratory analysis, data modeling, DAX calculations, and interactive dashboard development.

## Project Overview

This project analyzes three related banking datasets:

- Bank branch data
- Customer data
- Transaction data

Python was used to clean and validate the datasets, investigate data-quality issues, and create additional analytical columns.

Power BI was then used to build an interactive four-page dashboard covering:

- Banking overview
- Customer analysis
- Transaction analysis
- Branch analysis

## Business Objective

The main objective of this project is to understand banking customer behavior, transaction activity, investment patterns, and branch-level financial performance.

The analysis aims to answer questions such as:

- How many customers are active based on transaction activity?
- What types of customers and accounts are most common?
- How are transaction and investment amounts distributed?
- How does transaction activity change over time?
- How do revenue and expenses vary across cities and regions?
- Which branches generate higher revenue and calculated profit?
- What data-quality issues need to be considered before analysis?

## Tools & Technologies

- **Python** — Data cleaning, validation, transformation, and analysis
- **Pandas** — Data manipulation and preprocessing
- **NumPy** — Numerical analysis
- **Power BI** — Interactive dashboard development and visualization
- **DAX** — Measures and calculated columns
- **CSV** — Dataset storage
- **GitHub** — Project version control and portfolio

## Dataset

The project uses three related CSV datasets containing banking branch, customer, and transaction information.

### 1. Bank Data

Contains branch-level information such as:

- Branch ID
- City
- Region
- Firm Revenue
- Expenses
- Profit Margin

**Records:** 1,000 branches

### 2. Customer Data

Contains customer-level information such as:

- Customer ID
- Age
- Customer Type
- City
- Region
- Bank Name
- Branch ID

**Records:** 10,000 customers

### 3. Transaction Data

Contains transaction and investment information such as:

- Transaction ID
- Customer ID
- Account Type
- Total Balance
- Transaction Amount
- Investment Amount
- Investment Type
- Transaction Date

**Records:** 10,000 transactions

### Data Period

Transaction records cover the period from **March 21, 2022 to March 20, 2025**.

## Python Data Cleaning & Validation

Python was used as the first stage of the project to inspect, clean, validate, and prepare the datasets before importing them into Power BI.

### Data Quality Checks

The following checks were performed:

- Checked missing values
- Checked duplicate rows
- Verified unique IDs
- Validated customer-to-transaction relationships
- Validated customer-to-branch relationships
- Checked transaction date ranges
- Examined categorical distributions
- Reviewed numerical statistics
- Investigated the provided profit margin values

### Data Cleaning

#### Customer Data

- Filled missing `Customer_Type` values with `Unknown`
- Filled missing `City` values with `Unknown`
- Created `Age_Group`
- Created `Age_Group_Sort` to support correct ordering in Power BI
- Missing age values were retained rather than artificially filled

#### Transaction Data

- Converted `Transaction_Date` to datetime
- Created `Year`
- Created `Month`
- Created `Month_Name`

#### Bank Data

Created additional calculated fields:

- `Calculated_Profit`
- `Calculated_Profit_Margin`
- `Margin_Difference`

### Data Quality Findings

The validation identified:

- 0 duplicate rows across the three datasets
- 0 invalid customer IDs in transaction data
- 0 invalid branch IDs in customer data
- 50 missing firm revenue values
- 500 missing customer ages
- 500 missing customer types
- 500 missing customer cities

### Profit Margin Investigation

The source `Profit_Margin` column was compared with the standard calculation:

`(Firm Revenue - Expenses) / Firm Revenue × 100`

The calculated values did not match the provided source values. Therefore, the original `Profit_Margin` column was retained rather than overwritten, while separate calculated fields were created for comparison and analysis.


## Power BI Data Model & DAX

After cleaning the datasets with Python, the cleaned data was imported into Power BI for modeling and visualization.

### Data Model

The project uses three related tables:

- `bank_cleaned`
- `customer_cleaned`
- `transaction_cleaned`

The relationships are:

- `bank_cleaned[Branch_ID]` → `customer_cleaned[Branch_ID]`
- `customer_cleaned[Customer_ID]` → `transaction_cleaned[Customer_ID]`

Both relationships use a **one-to-many (1:*)** relationship with single-direction filtering.

### DAX Measures

Several DAX measures were created to support the dashboard analysis, including:

- Total Customers
- Total Transactions
- Total Transaction Amount
- Total Investment
- Active Customers
- Inactive Customers
- Average Customer Age
- Average Transaction Amount
- Average Investment Amount
- Total Branches
- Total Revenue
- Total Expenses
- Total Calculated Profit
- Average Profit Margin

### Calculated Columns

Additional calculated columns were created in Power BI for analysis and visualization:

- `Age_Group`
- `Age_Group_Sort`
- `Customer Status`

The `Age_Group_Sort` column was used to display age groups in the correct order from **18-29** through **70-79**.

## Power BI Dashboard

The final Power BI dashboard consists of four interactive pages, each focusing on a different area of the banking data.

### 1. Banking Analytics Dashboard

Provides an overall view of the banking data.

Key analysis includes:

- Total customers
- Total transactions
- Total transaction amount
- Total investment
- Customer type distribution
- Customer age groups
- Customer distribution by city and region
- Account type analysis
- Investment type analysis
- Transaction trends over time
- Branch revenue vs expenses by city

### 2. Customer Analysis

Focuses on customer behavior and activity.

Key analysis includes:

- Active customers
- Inactive customers
- Average customer age
- Average transaction amount
- Customer type distribution
- Customer distribution by city
- Transaction amount by customer type
- Active vs inactive customer analysis

### 3. Transaction Analysis

Focuses on transaction and investment activity.

Key analysis includes:

- Total transactions
- Average transaction amount
- Average investment amount
- Transaction amount trends
- Transaction amount by account type
- Investment amount by investment type
- Transaction count by account type
- Yearly transaction trends
- Monthly transaction trends
- Transaction amount by region
- Transaction count by region
- Transaction amount by customer type

### 4. Branch Analysis

Focuses on branch-level financial performance.

Key analysis includes:

- Total branches
- Total revenue
- Total expenses
- Total calculated profit
- Average profit margin
- Revenue vs expenses by city
- Profit by city
- Revenue and expenses by region
- Branch count by region
- Profit margin by region
- Top 10 branches by revenue
- Top 10 branches by calculated profit

## Key Insights

The analysis produced several notable findings:

- The dataset contains **10,000 customers** and **10,000 transactions** across **1,000 branches**.
- **6,335 customers** were identified as active based on transaction activity, representing approximately **63.35%** of the customer base.
- The average customer age is approximately **48.75 years**.
- The average transaction amount is approximately **2,542.71**.
- The average investment amount is approximately **25,550.25**.
- **2024** recorded the highest number of transactions with **3,388 transactions**. The 2025 data represents only a partial year and should therefore not be directly compared with full-year values.
- Customer types are relatively balanced across **Business, Employee, and Individual** customers.
- Transaction activity and investment amounts vary across account types, investment types, cities, regions, and customer segments.
- Branch-level analysis shows differences in revenue, expenses, calculated profit, and profit margin across cities and regions.
- The top-performing branches by revenue and calculated profit were identified using Power BI Top N analysis.
- Data validation revealed missing values in customer age, customer type, customer city, and branch firm revenue.
- The provided source `Profit_Margin` values did not match the standard profit-margin calculation, so the original values were preserved and separate calculated fields were created for comparison.

## Project Structure

```text
Banking_Analytics_Project/
│
├── data/
│   ├── raw/
│   │   ├── bank_data.csv
│   │   ├── customer_data.csv
│   │   └── transaction_data.csv
│   │
│   ├── bank_cleaned.csv
│   ├── customer_cleaned.csv
│   └── transaction_cleaned.csv
│
├── bank_analysis.py
├── Banking_Analytics.pbix
└── README.md

## Conclusion

This project demonstrates an end-to-end data analytics workflow, starting from raw banking data and ending with an interactive Power BI dashboard.

Python was used for data cleaning, validation, transformation, and data-quality investigation, while Power BI was used for data modeling, DAX calculations, and interactive visualization.

The project helped analyze customer behavior, transaction activity, investment patterns, and branch-level financial performance while also highlighting important data-quality considerations.

Overall, the project demonstrates practical skills in **Python, Pandas, data cleaning, data validation, Power BI, data modeling, DAX, and data visualization**.