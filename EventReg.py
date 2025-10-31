# Step 1: Import necessary libraries
import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import uuid
from datetime import datetime

# Step 2: Configure Streamlit page
st.set_page_config(page_title="Event Registration", layout="centered")

# Step 3: Set up the app header
st.title("🎟️ Event Registration System")
st.write("Please fill out the form below to register for the event.")

# Step 4: Create a form for user input
with st.form("registration_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
    with col2:
        email = st.text_input("Email Address")

    ticket_type = st.selectbox(
        "Select Ticket Type",
        ["General Admission", "VIP", "Student Pass", "Group Booking"]
    )

    comments = st.text_area("Any special requests or comments?")
    send_email = st.checkbox("Send me a confirmation email")
    submitted = st.form_submit_button("Register")

# Step 5: Helper function to validate email format
def is_valid_email(email):
    return "@" in email and "." in email

# Step 6: Handle form submission
if submitted:
    if not name or not email:
        st.error("❌ Please fill in all required fields: Name and Email.")
    elif not is_valid_email(email):
        st.error("❌ Please enter a valid email address.")
    else:
        registration_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        registration = {
            "Registration ID": registration_id,
            "Name": name,
            "Email": email,
            "Ticket Type": ticket_type,
            "Comments": comments,
            "Timestamp": timestamp
        }

        file_exists = os.path.isfile("registrations.csv")
        df = pd.DataFrame([registration])
        df.to_csv("registrations.csv", mode='a', header=not file_exists, index=False)

        st.success("✅ Registration Successful!")
        st.write(f"🆔 Registration ID: `{registration_id}`")
        st.write(f"🎫 Ticket Type: {ticket_type}")
        if comments:
            st.write(f"📝 Notes: {comments}")
        if send_email:
            st.write(f"📧 Confirmation will be sent to: {email}")

        # Optional email confirmation
        if send_email:
            try:
                sender_email = "youremail@example.com"
                sender_password = "yourpassword"
                smtp_server = "smtp.example.com"
                smtp_port = 587

                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = email
                msg["Subject"] = "Event Registration Confirmation"

                body = f"""
                Hi {name},

                Thank you for registering for our event!
                Registration ID: {registration_id}
                Ticket Type: {ticket_type}
                Comments: {comments if comments else 'None'}
                Timestamp: {timestamp}

                We look forward to seeing you!

                Best regards,
                Event Team
                """
                msg.attach(MIMEText(body, "plain"))

                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, email, msg.as_string())
                server.quit()

                st.info("📨 Confirmation email sent successfully.")
            except Exception as e:
                st.warning(f"⚠️ Failed to send email: {e}")

# Step 7: Display live registration count and full table
st.subheader("📊 Live Registration Summary")

if os.path.exists("registrations.csv"):
    try:
        reg_df = pd.read_csv("registrations.csv")
        total_count = len(reg_df)
        st.info(f"✅ Total Registrations: {total_count}")

        # Show full registration table
        st.dataframe(reg_df)

        # Download button
        csv = reg_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Registration Data as CSV",
            data=csv,
            file_name="registrations.csv",
            mime="text/csv"
        )
    except pd.errors.ParserError as e:
        st.warning(f"⚠️ Could not read registration data: {e}")
else:
    st.info("📊 Total Registrations: 0")
