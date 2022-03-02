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

            sh ' cd /home/sultana/learn-terraform-deploy-nginx-kubernetes && terraform apply -auto-approve -lock=false'
            
         } 
    }

    stage('Monitoring') {
        steps {
        echo 'Monitoring...'
         } 
    }

  }
}