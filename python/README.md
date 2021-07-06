# Python

Python Flask app that responds to basic endpoints.

```
pip install -r requirements.txt
python src/main.py
```

## Deploy to the Cloud

### Deploy to GCP - Cloud Run

```sh
# Build with Cloud Build
gcloud builds submit --project ${PROJECT_ID} --config ./cloudbuild.yaml .

# Deploy on Cloud Run
gcloud run deploy python-example \
    --image eu.gcr.io/${PROJECT_ID}/python-example \
    --platform=managed \
    --project ${PROJECT_ID} \
    --region europe-west1 \
    --allow-unauthenticated \
    --port "8080" \
    --set-env-vars PROJECT_ID="${PROJECT_ID}" \
    --set-env-vars FLASK_CONFIG="production"
```