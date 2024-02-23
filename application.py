from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/users')
def get_drinks():
    return {"users" : "user_data"}

