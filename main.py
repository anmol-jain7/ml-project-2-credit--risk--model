import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked

# Page config
st.set_page_config(
    page_title="Lauki Finance: Credit Risk Modelling",
    page_icon="📊",
    layout="wide"
)

# Sidebar theme switcher
with st.sidebar:
    st.markdown("### Choose Theme")
    st.radio(" ", ["Dark", "Light"], index=0, key="theme_choice")

# Title
st.markdown("<h1 style='text-align: center;'>📊 Lauki Finance: Credit Risk Modelling</h1>", unsafe_allow_html=True)
st.markdown("---")

# Input Rows
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Row 1
with row1[0]:
    age = st.number_input('Age', min_value=18, max_value=100, format="%d")
with row1[1]:
    income = st.number_input('Income (Annual ₹)', min_value=0, format="%d")
with row1[2]:
    loan_amount = st.number_input('Loan Amount (₹)', min_value=0, format="%d")

# Row 2
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.metric("Loan to Income Ratio", f"{loan_to_income_ratio:.2f}")
with row2[1]:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, format="%d")
with row2[2]:
    avg_dpd_per_delinquency = st.number_input('Average DPD', min_value=0, format="%d")

# Row 3
with row3[0]:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, format="%d")
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, format="%d")
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, format="%d")

# Row 4 - Dropdowns with 'Select' placeholders
with row4[0]:
    residence_type = st.selectbox('Residence Type', ['Select', 'Owned', 'Rented', 'Mortgage'])
with row4[1]:
    loan_purpose = st.selectbox('Loan Purpose', ['Select', 'Education', 'Home', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox('Loan Type', ['Select', 'Unsecured', 'Secured'])

st.markdown("### ")
if st.button('🚀 Calculate Risk'):
    # Validation
    if not all([age, income, loan_amount, loan_tenure_months,
                avg_dpd_per_delinquency, delinquency_ratio,
                credit_utilization_ratio, num_open_accounts]) \
        or residence_type == "Select" or loan_purpose == "Select" or loan_type == "Select":
        st.error("❗ Please fill in all the fields before calculating risk.")
    else:
        # Prediction
        probability, credit_score, rating = predict(
            age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

        st.success("✅ Risk Assessment Complete")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("🧾 **Default Probability**")
            st.markdown(f"<h3>{probability:.2%}</h3>", unsafe_allow_html=True)
        with col2:
            st.markdown("📊 **Credit Score**")
            st.markdown(f"<h3>{credit_score}</h3>", unsafe_allow_html=True)
        with col3:
            st.markdown("🔍 **Rating**")
            st.markdown(f"<h3>{rating}</h3>", unsafe_allow_html=True)

        st.markdown("---")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
footer_html = """
<style>
.footer {
    font-size: 0.85em;
    text-align: center;
    color: grey;
    padding-top: 10px;
}
</style>
<div class="footer">
    © 2025 <strong>Lauki Finance</strong> · All rights reserved.
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
