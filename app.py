from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        headline = "Headline goes here",
        description = """
<p>This is lorem ipsum. Pay no attention. This is lorem ipsum. 
Pay no attention. This is lorem ipsum. Pay no attention.</p>
"""
    )


if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("8000"),
        use_reloader=True,
        debug=True,
  )
