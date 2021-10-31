# gstav-docker

## Installation instructions
- Install docker and docker-compose for your distribution
- If you want to serve the application from an IP (not localhost) on the host machine, you need to create a file called .env in the root directory with the following content:
    - IP=YOUR_HOST_IP
- Create a directory server/secret, then create a file server/secret/env.py with the following contents, replacing the values with your own:
    - url = "YOUR_MAILGUN_API_URL"
    - api = "YOUR_MAILGUN_API_KEY"
    - mailFrom = "YOUR_MAILGUN_FROM_ADDRESS"
    - mongoURI = "mongodb://IP:PORT/DB"
    - flickrApiKey = "YOUR_FLICKR_API_KEY"

## Run application
docker compose -f docker-compose.yml up
## Stop application
docker compose -f docker-compose.yml down --rmi all -v
