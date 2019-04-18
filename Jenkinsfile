#!groovy

pipeline {
    agent {kubernetes true
}
    stages {
        stage('build') {
            steps {
                sh 'python unit-test.py'
            }
        }

        stage('zip') {
            steps {
                sh 'zip -v'
            }
        }
    }


}
