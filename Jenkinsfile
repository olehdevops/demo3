#!groovy

pipeline {
    agent {
    kubernetes {
      label 'declarative'
      containerTemplates {
          {name 'python'
           image 'python'
           ttyEnabled true
           command 'cat'},
          {name 'zip'
           image 'kramos/alpine-zip'
           ttyEnabled true
           command 'cat'}
       
      }
      
    }
  }
    stages {

        stage('python') {
            steps {
                sh 'python --version'
            }
        }
        tage('zip') {
            steps {
                sh 'zip -v'
            }
        }
        
    }


}
