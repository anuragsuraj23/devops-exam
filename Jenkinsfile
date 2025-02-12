pipeline {
    agent any
    environment {
        AWS_REGION = 'ap-south-1'
    }
    stages {
        stage('Init') {
            steps {
                sh 'terraform init -force-copy'
            }
        }
        stage('Plan') {
            steps {
                sh 'terraform plan -out=tfplan'
            }
        }
        stage('Apply') {
            steps {
                sh 'terraform apply -auto-approve tfplan'
            }
        }
        stage('Invoke Lambda') {
            steps {
                script {
                    def lambda_response = sh(
                        script: """aws lambda invoke --function-name trigger-api --payload '{ "subnet_id": "subnet-xyz", "full_name": "Anurag Dangi", "email": "your@email.com" }' response.json""",
                        returnStdout: true
                    )
                    echo "Lambda Invocation Response: ${lambda_response}"
                    sh 'cat response.json'
                }
            }
        }
    }
}
