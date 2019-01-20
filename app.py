from flask import Flask, render_template
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

@app.route("/test")
def test():
    user = {'username': 'Vignesh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)   

if __name__ == "__main__":
    app.run()
	

