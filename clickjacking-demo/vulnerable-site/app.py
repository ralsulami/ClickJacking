from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make-payment', methods=['POST'])
def make_payment():
    return jsonify({'status': 'success', 'message': 'Payment successful!'})

 # @app.after_request
# def add_headers(response):
 #   response.headers["X-Frame-Options"] = "DENY"
 #   response.headers["Content-Security-Policy"] = "frame-ancestors 'self'"
 #   return response

if __name__ == '__main__':
    app.run(port=5000)
