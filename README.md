# gstav-docker

## Installation instructions
Install docker and docker-compose for your distribution

## Run application
docker compose up
## Stop application
docker compose down --rmi all -v

## Optional steps
If you wish to use the contact form and the flickr API, then create a file .env in the root, with the following contents, replacing the capitalized strings with your own:
- mailgun_url = "YOUR_MAILGUN_API_URL"
- mailgun_api_key = "YOUR_MAILGUN_API_KEY"
- mailgun_from = "YOUR_MAILGUN_FROM_ADDRESS"
- flickr_api_key = "YOUR_FLICKR_API_KEY"
