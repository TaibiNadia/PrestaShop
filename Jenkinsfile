pipeline {
    agent {
        docker { image 'ladynadoo/prestashop' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'composer install -n'
                sh 'SYMFONY_DEPRECATIONS_HELPER=disabled composer unit-tests'
            }
        }
        stage(‘Build’) {
            steps {
                sh 'docker-compose up --build'
            }
        } 
    }
     
}
