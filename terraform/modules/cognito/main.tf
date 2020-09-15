resource "aws_cognito_user_pool" "pool" {
  name = "${var.environment}-user"
}

resource "aws_cognito_user_pool_domain" "main" {
  domain       = "rrobledo-${var.environment}"
  user_pool_id = aws_cognito_user_pool.pool.id
}

resource "aws_cognito_identity_provider" "google-provider" {
  user_pool_id  = aws_cognito_user_pool.pool.id
  provider_name = "Google"
  provider_type = "Google"

  provider_details = {
    authorize_scopes = "email"
    client_id        = "384564363979-37ghi3hriql540ue1sefu5qgetjpr4q3.apps.googleusercontent.com"
    client_secret    = "ZjQGLlO5feOgPUZeGw9MjslU"
  }

  attribute_mapping = {
    email    = "email"
    username = "sub"
  }
}

resource "aws_cognito_user_pool_client" "app-client" {
  name = "app-${var.environment}"
  user_pool_id = aws_cognito_user_pool.pool.id

  callback_urls = var.callback_urls
  logout_urls = var.logout_urls

  allowed_oauth_flows_user_pool_client = true
  allowed_oauth_flows = ["implicit"]
  allowed_oauth_scopes = ["email", "openid", "profile", "aws.cognito.signin.user.admin"]
  supported_identity_providers = ["Google"]

}
