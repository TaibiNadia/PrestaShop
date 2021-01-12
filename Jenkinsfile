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
                sh 'docker build -t ps_build .'
            }
        }
        stage(‘Test_fonctionnel’) {
            steps { 
                
                sh 'docker-compose -f docker-compose.yml -f fun-tests/docker-compose.yml up -d'
                
                sh 'docker-compose stop'
            }
        }
        
    }
     
}
