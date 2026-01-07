from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# Email configuration (from environment variables or defaults)
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS', 'yeshwanth9750@gmail.com')
APP_PASSWORD = os.environ.get('APP_PASSWORD', 'fiul nimu bkrm avlf')

@app.errorhandler(Exception)
def handle_exception(e):
    # Pass through HTTP errors
    print(f"❌ Global Error: {str(e)}")
    return jsonify({"error": str(e), "success": False}), 500

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
        if not data:
            return jsonify({'error': 'No JSON data received', 'success': False}), 400
            
        if 'to' not in data or 'subject' not in data or 'message' not in data:
            return jsonify({'error': 'Missing required fields: to, subject, message', 'success': False}), 400
        
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
        print(f"📧 Attempting to send email to {to_email}...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.send_message(msg)
        
        print(f"✅ Email sent successfully to {to_email}")
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"❌ Send Email Error: {str(e)}")
        return jsonify({'error': str(e), 'success': False}), 500

if __name__ == '__main__':
    # Use port 5001 to avoid Windows 5000 conflict
    port = int(os.environ.get('PORT', 5001))
    print(f"🚀 Alma Email API starting on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)
