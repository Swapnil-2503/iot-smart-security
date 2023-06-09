from flask import Flask, request, jsonify

app = Flask(__name__)

notifications = []

@app.route('/notification', methods=['POST'])
def handle_notification():
    message = request.form.get('message')
    notifications.append({'message': message})

    return 'Notification received'

@app.route('/notifications', methods=['GET'])
def get_notifications():
    return jsonify(notifications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
