from flask import jsonify
import src.crud as C


def get_tickets():
    return jsonify(C.get_tickets())


def get_ticket(ticket_id):
    return jsonify(C.get_ticket(ticket_id))
