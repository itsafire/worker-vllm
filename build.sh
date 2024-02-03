# run this script to build the docker images

docker pull itsafire/vllm:Mistral
docker pull itsafire/vllm:TinyLlama

# to run the client image:
# docker run -it --rm -v ./you_client.py:/client.py client 
docker build -t client -f Dockerfile.client .
docker build -t itsafire/vllm:Mistral --build-arg MODEL_NAME="mistralai/Mistral-7B-Instruct-v0.2" --build-arg MODEL_BASE_PATH="/models" .
docker build -t itsafire/vllm:TinyLlama --build-arg MODEL_NAME="TinyLlama/TinyLlama-1.1B-Chat-v1.0" --build-arg MODEL_BASE_PATH="/models" .
docker push itsafire/vllm:TinyLlama
docker push itsafire/vllm:Mistral
