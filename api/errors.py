from flask import jsonify
from sqlalchemy.exc import IntegrityError


def register_error_handlers(app):
    @app.errorhandler(IntegrityError)
    def handle_integrity_error(error):
        response = {
            'message': 'Integrity error: A record with the same unique key already exists.'
        }
        return jsonify(response), 400

    @app.errorhandler(404)
    def handle_not_found_error(error):
        response = {
            'message': 'Resource not found.'
        }
        return jsonify(response), 404

    @app.errorhandler(500)
    def handle_internal_server_error(error):
        response = {
            'message': 'An internal server error occurred.'
        }
        return jsonify(response), 500

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        response = {
            'message': 'An unexpected error occurred.'
        }
        return jsonify(response), 500
