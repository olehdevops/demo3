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
    }
  }
    stages {

        stage('zip') {
            steps {
                sh 'zip -v'
            }
        }
    }


}
