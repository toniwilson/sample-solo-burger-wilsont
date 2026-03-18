from flask import Flask

app = Flask(__name__)
app.secret_key = 'change-this-in-production'  # Required for session support

@app.route('/')
def index():
    return "Hello, World! Your Flask app is running."

if __name__ == '__main__':
    app.run(debug=True)
