import logging
from typing import Any, Dict
from vllm.utils import random_uuid
from constants import SAMPLING_PARAM_TYPES, DEFAULT_BATCH_SIZE

logging.basicConfig(level=logging.INFO)

def count_physical_cores():
    with open('/proc/cpuinfo') as f:
        content = f.readlines()

    cores = set()
    current_physical_id = None
    current_core_id = None

    for line in content:
        if 'physical id' in line:
            current_physical_id = line.strip().split(': ')[1]
        elif 'core id' in line:
            current_core_id = line.strip().split(': ')[1]
            cores.add((current_physical_id, current_core_id))

    return len(cores)

def validate_sampling_params(params: Dict[str, Any]) -> Dict[str, Any]:
    validated_params = {}
    invalid_params = []
    for key, value in params.items():
        expected_type = SAMPLING_PARAM_TYPES.get(key)
        if expected_type and isinstance(value, expected_type):
            validated_params[key] = value
        else:
            invalid_params.append(key)
        
    if len(invalid_params) > 0:
        logging.warning("Ignoring invalid sampling params: %s", invalid_params)
        
    return validated_params

class JobInput:
    def __init__(self, job):
        self.llm_input = job.get("messages", job.get("prompt"))
        self.stream = job.get("stream", False)
        self.batch_size = job.get("batch_size", DEFAULT_BATCH_SIZE)
        self.apply_chat_template = job.get("apply_chat_template", False)
        self.use_openai_format = job.get("use_openai_format", False)
        self.validated_sampling_params = validate_sampling_params(job.get("sampling_params", {}))
        self.request_id = random_uuid()
           
class DummyRequest:
    async def is_disconnected(self):
        return False