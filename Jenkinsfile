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
                
                sh 'docker-compose up -d --force-recreate' // Start ENV 
                sh 'tests/UI/.docker/prestashop/wait-for-it.sh --timeout=600 --strict localhost:8001 -- docker-compose up tests' // Wait and launch test
                /*sh 'docker-compose stop && docker-compose rm --force' // Clean ENV */
            }
        }
        
              
    }
     
}
