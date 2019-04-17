#!groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python unit-test.py'
            }
        }

        stage('zip') {
            steps {
                sh './filezip.sh app.zip main.py, requirements.txt'
            }
        }
    }


}