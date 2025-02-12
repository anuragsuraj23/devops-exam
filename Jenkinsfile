pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = credentials('github-token')  // Use stored GitHub token
        AWS_REGION = 'ap-south-1'
        S3_BACKEND = '467.devops.candidate.exam'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git credentialsId: 'github-token', url: 'https://github.com/anuragsuraj23/devops-exam.git', branch: 'main'
                }
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init -backend-config="bucket=${S3_BACKEND}"'
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

        stage('Package Lambda') {
            steps {
                sh 'zip -r lambda_payload.zip lambda_function.py'
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def subnet_id = sh(script: "terraform output -raw private_subnet_id", returnStdout: true).trim()
                    sh "aws lambda invoke --function-name MyLambdaFunction --payload '{\"subnet_id\": \"${subnet_id}\", \"full_name\": \"Anurag Dangi\", \"email\": \"anurag@example.com\"}' response.json"
                }
            }
        }
    }
}
