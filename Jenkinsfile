pipeline {
    agent {
        docker { image 'ladynadoo/prestashop' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'composer install -n'
                sh 'composer test-all'
            }
        }
    }
}
