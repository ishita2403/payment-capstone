pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching Payment Engine source code...'
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Building and testing Payment Engine...'
                sh 'python3 --version'
                sh 'git --version'
                echo 'Initial environment checks passed!'
            }
        }
    }

    post {
        success {
            echo 'Jenkins Pipeline SUCCESSFUL!'
        }

        failure {
            echo 'Jenkins Pipeline FAILED!'
        }
    }
}