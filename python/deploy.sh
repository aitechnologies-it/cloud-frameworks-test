#!/bin/bash

HELP="Usage: $0 [OPTIONS]

OPTIONS:
  -b|--build      build docker image with cloud build
  -d|--deploy     deploy cloud run. Make sure to set up env vars

GUIDES:
  - Run in project root
  - To deploy to another project:
      Edit $0 and cloudbuild.yaml
"

function parser {
    while (( $# > 0 ))
    do
        opt="$1"
        shift

        case $opt in
        --help)
            echo $HELP
            exit 0
            ;;
        -b|--build)
            export BUILD=true
            ;;
        -d|--deploy)
            export DEPLOY=true
            ;;
        --*)
            echo "Invalid option: '$opt'" >&2
            exit 1
            ;;
        *)
            # end of long options
            break;
            ;;
        esac
    done
}

if [ $# == 0 ]; then
    echo "$HELP"
    exit 1
fi

SERVICE_NAME="pythonminimal"
PROJECT_ID="ultra-badge-248311"
ZONE="europe-west1"
parser $@

if [ ! -z $BUILD ]; then
  echo "----- BUILD -----"
  gcloud builds submit --project ${PROJECT_ID} --config ./docker/cloudbuild.yaml .
fi

if [ ! -z $DEPLOY ]; then
  echo "----- DEPLOY -----"
  gcloud run deploy ${SERVICE_NAME}-cpu2-256-alpine \
      --image eu.gcr.io/${PROJECT_ID}/${SERVICE_NAME} \
      --platform=managed \
      --project ${PROJECT_ID} \
      --region ${ZONE} \
      --allow-unauthenticated \
      --max-instances 1 \
      --cpu 2 \
      --memory 256Mi \
      --port "8080" \
      --set-env-vars PROJECT_ID="${PROJECT_ID}" \
      --set-env-vars FLASK_CONFIG="production" \
      --set-env-vars FLASK_PORT="8080" \
      --set-env-vars REQUIRE_AUTH="true" \
      --set-env-vars BASIC_AUTH_USERNAME="manzi" \
      --set-env-vars BASIC_AUTH_PASSWORD="cane"
  fi