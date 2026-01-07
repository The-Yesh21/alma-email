# Alma Email API

Python Flask API for sending emails via Gmail SMTP.

## Features
- Send emails using Gmail SMTP
- CORS enabled for frontend integration
- Simple REST API endpoint

## Deployment
Deploy to Render or Railway for free hosting.

## API Endpoint
POST `/send-email`

Request body:
```json
{
  "to": "recipient@example.com",
  "subject": "Email Subject",
  "message": "Email message content"
}
```

## Local Development
```bash
pip install -r requirements.txt
python app.py
```
