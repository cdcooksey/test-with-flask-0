from flask import Flask
from flask import jsonify
from peewee import *
import json
from playhouse.flask_utils import FlaskDB

DATABASE = SqliteDatabase('data.db')

app = Flask(__name__)
app.config.from_object(__name__)

db_wrapper = FlaskDB(app)
peewee_db = db_wrapper.database

@app.route('/')
def hello():
    row = Event.select().get()
    data = {
            'id':           row.id,
            'status':       row.status,
            'start_date':   row.start_date,
            'end_date':     row.end_date,
            'description':  row.description,
            'official':     row.official
            }
    
    return jsonify({'data': data})

# CREATE TABLE events (
#     id integer NOT NULL,
#     status character varying,
#     start_date timestamp without time zone,
#     end_date timestamp without time zone,
#     description character varying,
#     official boolean,
#     visibility character varying,
#     guests_can_invite_others boolean,
#     modified_date timestamp without time zone,
#     created_date timestamp without time zone,
#     participant_count numeric,
#     reason_for_private character varying,
#     order_email_template character varying,
#     name character varying
class Event(db_wrapper.Model):
    status = CharField()
    start_date = DateField()
    end_date = DateField()
    description = CharField()
    official = BooleanField(default=True)

    class Meta:
        table_name = 'events'
