from flask import Flask

app = Flask(__name__)

@app.route("/")
def e():
  return "lol"

if __name__ == "__main__":
  app.run()
