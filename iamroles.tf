resource "aws_iam_role" "lambda_role" {
  name = "${var.prefix}-gft-lambda-role"

  assume_role_policy = <<-EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": [
            "lambda.amazonaws.com"
          ]
        },
        "Action": [
          "sts:AssumeRole"
        ]
      }
    ]
  }
EOF
  tags = {
    Owner = var.project_name
  }
}

resource "aws_iam_policy" "lambda_policy" {
  name = "${var.prefix}-gft-lambda-policy"

  policy = <<-EOF
{
    "Statement": [
        {
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Action" : [
                "ce:*"
                ],
                "Effect" : "Allow",
                "Resource": "*"
        },
        {
            "Action" : [
                "sqs:SendMessage",
                "sqs:DeleteMessage",
                "sqs:ChangeMessageVisibility",
                "sqs:ReceiveMessage",
                "sqs:TagQueue",
                "sqs:UntagQueue",
                "sqs:PurgeQueue",
                "sqs:GetQueueUrl"
                ],
                "Effect" : "Allow",
                "Resource" : "*"
        }
    ],
    
    "Version": "2012-10-17"
}
EOF
}