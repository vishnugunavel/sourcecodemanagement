from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def homepage():
    return "welcome to AIML"

@app.route("/help")
def help():    
    return "How can i help you?"

@app.route("/hello")
def hello():
    return "Hello how are you? what i can do for you?"

@app.route("/test)
def test():
    return "test route"

if __name__ == "__main__":
    app.run()
	

