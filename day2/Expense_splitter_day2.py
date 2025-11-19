import streamlit as st

st.set_page_config(page_title="Expense Splitter", page_icon="💸", layout="centered")

st.title("💸 Expense Splitter App")

st.write("Split expenses equally among a group of people!")

# Input: Total amount & number of people
total_amount = st.number_input("Enter Total Amount (₹)", min_value=1.0, step=1.0)
num_people = st.number_input("Number of People", min_value=1, step=1)

if num_people > 0:
    st.subheader("Enter Names and Paid Amounts")
    
    people = []
    paid_amounts = []
    
    for i in range(num_people):
        cols = st.columns(2)
        name = cols[0].text_input(f"Name of person {i+1}")
        paid = cols[1].number_input(f"Amount paid by {name or f'Person {i+1}'}", min_value=0.0, step=1.0)
        
        people.append(name)
        paid_amounts.append(paid)

    if st.button("Calculate Split"):
        
        if all(name.strip() for name in people):
            equal_share = total_amount / num_people

            st.info(f"Each person should pay: **₹{equal_share:.2f}**")

            st.subheader("Settlement Summary")
            results = []
            
            for name, paid in zip(people, paid_amounts):
                balance = paid - equal_share
                
                if balance > 0:
                    results.append(f"🟢 **{name} should receive ₹{balance:.2f}**")
                elif balance < 0:
                    results.append(f"🔴 **{name} owes ₹{-balance:.2f}**")
                else:
                    results.append(f"⚪ **{name} is settled**")

            for r in results:
                st.write(r)

        else:
            st.error("Please enter all names before calculating.")
