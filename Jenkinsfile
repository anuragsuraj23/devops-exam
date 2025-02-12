pipeline {
    agent any
    environment {
        AWS_REGION = 'ap-south-1'
        S3_BUCKET  = '467.devops.candidate.exam'
    }
    stages {
        stage("TF Init") {
            steps {
                sh 'terraform init -backend-config="bucket=${S3_BUCKET}" -backend-config="region=${AWS_REGION}"'
            }
        }
        stage("TF Validate") {
            steps {
                sh 'terraform validate'
            }
        }
        stage("TF Plan") {
            steps {
                sh 'terraform plan'
            }
        }
        stage("TF Apply") {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }
        stage("Invoke Lambda") {
            steps {
                sh 'aws lambda invoke --function-name trigger-api-function response.json'
                sh 'cat response.json'
            }
        }
    }
}
