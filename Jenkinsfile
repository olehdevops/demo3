#!groovy

pipeline {
    agent {
        kubernetes {
          containerTemplate {
            name 'python'
            image 'python'
            ttyEnabled true
            command 'cat'    
          }
        //containerTemplate {
          //name 'zip'
          //image 'kramos/alpine-zip'
          //ttyEnabled true
          //command 'cat'    
          //}
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
