# Step 1: Import required libraries
import streamlit as st
import pandas as pd

# Step 2: Configure Streamlit page
st.set_page_config(page_title="Non-Veg Restaurant Billing", layout="centered")

# Step 3: Define categorized menu
menu = {
    "Rice": {
        "Veg Fried Rice": 120,
        "Chicken Fried Rice": 160,
        "Egg Fried Rice": 140,
        "Mutton Biryani": 220,
        "Chicken Biryani": 180
    },
    "Starters": {
        "Paneer Tikka": 150,
        "Chicken Lollipop": 180,
        "Fish Fingers": 200,
        "Veg Manchurian": 130
    },
    "Main Course": {
        "Butter Chicken": 220,
        "Chicken Curry": 200,
        "Mutton Rogan Josh": 250,
        "Dal Tadka": 120,
        "Paneer Butter Masala": 180
    },
    "Beverages": {
        "Coke": 50,
        "Lassi": 60,
        "Fresh Lime Soda": 40,
        "Water Bottle": 20
    }
}

# Step 4: App header
st.title("🍛 Non-Veg Restaurant Order & Billing App")
st.write("Select your items below to generate your bill.")

# Step 5: Optional customer info
with st.expander("🧑 Customer Info (Optional)"):
    customer_name = st.text_input("Customer Name")
    table_number = st.text_input("Table Number")

# Step 6: Create selection form
with st.form("order_form"):
    quantities = {}
    st.subheader("📝 Select Items")

    for category, items in menu.items():
        st.markdown(f"### 🍽️ {category}")
        for item, price in items.items():
            quantities[item] = st.number_input(f"{item} (₹{price})", min_value=0, step=1)

    tax_rate = st.slider("GST (%)", min_value=0, max_value=18, value=5)
    discount_rate = st.slider("Discount (%)", min_value=0, max_value=50, value=0)
    submitted = st.form_submit_button("Generate Bill")

# Step 7: Calculate and display bill
if submitted:
    bill_items = []
    subtotal = 0

    for item, qty in quantities.items():
        if qty > 0:
            item_total = qty * [price for cat in menu.values() for name, price in cat.items() if name == item][0]
            bill_items.append([item, qty, item_total // qty, item_total])
            subtotal += item_total

    tax_amount = subtotal * (tax_rate / 100)
    discount_amount = subtotal * (discount_rate / 100)
    total = subtotal + tax_amount - discount_amount

    # Step 8: Show invoice
    st.subheader("🧾 Final Invoice")
    if customer_name:
        st.write(f"👤 Customer: {customer_name}")
    if table_number:
        st.write(f"🪑 Table No: {table_number}")

    bill_df = pd.DataFrame(bill_items, columns=["Item", "Quantity", "Unit Price", "Total"])
    st.table(bill_df)

    st.write(f"**Subtotal:** ₹{subtotal:.2f}")
    st.write(f"**GST ({tax_rate}%):** ₹{tax_amount:.2f}")
    st.write(f"**Discount ({discount_rate}%):** -₹{discount_amount:.2f}")
    st.write(f"**Grand Total:** ₹{total:.2f}")

    # Step 9: Download invoice
    csv = bill_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Invoice as CSV",
        data=csv,
        file_name="restaurant_invoice.csv",
        mime="text/csv"
    )
