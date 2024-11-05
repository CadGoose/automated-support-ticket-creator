python
Copy code
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import random

def generate_ticket_id():
    """Generate a unique ticket ID."""
    return f"Ticket-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"

def send_email(ticket):
    """Send an email notification to the appropriate department."""
    # Email configuration (replace these with actual email credentials)
    SMTP_SERVER = 'smtp.yourmail.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'your_email@domain.com'
    SENDER_PASSWORD = 'your_email_password'
    
    # Department emails
    department_emails = {
        "Technical Support": "techsupport@domain.com",
        "Sales": "sales@domain.com",
        "Customer Service": "customerservice@domain.com"
    }
    
    # Get the recipient email based on the department
    recipient_email = department_emails.get(ticket['Department'], SENDER_EMAIL)
    
    # Email content
    subject = f"New Support Ticket: {ticket['Ticket ID']}"
    body = "\n".join([f"{key}: {value}" for key, value in ticket.items()])
    
    # Set up email message
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        print("\nNotification email sent successfully to the appropriate department!")
    except Exception as e:
        print(f"Failed to send email notification: {e}")

def create_support_ticket():
    """Main function to gather ticket information and generate a ticket."""
    print("Welcome to the Automated Support Ticket Generator!")
    
    # Step 1: Choose Department
    print("\nWhich department are you trying to reach?")
    departments = {
        "1": "Technical Support",
        "2": "Sales",
        "3": "Customer Service"
    }
    for key, value in departments.items():
        print(f"{key}. {value}")
    dept_choice = input("Enter the department number (1-3): ")
    department = departments.get(dept_choice, "Customer Service")  # Default to Customer Service

    # Step 2: Choose Issue Type Based on Department
    if department == "Technical Support":
        print("\nWhat type of issue are you experiencing?")
        tech_issues = {
            "1": "Connection Issue",
            "2": "Broken Device",
            "3": "No Power",
            "4": "Software Issue"
        }
        for key, value in tech_issues.items():
            print(f"{key}. {value}")
        issue_choice = input("Enter the issue type number (1-4): ")
        issue_type = tech_issues.get(issue_choice, "Other Technical Issue")

    elif department == "Sales":
        print("\nWhat do you need help with?")
        sales_issues = {
            "1": "Product Inquiry",
            "2": "Pricing Information",
            "3": "Bulk Order",
            "4": "Other Sales Inquiry"
        }
        for key, value in sales_issues.items():
            print(f"{key}. {value}")
        issue_choice = input("Enter the issue type number (1-4): ")
        issue_type = sales_issues.get(issue_choice, "Other Sales Inquiry")

    elif department == "Customer Service":
        print("\nWhat can we assist you with?")
        customer_service_issues = {
            "1": "Order Status",
            "2": "Return/Exchange",
            "3": "Account Assistance",
            "4": "Other Customer Service Inquiry"
        }
        for key, value in customer_service_issues.items():
            print(f"{key}. {value}")
        issue_choice = input("Enter the inquiry type number (1-4): ")
        issue_type = customer_service_issues.get(issue_choice, "Other Customer Service Inquiry")

    # Step 3: Get Description of the Issue
    description = input("\nPlease provide a brief description of your issue: ")

    # Step 4: Set Priority Level
    print("\nSelect the priority level of your issue:")
    print("1. Low\n2. Medium\n3. High")
    priority_choice = input("Enter the priority number (1-3): ")
    priority_levels = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priority_levels.get(priority_choice, "Medium")  # Default to Medium if input is invalid

    # Generate ticket ID and set current date
    ticket_id = generate_ticket_id()
    creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Assemble the ticket information
    ticket = {
        "Ticket ID": ticket_id,
        "Creation Date": creation_date,
        "Department": department,
        "Issue Type": issue_type,
        "Description": description,
        "Priority": priority,
        "Status": "Open"
    }

    # Display the generated ticket
    print("\nSupport Ticket Created Successfully!")
    print("-" * 40)
    for key, value in ticket.items():
        print(f"{key}: {value}")
    print("-" * 40)

    # Send the email notification
    send_email(ticket)

# Main script execution
if __name__ == "__main__":
    create_support_ticket()
