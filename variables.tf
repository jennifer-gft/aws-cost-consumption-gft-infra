variable "region" {
  type = string
  default = "eu-west-2"
}

variable "environment" {
  type = string
  default = "gft"
}

variable "vpc_cidr" {
  type = string
  default = "192.168.0.0/22"
  description = "cidr range"
}

variable "public_subnets_cidr" {
  type = list
  description = "public cidr"
  default = ["192.168.2.0/25","192.168.2.128/25"]
}

variable "private_subnets_cidr" {
  type = list
  description = "private cidr"
  default = ["192.168.0.0/24","192.168.1.0/24"]
}

variable "availability_zones" {
  type = list
  description = "AZ of the region"
  default = ["eu-west-2a","eu-west-2b","eu-west-2c"]
}