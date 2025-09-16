pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/syedtalhahamid/ecomm-devops.git' }
    }
    stage('Build Docker') {
      steps { sh 'docker build -t myshop:v1 .' }
    }
    stage('Push DockerHub') {
      steps { sh 'docker push myshop:v1' }
    }
    stage('Deploy with Ansible') {
      steps { sh 'ansible-playbook -i ansible/hosts.ini ansible/playbook.yml' }
    }
  }
}
