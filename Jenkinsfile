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
            }
        }
    }

    post {
        success {
            echo 'All automated tests PASSED!'
        }

        failure {
            echo 'Pipeline FAILED!'
        }
    }
}