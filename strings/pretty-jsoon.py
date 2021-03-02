#https://www.interviewbit.com/problems/pretty-json/
A = '["foo", {"bar":["baz",null,1.0,2]}]'
import json
json_obj = json.loads(A)
print(json.dumps(json_obj, indent=0))


