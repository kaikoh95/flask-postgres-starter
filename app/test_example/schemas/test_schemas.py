from marshmallow import Schema, fields, validate


class LocationSchema(Schema):
    long = fields.Float(required=True, example=123.45)
    lat = fields.Float(required=True, example=123.45)


class TestObjectSchema(Schema):
    id = fields.String(required=True, example="xxxxxx-xxxx-xxxx-xxxxx")
    object = fields.String(required=True, example="50",
                           validate=validate.OneOf([str(i) for i in range(1, 51)]))
    objectNumber = fields.String(required=True, example="123")
    objectStatus = fields.String(required=True, example="123")
    lastLocation = fields.Nested(LocationSchema(), required=True)


class TestObjectRequestSchema(Schema):
    objectId = fields.String(required=True, example="23",
                             validate=validate.OneOf([str(i) for i in range(1, 51)]))
    objectNumber = fields.String(required=True, example="123")
