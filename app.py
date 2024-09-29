from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<a href='/about'>Click here for the about page</a>"


@app.route('/about')
def about():
    return """
    <p1>about this project</p>
    <a href='/'>back to home</a>
    """

if __name__ == '__main__':

    app.run()
