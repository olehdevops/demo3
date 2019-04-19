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
  name: mypod
spec:
  containers:
  - name: python
    image: python
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
    
   
  }
}
