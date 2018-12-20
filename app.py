"""
RUN WITH:
FLASK_APP=app.py FLASK_ENV=development flask run 
"""

import json
from flask import Flask, jsonify, request, abort, make_response
from peewee import *
from playhouse.flask_utils import FlaskDB
from playhouse.shortcuts import model_to_dict
from flask_cors import CORS

DATABASE = SqliteDatabase('data.db')

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

db_wrapper = FlaskDB(app)
peewee_db = db_wrapper.database

@app.route('/api/v1/events/<int:eventId>', methods=['GET'])
def event_details(eventId=0):
    try:
        event = (Event
                    .select()
                    .join(Location, on=(Location.event == Event.id))
                    .where(Event.id == eventId).get())
        response = jsonify(event_details_response(event))
    except DoesNotExist:
        abort(404)
    return make_response(response, 200)

def event_details_response(event):
    return {'data': model_to_dict(event)}

@app.route('/api/v1/events', methods=['GET'])
def events_summary():
    page      = int(request.args.get('page', '0'))
    delimiter = 10
    offset    = 0
    limit     = delimiter
    if page > 0:
        limit  = page * delimiter
        offset = page * delimiter

    rows = (Event
              .select(Event.id, Event.name, Location.name)
              .join(Location, on=(Location.event == Event.id))
              .limit(limit)
              .offset(offset))

    response = jsonify(events_summary_response(rows))
    return make_response(response, 200)

def events_summary_response(events):
    return [{'id': event.id,
             'name': event.name,
             'venue': event.location.name} for event in events]

@app.route('/api/v1/events/<int:eventId>', methods=['PUT'])
def rsvp(eventId=0):
    try:
        event = Event.select().where(Event.id == eventId).get()
        res = (Event
                    .update({Event.participant_count: event.participant_count + 1})
                    .where(Event.id == eventId)
                    .execute())
    except DoesNotExist:
        abort(404)

    return make_response('', 204)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

class Event(db_wrapper.Model):
    status                   = CharField()
    start_date               = DateField()
    end_date                 = DateField()
    description              = CharField()
    official                 = BooleanField(default = True)
    visibility               = CharField()
    guests_can_invite_others = CharField()
    modified_date            = DateField()
    created_date             = DateField()
    participant_count        = IntegerField()
    reason_for_private       = CharField()
    order_email_template     = CharField()
    name                     = CharField()

    class Meta:
        table_name = 'events'

class Location(db_wrapper.Model):
    event                   = ForeignKeyField(Event, backref='events')
    contact_phone           = CharField()
    primary                 = BooleanField()
    contact_email           = CharField()
    contact_family_name     = CharField()
    contact_given_name      = CharField()
    host_given_name         = CharField()
    timezone                = CharField()
    city                    = CharField()
    locality                = CharField()
    state                   = CharField()
    address_type            = CharField()
    latitude                = CharField()
    longitude               = CharField()
    accuracy                = CharField()
    address1                = CharField()
    address2                = CharField()
    postal_code             = CharField()
    country                 = CharField()
    modified_date           = DateField()
    created_date            = DateField()
    number_spaces_remaining = IntegerField()
    spaces_remaining        = BooleanField()
    name                    = CharField()

    class Meta:
        table_name = 'locations'
