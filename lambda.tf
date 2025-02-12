resource "aws_lambda_function" "my_lambda" {
  function_name    = "trigger-api"
  role            = data.aws_iam_role.lambda.arn
  handler        = "lambda_function.lambda_handler"
  runtime        = "python3.9"
  timeout        = 10

  filename        = "lambda_function.zip"

  vpc_config {
    subnet_ids         = [aws_subnet.private.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}
