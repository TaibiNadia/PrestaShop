pipeline {
    agent { node { label 'ubuntu_slave' } }
    
    stages {
        stage('Test_unitaire') {
            steps {
                sh 'composer install -n'
                sh 'SYMFONY_DEPRECATIONS_HELPER=disabled composer unit-tests'
            }
        }
        stage('Build') {
            steps { 
                sh 'docker build -t ps_build .'
            }
        }
        stage('Test_fonctionnel') {
            options {
                 timeout(time: 1, unit: 'HOURS') 
            }
            steps { 
                
                sh 'docker-compose up -d --force-recreate' // Start ENV 
                sh 'tests/UI/.docker/prestashop/wait-for-it.sh 10.10.20.71:8001 -s -t 1200 -- docker-compose up tests' // Wait and launch test
                /*sh 'docker-compose stop && docker-compose rm --force' // Clean ENV */
            } 
        }
    }
        
    post ('Test_Results') {
            always {
                echo 'I will always execute this!'
                junit keepLongStdio: true, testResults: '/home/jenkins/workspace/prestashop2/test-reports/*.xml' 
              
            }    
    }  
       
}
