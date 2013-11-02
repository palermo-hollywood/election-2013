from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html',
        headline = "Resultados de las elecciones en la escuela donde votaste",
        description = """
<p>The results of October's deputies election at the schools where
<em>Capital Federal</em> voters cast ballots.</p>

<p>Circles are colored in to represent
that party that won the most votes and sized to show the margin of victory.</p>

<p>
    This is a modified take on <a href="http://www.lanacion.com.ar/1633333-como-fueron-los-resultados-de-las-elecciones-en-la-escuela-donde-votaste">a map</a> published by <em>La Nacion</em> 
    last week.
    It was developed by Team Hollywood Palermo at <a href="http://blogs.lanacion.com.ar/datafest/">Datafest 2013</a> in Buenos Aires.
    The source is <a href="https://github.com/palermo-hollywood/election-2013">available on GitHub</a>.
</p>
"""
    )


if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("8000"),
        use_reloader=True,
        debug=True,
  )
