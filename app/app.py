from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "<h2 style='color:green'>Hello World!</h2>\n"

if __name__ == "__main__":
  app.run(host='0.0.0.0')

