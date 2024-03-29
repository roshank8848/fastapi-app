### Sample app for three tier app in kubernetes

#### Instructions
* Clone the repo 
* build the docker image

#### Environment variables
* create a new file named .env 
* create an env variable named `MONGO_URI` in `.env` file
* If you want to integrate this with senty setup a variable named `SENTRY_DSN` and update the `SENTRY_DSN` values you get when creating a fastapi app in [Sentry website](https://sentry.io) 