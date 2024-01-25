# this requires the installation of runpod-python
# with `pip install runpod-python` beforehand

import runpod
import json

runpod.api_key = "R9QF4C991BKME1P17UNTJBPI75F3VIXAQSDPTOTK" # you can find this in settings

endpoint = runpod.Endpoint("3w0sgvd0blkzbi")

run_request = endpoint.run_sync(
    {
        "input": {
            "prompt": "Tell me a little funny story."
        }
    }
)

pretty_json = json.dumps(run_request, indent=4)
print(pretty_json)