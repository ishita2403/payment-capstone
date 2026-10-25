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
                echo 'Running Payment Engine automated tests...'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r backend/requirements.txt pytest
                    .venv/bin/python -m pytest tests/ -v
                '''

                echo 'All backend tests completed!'
            }
        }

        stage('Docker Packaging') {
            steps {
                echo 'Building Payment Engine Docker images...'

                sh 'docker build -t payment-engine:capstone ./backend'

                sh 'docker build -t payment-frontend:capstone ./frontend'

                echo 'Docker images built successfully!'
            }
        }
    }

    post {
        success {
            echo 'CAPSTONE PIPELINE SUCCESSFUL!'
        }

        failure {
            echo 'CAPSTONE PIPELINE FAILED!'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}