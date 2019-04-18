#!groovy

pipeline {
    agent {
        kubernetes true
        }
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
