import json
import bgt_traffic

april_1 = bgt_traffic.traffic.get('04/01/2015')

print (json.dumps(april_1,sort_keys=True, indent=8))

"""
import json
print json.dumps({'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}},
...                  sort_keys=True, indent=4)
{
    "a": 2,
    "b": {
        "x": 3,
        "y": {
            "t1": 4,
            "t2": 5
        }
    }
}
"""
