pipeline {
    agent any
    environment {
        AWS_REGION = 'ap-south-1'
        LAMBDA_FUNCTION_NAME = 'trigger-api-function'
    }
    stages {
        stage("Checkout Code") {
            steps {
                git branch: 'main', url: 'https://github.com/anuragsuraj23/devops-exam.git'
            }
        }
        
        stage("Package Lambda") {
            steps {
                sh '''
                zip lambda_payload.zip lambda_function.py
                '''
            }
        }

        stage("Terraform Init") {
            steps {
                sh '''
                terraform init
                '''
            }
        }

        stage("Terraform Apply") {
            steps {
                sh '''
                terraform apply -auto-approve
                '''
            }
        }

        stage("Invoke Lambda") {
            steps {
                script {
                    def response = sh(script: '''
                        aws lambda invoke \
                            --function-name ${LAMBDA_FUNCTION_NAME} \
                            --log-type Tail \
                            --query 'LogResult' \
                            --output text \
                            response.json | base64 --decode
                        ''', returnStdout: true).trim()

                    echo "Lambda Response: ${response}"
                }
            }
        }
    }
}
