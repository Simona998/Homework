variable "base_name" {
  type = string
  default = "task"
}
variable "location" {
  type = string
  default = "eastus"
}
variable "my_public_ip"{
    type = string
    default = "46.217.114.162"
}
variable "my_password" {
  type = string
  default = "adminpassword123!"
}
variable "vms_subnet_id"{
    type = string 
    default =  "10.0.1.0/24"
}