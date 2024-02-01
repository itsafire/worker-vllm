# this requires the installation of runpod-python
# with `pip install runpod-python` beforehand

import runpod
import json

runpod.api_key = "R9QF4C991BKME1P17UNTJBPI75F3VIXAQSDPTOTK" # you can find this in settings

endpoint = runpod.Endpoint("j0d7qek42k9nf7")

run_request = endpoint.run(
    {
        "input": {
            "prompt": "Tell me a little story.",
            "batch_size": 512,
            "stream": True
        }
    }
)

breakpoint()

pretty_json = json.dumps(run_request, indent=4)
print(pretty_json)