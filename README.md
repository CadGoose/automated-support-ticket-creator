# Automated-support-ticket-creator
# Automated Support Ticket Generator 📋

## Overview
The **Automated Support Ticket Generator** is a Python script that simplifies the creation of support tickets. It prompts users for information about their issue and generates a formatted ticket that can be used as a template for IT support systems or help desks.

## Features
- **Unique Ticket ID Generation**: Creates a unique ID for each ticket based on the timestamp and a random number.
- **Priority and Category Selection**: Allows users to specify priority (Low, Medium, High) and select the category of the issue.
- **Structured Output**: Generates a support ticket with fields like Ticket ID, Creation Date, Description, Priority, Category, and Status.

## Usage
1. Clone or download the repository.
2. Run the script in a Python environment.
3. Follow the prompts to create a support ticket.

Example:
```bash
$ python support_ticket_generator.py


Welcome to the Automated Support Ticket Generator!
Please enter the following information to generate a ticket.
Describe the issue you're experiencing: Cannot connect to Wi-Fi.

Select priority level:
1. Low
2. Medium
3. High
Enter the priority number (1-3): 2

Select issue category:
1. Hardware
2. Software
3. Network
4. Account Access
5. Other
Enter the category number (1-5): 3

Support Ticket Created Successfully!
----------------------------------------
Ticket ID: Ticket-20241105093021-123
Creation Date: 2024-11-05 09:30:21
Description: Cannot connect to Wi-Fi.
Priority: Medium
Category: Network
Status: Open
----------------------------------------
