election-2013
=============

Oct. 2013 election results for Argentine Diputados Nacionales in Buenos Aires.

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
```

To flatten the Flask site so it can be hosted without a server as static files.

```bash
# This will update the files in the ./build directory
$ python freeze.py
```

Visit [http://localhost:8000](http://localhost:8000) in your browser and check it out.

Who to blame
------------

![don't hate](static/sign.jpg)

This code was developed at Data Fest 2013 in Buenos Aires by Team Palermo Hollywood.
