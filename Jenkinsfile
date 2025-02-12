pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-token')
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main',
                        credentialsId: 'github-token',
                        url: "https://github.com/anuragsuraj23/devops-exam.git"
                }
            }
        }

        stage('Terraform Init & Apply') {
            steps {
                script {
                    sh '''
                    terraform init
                    terraform plan -out=tfplan
                    terraform apply -auto-approve tfplan
                    '''
                }
            }
        }

        stage('Package Lambda') {
            steps {
                script {
                    sh '''
                    zip lambda_payload.zip lambda_function.py
                    '''
                }
            }
        }

        stage('Deploy Lambda') {
            steps {
                script {
                    sh '''
                    aws lambda update-function-code --function-name my_lambda_function --zip-file fileb://lambda_payload.zip
                    '''
                }
            }
        }
    }
}
