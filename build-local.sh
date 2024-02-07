# run this script to build the docker images

# to run the client image:
# docker run -it --rm -v ./you_client.py:/client.py client 
docker build -t client -f Dockerfile.client .
docker build -t itsafire/vllm:opt125m --build-arg MODEL_NAME="facebook/opt-125m" --build-arg MODEL_BASE_PATH="/models" .

