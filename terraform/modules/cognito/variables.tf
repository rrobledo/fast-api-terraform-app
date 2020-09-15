variable "environment" {
  description = "The name of the environment"
}

variable "callback_urls" {
  description = "List of allowed callback URLs for the identity providers."
}

variable "logout_urls" {
  description = "List of allowed logout URLs for the identity providers."
}
