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
 
if __name__ == "__main__":
    app.run()
	

