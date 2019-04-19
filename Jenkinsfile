#!groovy

pipeline {
  agent {
    kubernetes {
      label 'mypod'
      yaml 
"""
apiVersion: v1
kind: Pod
metadata:

spec:
  containers:
  - name: python
    image: python
    command:
    - cat
    tty: true
  - name: zip
    image: kramos/alpine-zip
    command:
    - cat
    tty: true
"""
    }
  }
  stages {
    stage('python') {
      steps {
        container('python') {
          sh 'python --version'
        }
        container('zip') {
          sh 'zip -v'
        }
      }
    }
  }
}
