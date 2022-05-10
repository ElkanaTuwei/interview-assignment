# Interview Assignment
Receives an integer as GET parameter and returns a json response based on if the number is a multiple of five, seven, both five and seven or none.

To run project:

Activate the virtual environment

``
$ source virtualenv/bin/activate
``

and start the development server

``
$ python3 manage.py runserver
``

Make a get request to `ip`:`port`/?integer=`{{integer_value}}`

e.g `http://127.0.0.1:8000?integer=34`