#!groovy

pipeline {
  agent {
    kubernetes {
      label 'mypod'
      podTemplate {
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
        container('python') {
          
          sh 'python --version'
        }
      }
    }
    stage('zip') {
      steps {
        container('zip') {
          
          sh 'zip -v'
        }
      }
    }
  }
}
