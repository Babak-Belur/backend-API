from flask import jsonify, make_response

def success(values, message):
    res = {
        'message': message,
        'status': True,    
        'data': values
    }

    return make_response(jsonify(res)), 200

def badRequest(values, message):
    res = {
        'data': values,
        'message': message
    }

    return make_response(jsonify(res)), 400