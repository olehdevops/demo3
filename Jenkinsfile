#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containerTemplate {
        name 'python'
        image 'python'
        ttyEnabled true
        command 'cat'
       
      }
      
    }
  }
    stages {

        stage('python') {
            steps {
                sh 'python --version'
            }
        }
        
    }


}
