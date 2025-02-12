resource "aws_lambda_function" "lambda" {
  function_name = "MyLambdaFunction"
  filename      = "lambda_payload.zip"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"
  role          = data.aws_iam_role.lambda.arn

  vpc_config {
    subnet_ids         = [data.aws_subnet.private_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  environment {
    variables = {
      SUBNET_ID = data.aws_subnet.private_subnet.id
    }
  }
}
