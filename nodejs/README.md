# Nodejs

Node.js express web app that simply says Hello from its root endpoint.

```
npm install
node index.js
```

## Deploy to the Cloud 

### Deploy to GCP - Cloud Run

Use `gcloud` to build and deploy.

```sh
# Build with cloud build
gcloud builds submit --tag eu.gcr.io/${PROJECT_ID}/nodejs --project ${PROJECT_ID}

# Deploy and Run with Cloud Run
gcloud run deploy nodejs --project ${PROJECT_ID} --allow-unauthenticated --image eu.gcr.io/${PROJECT_ID}/nodejs --platform managed --region europe-west1
```