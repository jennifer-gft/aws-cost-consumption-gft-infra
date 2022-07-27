terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }


  }
  backend "s3" {
    bucket = "gftcostconsumption-tfstate"
    key    = "gftccstate/terraform.tfstate"
    region = "eu-west-2"
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
}