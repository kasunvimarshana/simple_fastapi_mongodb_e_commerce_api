import json as json
from bson import json_util
from bson import ObjectId
from datetime import datetime, timezone, timedelta, date

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        # if isinstance(o, (datetime, date)):
        #     return o.isoformat()
        if isinstance(o, ObjectId):
            return str(o)
        else:
            # return json.JSONEncoder.default(self, o)
            return super().default(o)


# if __name__ == "__main__":
#     JSONEncoder().encode({})
#     json.encode({}, cls=JSONEncoder)
#     json.loads(json.dumps({}, default=json_util.default))
