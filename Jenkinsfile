#!groovy

pipeline {
  agent {
    kubernetes {
      label 'mypod'
      containerTemplates {
        containerTemplate {
          name 'python'
          image 'python'
          ttyEnabled true
          command 'cat'
        }
        
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
