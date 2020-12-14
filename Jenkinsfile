pipeline {
 
  agent {
    label 'presta_docker_slave'
  }
 
  stages {

    stage('Tests unitaires') {

      steps {
        sh 'composer install'
        sh 'composer test-all'
      }
    }
  }
}
