pipeline {
  agent any

  environment {
      DOCKERHUB_USRNAME = "ausaf009"
      APP_NAME = "python-pro"
      IMAGE_TAG = "${BUILD_NUMBER}"
      IMAGE_NAME = "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
      REGISTRY_CREDS = 'docker-cred'
  }

  stages {
    stage('Checkout') {
      steps {
        sh "echo passed"
        //git branch: 'main', url: 'https://github.com/0akash0/java-minikube.git'
      }
    }

    stage('Build and Push Docker Image') {
      environment {
        DOCKER_IMAGE = "ausaf009/python-img:latest:${BUILD_NUMBER}"
        // REGISTRY_CREDENTIALS = credentials('docker-cred')
      }
      steps {
        script {
            sh 'docker build -t ${DOCKER_IMAGE} .'
            def dockerImage = docker.image("${DOCKER_IMAGE}")
            docker.withRegistry('https://index.docker.io/v1/', "Dockerhub") {
                dockerImage.push()
            }
        }
      }
    }
    stage('Update Deployment File') {
        environment {
            GIT_REPO_NAME = "python-pro"
            GIT_USER_NAME = "ausaf-wohlig"
        }
        steps {
            withCredentials([string(credentialsId: 'github', variable: 'GITHUB_TOKEN')]) {
                sh '''
                    git config user.email "ausafansari.wohlig@gmail.com"
                    git config user.name "ausaf-wohlig"
                    BUILD_NUMBER=${BUILD_NUMBER}
                    sed -i "s/${APP_NAME}./${APP_NAME}:${IMAGE_TAG}/g" deploy/deployment.yml
                    git add deploy/deployment.yml
                    git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                    git push @github.com/${GIT_USER_NAME}/${GIT_REPO_NAME">https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                '''
            }
        }
    }
  }
}
