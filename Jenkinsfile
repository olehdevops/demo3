#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containerTemplate {
        name 'python'
        image 'python'
        ttyEnabled true
        command 'cat'
        
        name 'zip'
        image 'kramos/alpine-zip'
        ttyEnabled true
        command 'cat'
       
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
