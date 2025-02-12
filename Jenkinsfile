pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        S3_BUCKET = "467.devops.candidate.exam"
        API_URL = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_GITHUB_REPO'
            }
        }

        stage('Setup Terraform') {
            steps {
                sh '''
                terraform init -backend-config="bucket=${S3_BUCKET}" -backend-config="region=${AWS_REGION}"
                terraform plan -out=tfplan
                '''
            }
        }

        stage('Apply Terraform') {
            steps {
                sh 'terraform apply -auto-approve tfplan'
            }
        }

        stage('Prepare Lambda Deployment') {
            steps {
                sh '''
                rm -f lambda_payload.zip
                zip lambda_payload.zip lambda_function.py
                '''
            }
        }

        stage('Deploy Lambda Function') {
            steps {
                sh '''
                aws lambda update-function-code --function-name my-lambda-function --zip-file fileb://lambda_payload.zip --region ${AWS_REGION}
                '''
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def response = sh(
                        script: '''
                        aws lambda invoke --function-name my-lambda-function --payload '{"subnet_id": "subnet-1234abcd", "full_name": "Anurag Dangi", "email": "your.email@example.com"}' response.json --region ${AWS_REGION}
                        cat response.json
                        ''',
                        returnStdout: true
                    )
                    echo "Lambda Response: ${response}"
                }
            }
        }
    }

    post {
        always {
            sh 'terraform destroy -auto-approve'
        }
    }
}
