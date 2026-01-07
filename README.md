# 📧 Alma Email API

Flask-based email service for sending OTPs and notifications via Gmail SMTP.

## ✨ Features

- ✅ Send emails using Gmail SMTP (port 465, SSL)
- ✅ CORS enabled for frontend integration
- ✅ Simple REST API endpoint
- ✅ Error handling and logging
- ✅ Ready for deployment (Render, Railway, etc.)

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Server will start on `http://localhost:5001`

### From Project Root

```bash
# Using npm script
npm run email:start

# Or using batch file (Windows)
start-email-api.bat

# Or using PowerShell script
.\start-with-email.ps1
```

## 📡 API Endpoint

### POST `/send-email`

Send an email via Gmail SMTP.

**Request Body:**
```json
{
  "to": "recipient@example.com",
  "subject": "Email Subject",
  "message": "Email message content"
}
```

**Success Response (200):**
```json
{
  "success": true
}
```

**Error Response (400/500):**
```json
{
  "success": false,
  "error": "Error message"
}
```

### GET `/`

Health check endpoint.

**Response:**
```json
{
  "status": "running",
  "message": "Alma Email API is active",
  "email": "yeshwanth9750@gmail.com"
}
```

## 🧪 Testing

### Test 1: Health Check
```bash
curl http://localhost:5001/
```

### Test 2: Send Email (PowerShell)
```powershell
$body = @{
    to = "your-email@example.com"
    subject = "Test Email"
    message = "This is a test!"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5001/send-email" -Method POST -Body $body -ContentType "application/json"
```

### Test 3: Using Test Script
```bash
npm run email:test
```

## 🔧 Configuration

### Email Credentials

Currently configured in `app.py`:
```python
EMAIL_ADDRESS = "yeshwanth9750@gmail.com"
APP_PASSWORD = "fiul nimu bkrm avlf"
```

**For production**, use environment variables:
```python
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS', 'your-email@gmail.com')
APP_PASSWORD = os.environ.get('APP_PASSWORD', 'your-app-password')
```

### Gmail App Password

1. Go to [Google Account Settings](https://myaccount.google.com/apppasswords)
2. Generate a new app password
3. Use it in place of your regular Gmail password

## 🌐 Deployment

### Deploy to Render

1. Create account at [render.com](https://render.com/)
2. Create new Web Service
3. Connect GitHub repo
4. Configure:
   - **Root Directory**: `email-api`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add environment variables:
   - `EMAIL_ADDRESS`: Your Gmail address
   - `APP_PASSWORD`: Your Gmail app password
6. Deploy!

### Deploy to Railway

1. Create account at [railway.app](https://railway.app/)
2. Deploy from GitHub
3. Select `email-api` folder
4. Add environment variables (same as above)
5. Railway auto-detects Python and deploys

### Update Frontend

After deployment, update `.env` in project root:
```env
VITE_EMAIL_API_URL=https://your-deployed-url.com/send-email
```

## 📁 Project Structure

```
email-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # For deployment
└── README.md          # This file
```

## 🐛 Troubleshooting

### Port 5001 already in use
```bash
# Windows: Find and kill process
netstat -ano | findstr :5001
taskkill /PID <PID> /F
```

### Module not found
```bash
pip install -r requirements.txt
```

### SMTP Authentication Error
- Verify Gmail app password is correct
- Ensure 2-factor authentication is enabled on Gmail
- Generate a new app password if needed

### CORS errors
- CORS is already enabled for all origins
- Check if API is running on correct port
- Verify frontend is using correct API URL

## 📊 Email Flow

```
Frontend → POST /send-email → Flask API → Gmail SMTP → Recipient
```

## 🔒 Security Notes

- ⚠️ Never commit credentials to Git
- ✅ Use environment variables in production
- ✅ Keep `.env` file in `.gitignore`
- ✅ Rotate app passwords regularly

## 📝 Dependencies

- **Flask** (3.0.0): Web framework
- **flask-cors** (4.0.0): CORS support
- **gunicorn** (21.2.0): Production server

## 💡 Usage in Project

This API is used by:
- `src/services/emailService.ts` - Frontend email service
- Principal OTP emails during login
- Teacher welcome emails with credentials

## 🤝 Support

For issues or questions, check:
1. [EMAIL_INTEGRATION_GUIDE.md](../EMAIL_INTEGRATION_GUIDE.md) in project root
2. Browser console for frontend errors
3. Terminal logs for API errors

---

**Ready to send emails!** 🚀

