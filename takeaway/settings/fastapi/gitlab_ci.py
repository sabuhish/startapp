Gitlab ='''

.anchors:
  - &config-gcp echo $GCP_SERVICE_CONFIG | base64 -di > ${HOME}/gcloud-service-key.json
    && gcloud auth activate-service-account --quiet --key-file ${HOME}/gcloud-service-key.json
    && gcloud auth configure-docker --quiet

  - &config-prod-kube mkdir -p $HOME/.kube
    && echo -n $KUBE_CONFIG | base64 -di > $HOME/.kube/config
    && kubectl version
  - &publish-image docker build -t $IMAGE_ADDRESS .
    && docker push $IMAGE_ADDRESS


stages:
- build
- test
- deploy
- cleanup

publish:
  stage: build
  services:
    - docker:dind
  image: google/cloud-sdk:latest
  before_script:
    - *config-gcp
  script:
    - export IMAGE_ADDRESS=eu.gcr.io/${GCP_PROJECT_ID}/${CI_PROJECT_NAME}:${CI_COMMIT_SHA}
    - *publish-image
  only:
    - develop
    - master
  tags:
  - digital_runner_ci

release:
  stage: build
  services:
    - docker:dind
  image: google/cloud-sdk:latest
  before_script:
    - *config-gcp
  script:
    - export IMAGE_ADDRESS=eu.gcr.io/${GCP_PROJECT_ID}/${CI_PROJECT_NAME}:${CI_BUILD_TAG}
    - *publish-image
  only:
    - tags
  tags:
  - digital_runner_ci


test:
  services:
    - docker:dind 

  stage: test
  script:
    - echo $CI_JOB_STAGE
    - echo So you are telling me that I have to write code to check if the code I wrote earlier was right ?
    - echo I dont always test my code but when I do, I do it in production

  tags:
  - digital_runner_ci


deploy:
  stage: deploy
  dependencies:
    - test
  image: google/cloud-sdk
  before_script:
    - *config-prod-kube
  script:
    - export IMAGE_ADDRESS=eu.gcr.io/${GCP_PROJECT_ID}/${CI_PROJECT_NAME}:${CI_COMMIT_SHA}
    - kubectl set image deployment/${CI_PROJECT_NAME} app=${IMAGE_ADDRESS}
  only:
    - master
    - develop
  environment:
    name: deploy
  when: manual
  tags:
  - digital_runner_ci




production:
  stage: deploy
  dependencies:
    - test
  image: google/cloud-sdk
  before_script:
    - *config-prod-kube
  script:
    - export IMAGE_ADDRESS=eu.gcr.io/${GCP_PROJECT_ID}/${CI_PROJECT_NAME}:${CI_BUILD_TAG}
    - kubectl set image deployment/${CI_PROJECT_NAME} app=${IMAGE_ADDRESS}
  only:
    - tags
  environment:
    name: Production
  tags:
  - digital_runner_ci
  when: manual
 

cleanup:
  stage: cleanup
  before_script:
    - bash containers.sh
  script:
    - echo $CI_JOB_STAGE
  tags:
  - digital_runner_sh

'''