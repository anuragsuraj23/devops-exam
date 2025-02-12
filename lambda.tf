resource "aws_lambda_function" "my_lambda" {
  function_name    = "my_lambda_function"
  role            = data.aws_iam_role.lambda.arn
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.8"
  filename        = "lambda_payload.zip"
  source_code_hash = filebase64sha256("lambda_payload.zip")
  vpc_config {
    subnet_ids         = [aws_subnet.private_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}
