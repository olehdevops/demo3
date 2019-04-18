#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containerTemplate {
        name 'zip'
        image 'kramos/alpine-zip'
        ttyEnabled true
        command 'cat'
       
      }
      containerTemplate {
        name 'python'
        image 'python'
        ttyEnabled true
        command 'cat'
 
      }
    }
  }
    stages {

        stage('zip') {
            steps {
                sh 'zip -v'
            }
        }
        stage('python') {
            steps {
                sh 'python --version'
            }
        }
    }


}
