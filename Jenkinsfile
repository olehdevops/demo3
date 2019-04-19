#!groovy

pipeline {
  agent {
    kubernetes {
      label 'mypod'
      defaultContainer: 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: some-label-value
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
