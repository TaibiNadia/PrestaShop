pipeline {
    agent { node { label 'ubuntu_slave' } }
    
    stages {
        stage('Test_unitaire') {
            steps {
                sh 'composer install -n'
                sh 'SYMFONY_DEPRECATIONS_HELPER=disabled composer unit-tests'
            }
        }
        stage(‘Build’) {
            steps { 
                sh 'docker build -t buid .'
            }
        }
        stage(‘Test_fonctionnel’) {
            steps { 
                sh 'docker-compose up -d'
                sh '/UI/test/docker-compose up'
                sh 'docker-compose stop'
            }
        }
        
    }
     
}
