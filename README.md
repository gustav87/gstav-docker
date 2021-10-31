# gstav-docker

## Installation instructions
- Install Docker for your distribution
- Run npm start
- If you want to serve the site from an IP (not localhost) on the host machine, you need to create a file called .env in the root directory with the following content:
    - IP=YOUR_HOST_IP
- Create a directory server/secret, then create a file server/secret/env.py with the following contents, replacing the values with your own:
    - url = "YOUR_MAILGUN_API_URL"
    - api = "YOUR_MAILGUN_API_KEY"
    - mailFrom = "YOUR_MAILGUN_FROM_ADDRESS"
    - mongoURI = "mongodb://IP:PORT/DB"
    - flickrApiKey = "YOUR_FLICKR_API_KEY"
