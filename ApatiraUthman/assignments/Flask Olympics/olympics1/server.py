from flask import Flask
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug = True)
