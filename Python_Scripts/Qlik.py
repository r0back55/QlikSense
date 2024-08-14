import requests


# Qlik Sense server details
qlik_server = 'https://your-qlik-sense-server'
app_id = 'your-app-id'
sheet_id = 'your-sheet-id'

# API endpoint and headers
export_url = f'{qlik_server}/qrs/export/app/{app_id}/sheet/{sheet_id}/pdf'
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

# Request body for PDF export
body = {
    "paperSize": "A4",
    "orientation": "landscape"
}

# Make the API request to export the sheet as PDF
response = requests.post(export_url, headers=headers, json=body)

# Save the PDF file
if response.status_code == 200:
    with open('report.pdf', 'wb') as file:
        file.write(response.content)
    print("PDF report generated successfully.")
else:
    print(f"Failed to generate PDF report. Status code: {response.status_code}")



# Optional: Email the PDF report
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email details
sender = 'you@example.com'
recipient = 'recipient@example.com'
subject = 'Daily Report'
body = 'Please find the attached daily report.'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

# Attach the PDF report
with open('report.pdf', 'rb') as attachment:
    part = MIMEApplication(attachment.read(), Name='report.pdf')
    part['Content-Disposition'] = 'attachment; filename="report.pdf"'
    msg.attach(part)

# Send the email
with smtplib.SMTP('smtp.example.com', 587) as server:
    server.starttls()
    server.login('your_email@example.com', 'your_password')
    server.sendmail(sender, recipient, msg.as_string())

print("Email sent successfully.")
