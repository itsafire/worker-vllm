import os, json
from argparse import ArgumentParser

import runpod

ENDPOINTS = {
    'mistral': 'ez6y7mp148jscf',
    'tinyllama': 'o3k3v8rv7e0cov'
}

def query_llm(prompt: str, model: str):
    runpod.api_key = os.getenv('API_KEY')
    endpoint = runpod.Endpoint(ENDPOINTS[model])

    run_request = endpoint.run(
        {
            "input": {
                "prompt": "Hello, my name is",
            }
        }
    )
    output = run_request.output()
    return output

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('model', type=str, help='Model to use for the function')
    parser.add_argument('prompt', type=str, help='Prompt to use for the function')
    args = parser.parse_args()

    print(f'Model: {args.model} Prompt: {args.prompt} API_KEY: {os.getenv("API_KEY")}')
    runpod.api_key = os.getenv('API_KEY')

    response = query_llm(args.prompt, args.model)
    print(json.dumps(response, indent=4))