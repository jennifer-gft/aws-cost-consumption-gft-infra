variable "region" {
  type = string
}

variable "rds_vpc_id" {
  default = "vpc-0a2c89c0f7c6305e8"
  description = "Our default RDS virtual private cloud (rds_vpc)."
  type = string
}

variable "rds_public_subnets" {
  default = "subnet-005c9506988c1a4c6,subnet-01beaafbc576f96ab,subnet-0d806aad769b41878"
  description = "The public subnets of our RDS VPC rds-vpc."
}

variable "rds_public_subnet_group" {
  default = "default"
  description = "Apparently the group name, according to the RDS launch wizard."
}

variable "db_username" {
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}