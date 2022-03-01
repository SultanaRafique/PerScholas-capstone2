pipeline {
  agent any
  stages {

    stage('Docker Build') {
      steps {
         sh 'docker build -t srafique001/capstone2:latest .'
      }
    }

    stage('Docker Login') {
        steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
            } 
        }
    }

     stage('Docker Push') {
        steps {
          sh 'docker push srafique001/capstone2:latest'
         } 
    }

    stage('Testing') {
        steps {
            echo 'Testing....'
         } 
    }

    stage('Deploying') {
        steps {

            sh """
            whoami
             ssh -v sultana@192.168.1.208 date 
             cd ~/learn-terraform-deploy-nginx-kubernetes
             terraform apply
            """
         } 
    }

    stage('Monitoring') {
        steps {
        echo 'Monitoring...'
         } 
    }

  }
}