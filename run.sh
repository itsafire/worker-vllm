#/bin/sh

docker build -f Dockerfile.client -t client  -q . >/dev/null

# check if at least 1 argument is passed
if [ $# -eq 0 ]; then
    echo "No arguments supplied"
    exit 1
fi
docker run -ti --rm --env-file .env client $1 "$2"

