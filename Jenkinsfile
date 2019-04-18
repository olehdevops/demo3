#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containers: {
        containerTemplate {
          name 'python'
          image 'python'
          ttyEnabled true
          command 'cat'    
          }
        containerTemplate {
          name 'zip'
          image 'kramos/alpine-zip'
          ttyEnabled true
          command 'cat'    
          }
      }
    }
  }
    stages {

        stage('python') {
            steps {
                sh 'python --version'
            }
        }
        stage('zip') {
            steps {
                sh 'zip -v'
            }
        }
        
    }


}
