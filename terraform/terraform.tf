terraform {
  backend "remote" {
    organization = "rrobledo"

    workspaces {
      name = "nexton-challenge"
    }
  }
}
