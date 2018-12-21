python get-pip.py --user
pip install flask --user
pip install peewee --user
pip install flask-cors --user
echo "pip, flask, and peewee ORM installed. Running flask:"
FLASK_APP=app.py FLASK_ENV=development flask run --host=0.0.0.0
