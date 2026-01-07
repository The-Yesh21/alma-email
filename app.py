from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Email configuration (from new.py)
EMAIL_ADDRESS = "yeshwanth9750@gmail.com"
APP_PASSWORD = "fiul nimu bkrm avlf"

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'running',
        'message': 'Alma Email API is active',
        'email': EMAIL_ADDRESS
    })

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'to' not in data or 'subject' not in data or 'message' not in data:
            return jsonify({'error': 'Missing required fields: to, subject, message'}), 400
        
        to_email = data['to']
        subject = data['subject']
        message = data['message']
        
        # Create email message
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(message)
        
        # Send email using SMTP_SSL (same as new.py)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Email sent to {to_email}")
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
