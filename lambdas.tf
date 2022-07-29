resource "null_resource" "install_python_dependencies" {
  provisioner "local-exec" {
    command = "bash ${path.module}/scripts/create_pkg.sh"

    environment = {
      source_code_path = "lambda_function"
      function_name    = "client-report-generator"
      path_module      = path.module
      runtime          = "python3.7"
      path_cwd         = path.cwd
    }
  }
}

data "archive_file" "create_pkg" {
  depends_on  = [null_resource.install_python_dependencies]
  source_dir  = "${path.module}/lambda_function/"
  output_path = "${path.module}/client-report-generator.zip"
  type        = "zip"
}

resource "aws_lambda_function" "aws_lambda" {
  function_name = "${var.prefix}-gft-report-generator"
  description   = "Generate cost consumption report"
  handler       = "lambda.lambda_handler"
  runtime       = "python3.7"

  role        = aws_iam_role.lambda_role.arn
  memory_size = 128
  timeout     = 60

  depends_on       = [null_resource.install_python_dependencies]
  source_code_hash = data.archive_file.create_pkg.output_base64sha256
  filename         = data.archive_file.create_pkg.output_path

  environment {
    variables = {
      region       = var.region
      sqs          = var.sqs
    }
  }
}

resource "aws_lambda_event_source_mapping" "example" {
  event_source_arn = var.sqs
  function_name    = aws_lambda_function.aws_lambda.function_name
}