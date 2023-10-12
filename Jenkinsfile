pipeline {
    agent any
    
    stages {
        // stage("Code") {
        //     steps {
        //            withCredentials([usernamePassword(credentialsId: "github", passwordVariable: "githubPass", usernameVariable: "githubUser")])
        //         git url: "https://github.com/ausaf-wohlig/python-pro.git", branch: "main"
        //     }
        // }
        stage("Build & Test") {
            steps {
                sh "docker build -t python-img ."
            }
        }
        stage("Push to DockerHub") {
            steps {
                withCredentials([usernamePassword(credentialsId: "Dockerhub", passwordVariable: "DockerhubPass", usernameVariable: "DockerUser")]) {
                    sh "docker login -u ${env.DockerhubUser} -p ${env.DockerhubPass}"
                    sh "docker tag python-img ${env.DockerhubUser}/python-img:latest"
                    sh "docker push ${env.DockerhubUser}/python-img:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                sh "yq eval '.spec.template.spec.containers[0].image = \"${env.DockerhubUser}/python-img:latest\"' -i deployments/deployment.yml"
            }
        }
    }
}
