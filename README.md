![don't hate](static/screenshot.png)

Resultados de las Oct. 2013 Buenos Aires elecciones. Live at [http://palermo-hollywood.github.io/election-2013/](http://palermo-hollywood.github.io/election-2013/). Later appeared in a print edition of [La Nacion](http://www.flickr.com/photos/palewire/10837636836/) as well as on its [website](http://www.lanacion.com.ar/1637762-la-obra-publica-y-el-clientelismo-tambien-pesan-en-la-capital).

Getting started
---------------

Create a virtualenv to store all the code in a nice tupperware container.

```bash
$ virtualenv election-2013
```

Jump into it.

```bash
$ cd election-2013
$ . bin/activate
```

Clone the repository.

```bash
$ git clone git@github.com:palermo-hollywood/election-2013.git repo
```

Jump into it.

```bash
$ cd repo
```

Install the other Python dependencies.

```bash
$ pip install -r requirements
```

Fire up the Flask server that hosts our development pages.

```bash
$ python app.py
# Visit http://localhost:8000 in your browser and check it out.
```

To flatten the Flask site so it can be hosted without a server as static files.

```bash
# This will update the files in the ./build directory
$ python freeze.py
```

Who to blame
------------

![don't hate](static/sign.jpg)

This code was developed at Data Fest 2013 in Buenos Aires by Team Palermo Hollywood.
