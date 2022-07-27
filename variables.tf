variable "region" {
  type = string
}

variable "environment" {
  type    = string
  default = "gft"
}

variable "vpc_cidr" {
  type        = string
  default     = "192.168.0.0/22"
  description = "cidr range"
}

variable "public_subnets_cidr" {
  type        = list(any)
  description = "public cidr"
  default     = ["192.168.2.0/25", "192.168.2.128/25"]
}

variable "private_subnets_cidr" {
  type        = list(any)
  description = "private cidr"
  default     = ["192.168.0.0/24", "192.168.1.0/24"]
}

variable "availability_zones" {
  type        = list(any)
  description = "AZ of the region"
  default     = ["eu-west-2a", "eu-west-2b", "eu-west-2c"]
}
########
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