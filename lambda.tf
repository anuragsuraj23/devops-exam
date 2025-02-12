resource "aws_lambda_function" "my_lambda" {
  function_name    = "my-lambda-function"
  role            = aws_iam_role.lambda_exec.arn
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.8"
  timeout         = 30

  filename        = "lambda_payload.zip"

  environment {
    variables = {
      API_URL = "https://bc1yy8dzsg.execute-api.eu-west-1.amazonaws.com/v1/data"
    }
  }
}
