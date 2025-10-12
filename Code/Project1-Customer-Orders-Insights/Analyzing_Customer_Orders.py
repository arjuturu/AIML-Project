from collections import defaultdict
from collections import Counter

#customer names
customerNamesList = ["Amar","Kalpana","Anwika","Ramu","Raju","Jeevan"];
#print(customerNamesList)
allCustomerOrders = [
    ("Amar", "Fridge", 112, "Home Essentials"),
    ("Kalpana", "Phone", 563, "Electronics"),
    ("Anwika", "Frock", 5, "Clothing"),
    ("Ramu", "Laptop", 732, "Electronics"),
    ("Jeevan", "Phone", 665, "Electronics"),
    ("Raju", "Pant", 18, "Clothing"),
    ("Amar", "Fridge", 135, "Home Essentials"),
    ("Kalpana", "Smartphone", 619, "Electronics"),
    ("Anwika", "Dress", 16, "Clothing"),
    ("Ramu", "Laptop", 698, "Electronics"),
    ("Raju", "Jeans", 10, "Clothing"),
    ("Jeevan", "Washing Machine", 247, "Home Essentials"),
    ("Amar", "Microwave", 95, "Home Essentials"),
    ("Kalpana", "Headphones", 33, "Electronics"),
    ("Anwika", "Skirt", 10, "Clothing"),
    ("Ramu", "Tablet", 281, "Electronics"),
    ("Raju", "T-Shirt", 7, "Clothing"),
    ("Jeevan", "Air Conditioner", 394, "Home Essentials"),
    ("Amar", "Smartwatch", 135, "Electronics"),
    ("Kalpana", "Saree", 28, "Clothing"),
    ("Anwika", "Mixer Grinder", 45, "Home Essentials"),
    ("Ramu", "Bluetooth Speaker", 50, "Electronics"),
    ("Raju", "Kurta", 8, "Clothing"),
    ("Jeevan", "Vacuum Cleaner", 87, "Home Essentials"),
    ("Amar", "LED TV", 338, "Electronics"),
    ("Kalpana", "Blouse", 13, "Clothing"),
    ("Rana", "Blouse", 13, "Clothing")
]

def print_dict(title, data):
    print(f"\n{title}")
    for key, value in data.items():
        print(f"---> {key}: {value}")

# Use a dictionary where keys are customer names and values are lists of ordered products

def group_orders_by_customers(orders):
    customer_orders = defaultdict(list)
    for name, product, price, category in orders:
            customer_orders[name].append((product, price, category))
    return customer_orders
# 1. Group orders by customers
customers_ordered_products = group_orders_by_customers(allCustomerOrders)
print_dict("customersOrderedProducts",customers_ordered_products)

#2. Classify products by category

def classify_products_by_category(orders):
    category_products = defaultdict(set)
    for _, product, _, category in orders:
        category_products[category].add(product)
    return {category: list(products) for category, products in category_products.items()}
products_by_categroy = classify_products_by_category(allCustomerOrders)
print_dict("products_by_categroy",products_by_categroy)

# 3. Analyze customer orders

def categorize_customer_by_purchases(customers_ordered_products):
    customer_category = defaultdict(set)
    for name, customer_orders in customers_ordered_products.items():
        total = sum(price for _, price, _ in customer_orders)
        if total > 100:
            label = "High-Value Buyer"
        elif total > 50:
            label = "Moderate-Value Buyer"
        else:
            label = "Low-Value Buyer"
        customer_category[name] = (total, label)
    return customer_category

customers_by_category = categorize_customer_by_purchases(customers_ordered_products)
print_dict("customers_by_category",customers_by_category)


# print("\nGenerate business insights")

# #4.1 Calculate the total revenue per product category and store it in a dictionary

def calculate_revenure_per_category(customers_ordered_products):
    total_revenue_by_category = defaultdict(int)
    for orders in customers_ordered_products.values():
        for _, price, category in orders:
            total_revenue_by_category[category] += price
    return dict(total_revenue_by_category)
total_revenue_by_category = calculate_revenure_per_category(customers_ordered_products)
print_dict("total_revenue_by_category",total_revenue_by_category)

# # • Extract unique products from all orders using a set
def extract_unique_products(customers_ordered_products):
    products_count = Counter()
    for customers_orders in customers_ordered_products.values():
        for product, _, _ in customers_orders:
            products_count[product] += 1
    return dict(products_count)
unique_products = extract_unique_products(customers_ordered_products)
print_dict("unique_products",unique_products)

# # • Use a list comprehension to find all customers who purchased electronics
def find_customers_who_purchased_electronics(customers_orders):
    electronics_customers = [name for name, orders in customers_orders.items() if any(category == "Electronics" for _, _, category in orders)]
    return electronics_customers
customer_purchased_only_electronics = find_customers_who_purchased_electronics(customers_ordered_products)
print("customer_purchased_only_electronics",customer_purchased_only_electronics)


# # • Identify the top three highest-spending customers using sorting
def top_spenders(classification, top_n=3):
    return sorted(classification.items(), key=lambda x: x[1][0], reverse=True)[:top_n]
top_spenderss = top_spenders(customers_by_category,3)
print("top_spenders",top_spenderss)


# # • Print a summary of each customer’s total spending and their classification
print_dict("customers_by_category",customers_by_category)


# # • Use set operations to find customers who purchased from multiple categories
def customers_purchased_from_multiple_categories(customer_orders):
    customers_multiple_categories = {}
    for name, orders in customer_orders.items():
        categories = {category for _, _, category in orders}
        if len(categories) > 1:
            customers_multiple_categories[name] = categories
    return customers_multiple_categories
customers_multiple_categories = customers_purchased_from_multiple_categories(customers_ordered_products)
print_dict("customers_multiple_categories",customers_multiple_categories)


# # • Identify common customers who bought both electronics and clothing
def customers_who_bought_electronics_and_clothing(customers_orders):
    required = {"Clothing", "Electronics"}
    common_customers = {}
    for name, orders in customers_orders.items():
        categories = {category for _, _, category in orders}
        if required.issubset(categories):
            common_customers[name] = categories
    return common_customers
customers_who_bought_both = customers_who_bought_electronics_and_clothing(customers_ordered_products)
print_dict("customers_who_bought_both",customers_who_bought_both)

        
# #Identify trends based on category-wise sales 
def category_wise_sales_trends(orders):
    category_sales = defaultdict(int)
    for _, _, price, category in orders:
        category_sales[category] += price
    return dict(category_sales)
category_sales_trends = category_wise_sales_trends(allCustomerOrders)
print_dict("category_sales_trends",category_sales_trends)

# # Most frequently purchased products
def most_frequently_bought_products(orders, top_n=1):
    product_list = [order[1] for order in orders]
    product_frequency = Counter(product_list)
    return product_frequency.most_common(top_n)
most_frequent_products = most_frequently_bought_products(allCustomerOrders,1)
print("Most Frequently Purchased Products:")
for product, count in most_frequent_products:
    print(f"- {product}: {count} time(s)")

