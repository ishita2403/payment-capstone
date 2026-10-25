pipeline {
    agent any

    environment {
        KUBECONFIG = '/var/jenkins_home/kubeconfig'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching Payment Engine source code...'
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                echo 'Running automated backend tests...'

                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r backend/requirements.txt pytest
                    .venv/bin/python -m pytest tests/ -v
                '''
            }
        }

        stage('Docker Packaging') {
            steps {
                echo 'Building application Docker images...'

                sh 'docker build -t payment-engine:capstone ./backend'
                sh 'docker build -t payment-frontend:capstone ./frontend'
            }
        }

        stage('Deploy Cluster') {
            steps {
                echo 'Deploying frontend and backend to Kubernetes...'

                sh 'kubectl apply -f capstone-stack.yaml'

                sh 'kubectl rollout status deployment/payment-backend --timeout=120s'
                sh 'kubectl rollout status deployment/payment-frontend --timeout=120s'

                sh 'kubectl get deployments'
                sh 'kubectl get services'
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
    }
}