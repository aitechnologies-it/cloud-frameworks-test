# Cloud Frameworks Tests

This repository contains some Web Hello Worlds in different technologies to be used to test Cloud Services.

* [Micronaut & Graal (Java)](mngraal)
* [Nodejs](nodejs)
* [Python](python)


## Google Cloud Platform - Cloud Run

Cloud Run default `512MB` functions, region `europe-west1`

For Pisa (Italy) we did some tests with the function Endpoints
- ***Cold Starts***
usually between `1s` and `2s` for all the technologies.

- ***Up Requests*** when the function is alive, we have a full response in `100ms-200ms`

All the technologies are pretty good to develop REST Endpoints that are good even if the response may took some seconds.