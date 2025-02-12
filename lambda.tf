resource "aws_lambda_function" "lambda" {
  function_name    = "MyLambdaFunction"
  filename         = "lambda_payload.zip"
  source_code_hash = filebase64sha256("lambda_payload.zip")
  role             = data.aws_iam_role.lambda.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"
  vpc_config {
    subnet_ids         = [aws_subnet.private.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}
