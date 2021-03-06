entity = {
    'schema': {
        'key': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'value': {
            'type': 'boolean',
            'required': True
        }
    },
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PUT', 'PATCH']
}
