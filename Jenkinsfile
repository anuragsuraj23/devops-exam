pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/anuragsuraj23/devops-exam.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init -force-copy'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform plan -out=tfplan'
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve tfplan'
            }
        }

        stage('Invoke Lambda') {
            steps {
                script {
                    def lambdaFunctionName = "trigger-api"
                    def invokeCommand = """
                    aws lambda invoke --function-name ${lambdaFunctionName} --region ${AWS_REGION} \
                    --payload '{ "subnet_id": "subnet-xyz", "full_name": "Anurag Dangi", "email": "your.email@example.com" }' response.json
                    cat response.json
                    """
                    sh invokeCommand
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}
