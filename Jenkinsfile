pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        S3_BUCKET  = "467.devops.candidate.exam"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init -backend-config="bucket=${S3_BUCKET}" -backend-config="region=${AWS_REGION}"'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform plan'
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def subnet_id = sh(script: "terraform output -raw private_subnet_id", returnStdout: true).trim()
                    sh """
                    aws lambda invoke \
                        --function-name MyLambdaFunction \
                        --payload '{ "subnet_id": "${subnet_id}", "full_name": "Anurag Dangi", "email": "your-email@example.com" }' \
                        response.json
                    """
                }
            }
        }
    }
}
