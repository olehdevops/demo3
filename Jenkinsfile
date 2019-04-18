#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containerTemplate {
        name 'zip'
        image 'kramos/alpine-zip'
        ttyEnabled true
       
      }
      containerTemplate {
        name 'python'
        image 'python'
        ttyEnabled true
 
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
