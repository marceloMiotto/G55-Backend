def success_to_json(returned_id):
    return '{"result": "SUCCESS", "id":"' + returned_id + '" }'


def error_to_json(msg):
    return '{"result": "' + msg + '"} '

