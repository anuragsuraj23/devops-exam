terraform {
  backend "s3" {
    bucket         = "467.devops.candidate.exam"
    key            = "terraform/state"
    region         = "ap-south-1"
    encrypt        = true
  }
}

provider "aws" {
  region = "ap-south-1"
}
