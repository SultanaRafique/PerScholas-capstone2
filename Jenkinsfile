pipeline {
  agent any
  stages {

    stage('Docker Build') {
      steps {
         bat 'docker build -t srafique001/capstone2:latest .'
      }
    }

    stage('Docker Login') {
        steps {
        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          bat "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
            } 
        }
    }

     stage('Docker Push') {
        steps {
          bat 'docker push srafique001/capstone2:latest'
         } 
    }

    stage('Testing') {
        steps {
            echo 'Testing....'
         } 
    }

    stage('Deploying') {
        steps {
            bat 'ssh sultana@192.168.1.208  terraform apply'
         } 
    }

    stage('Monitoring') {
        steps {
        echo 'Monitoring...'
         } 
    }

  }
}