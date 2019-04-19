pipeline {
  agent {
    kubernetes {
      label 'mypod'
      defaultContainer 'jnlp'
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

    stage('Clone repo') {
      steps {
      checkout([$class: 'GitSCM', branches: [[name: '*/test1']],
        userRemoteConfigs: [[url: 'https://github.com/olehdevops/demo3.git']]])
      }
    }
    stage("python"){
      steps {
      container("python"){
        sh "python --version"
          sh "python unit-test.py"
        }
      }
    }

    stage("run in other container"){
      steps {
      container('zip'){

        sh "zip -v"
        sh "zip -j app.zip main.py requirements.txt"
        }
      }
    }
  }
}
