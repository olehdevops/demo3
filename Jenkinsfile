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
  - name: terraform
    image: hashicorp/terraform
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

    stage("zip"){
      steps {
      container('zip'){

        sh "zip -v"
        sh "zip -j app.zip main.py requirements.txt"
        }
      }
    }

    stage('Checkout') {
      steps{
        container('terraform'){
          withCredentials([file(credentialsId: 'terraform-auth', variable: 'SVC_ACCOUNT_KEY')]) {
            sh 'ls -al $SVC_ACCOUNT_KEY'
            echo "My secret text is '${SVC_ACCOUNT_KEY}'"
            sh 'mkdir -p creds'
            sh "cp \$SVC_ACCOUNT_KEY ./keys/gcp-key.json"
          }
        }
      }
    }


    stage("TF plan"){
      steps {
      container('terraform'){

        sh "terraform version"
        sh "terraform init"
        sh "terraform plan -out myplan"
        
        }
      }
    }
    stage("TF Apply") {
      steps {
        container("terraform") {
          sh "terraform apply -input=false myplan"
        }
      }
    }
  }
}
