# CI/CD

## *Microservices*

There are 2 microservices:

* Service1 - creates hashes of strings
* Service2 - downloads a web page and calls service1 to create a md5 hash of it

Your task is to check (and fix) the microservice implementation / docker images:

* which improvements do you suggest
* which errors did you detect
* other comments

## Continuous Integration/Delivery

Create a pipeline for the microservices that will:
1. version and build docker images of both services
2. run tests
3. publish the docker images

## *Continuous* Deployment

Create a script (bash/python) that would deploy (run with docker) the set of microservices with specified versions and parameters (if needed).

```bash
> ./deploy --version_service1=v1.0 --version_service2=v1.0 --additional_param_1=5 #both microservices should be deployed with version v1.0 and accessible on the local machine (via docker)
```

## (optional\*) Kubernetes deployment

1. Create kubernetes yaml configuration files for both microservices.
2. Deploy the yaml files on kubernetes (local installation)
3. Create a helm chart for each microservice
4. Create scripts that will deploy points `2.` and `3.` similarly to the [previous task](#"continuous"-deployment) (exception that it would be run on kubernetes instead of only docker)

## Expected outcome

1. Optimized, maintainable docker images
2. Automated, maintainable pipelines
3. Automated versioning of service/solution artifacts
4. Simple docker deployment of both microservices
5. (optional\*) kubernetes deployment of both microservices (helm + kubernetes yaml)

## Help

* Docker images can be stored on dockerhub or as tar.gz archives or any other way that you see fit
* All of the utilities / libraries (e.g. openFaaS) already included are enough to support functional services
  * Substitutions are welcome (e.g. replacing openFaaS with Flask) as long as they are made to fulfill the same role
* The emphasis is not that the services work correctly, or make sense :), but on:
  * Service communication
  * Configurability
  * Maintainability
  * Time to deploy
  * Docker image optimization
  * Pipeline stability
* (optional\*) Each service should be a kubernetes deployment, and can include services/ingress/other kubernetes components 

### Basic pipeline

* Build
* Unit Test+
* Integration Test+
* Publish Artifact

+No need for writing unit/integration/e-2-e tests, just include a step that will execute them

### Tools

* Docker
* Kubernetes (**local - docker**, minikube, ...)
* Kubectl/kustomize
* Helm 3
* Git
* CI/CD tool (GitLab/Azure DevOps/CircleCI/Jenkins/**github actions**/...)
* Python

### Additional info

* (optional\*) gives extra 'points'
* (optional\*) is required for certain roles


# Solution:

* When the code is pushed to the GitHub, Github Actions automatically runs `main.yaml` file to execute the CI/CD pipeline. 

* Python script `deploy.py` that would deploy (run with docker) the set of microservices with specified versions and parameters (if needed).
```
python deploy.py --version_service1=v1.0.0 --version_service2=v1.0.0
```
* Running the python script `deploy_on_k8s.py` deploys the yaml files on kubernetes.
* To deploy helm charts for each microservice, execute the `deploy_helm_charts.py` script.

### Improvements in code for service1/entrypoint.py:
- **function encapsulation:** `create_hash()` function for modularity, testability and reusability
- **error handling:** checks for supported hash functions, preventing unexpected errors
- **input validation:** checks input for unsupported hash functions
- added unittest to ensure correct behaviour
- added `str.encode('utf-8')` for encoding non-ASCII characters
- added `if __name__ == "__main__"`: to allow importing functions without executing the code directly

### Improvements in code for service2/entrypoint.py:
- **function encapsulation:** `call_service1(service_name, hash_function, message)`
- **error handling:** checks for invalid URLs and malformed responses
- **input validation:** checks for valid URL, if invalid throws **ValueError**
- added unittest to ensure correct behaviour
- added `if __name__ == "__main__":` to allow importing functions without executing the code directly