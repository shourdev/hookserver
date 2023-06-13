from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Retrieve the JSON data from the request
    # Process the webhook data here
    print(data)
    return 'Webhook received successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
