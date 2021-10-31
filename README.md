# gstav-docker

## Installation instructions
Install docker and docker-compose for your distribution

## Run application
docker compose -f docker-compose.yml up
## Stop application
docker compose -f docker-compose.yml down --rmi all -v

## Optional steps
If you wish to use the contact form and the flickr API, then create a file ./server/env.py with the following contents, replacing the capitalized strings with your own:
- url = "YOUR_MAILGUN_API_URL"
- api = "YOUR_MAILGUN_API_KEY"
- mailFrom = "YOUR_MAILGUN_FROM_ADDRESS"
- flickrApiKey = "YOUR_FLICKR_API_KEY"
