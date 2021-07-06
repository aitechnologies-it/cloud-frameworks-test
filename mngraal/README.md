# Micronaut  Graal

## Build 

### Step 0 - How we created the project
We created the project using the `mn` cli, choosing the maven build system.

```sh
sdk install micronaut 2.5.7
mn create-app it.aitlab.tests.mngraal --build=maven
```


### Step 1 - How To Run Locally

It is a Maven Micronaut Web Application, so simply type

```sh
./mvnw mn:run 
```

Take a look at the startup completed time.

### Step 2 - Native Compilation With Graal

To native compile the code you need the GraalVM. We suggest to use `sdk` to install it.

```sh
# Example: Install Graal and Native Image
sdk install java 21.1.0.r11-grl
gu install native-image
```

```sh
# Point to the graal jdk and then package the app
sdk use java 21.1.0.r11-grl
./mvnw package -Dpackaging=native-image
./target/mngraal

# test the service
curl 127.0.0.1:8080
```

### Step 3 - Docker Native Image

You can also create a Native Docker Image, useful for cloud serverless services.

```sh
# Create the image locally
./mvnw package -Dpackaging=docker-native

# Run the image locally
docker run -p 8080:8080 mngraal
curl 127.0.0.1:8080
```


## Deploy to the Cloud 

### Deploy to GCP - Cloud Run
To deploy you must have `gcloud` enabled in your environment, and a valida google project with billing enabled. 

```sh
# to authorize docker (can be done only once in the system)
gcloud auth configure-docker

# Tag and push the image to your project registry (you can change the location, we use eu for europe)
docker image tag mngraal:latest eu.gcr.io/${PROJECT_ID}/mngraal:latest
docker image push eu.gcr.io/${PROJECT_ID}/mngraal:latest
```

Now you can create a Cloud Run Function

```sh
# Example: deploy as mngraal in europe-west1 without authentication

gcloud run deploy mngraal --project ${PROJECT_ID} --allow-unauthenticated --image eu.gcr.io/${PROJECT_ID}/mngraal:latest --platform mnaged --region europe-west1
```

Check the response with response time (and start transfer)
```sh
curl -s  -w  '\n\n%{time_starttransfer}-%{time_total}\n' https://mngraal-yourendpoint-ew.a.run.app/
```
```
Hello World!!!

0,170996-0,171144
```