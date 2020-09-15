resource "aws_db_subnet_group" "postgres-db-subnet-group" {
  name_prefix = "${var.environment}-postgres-db-subnet-group"
  subnet_ids  = var.subnet_ids
}

resource "aws_security_group" "postgres-sg" {
  name        = "${var.environment}-postgres-sg"
  description = "Used in Postgres"
  vpc_id      = var.vpc_id

  tags = {
    Environment   = var.environment
  }
}

resource "aws_security_group_rule" "outbound_postgres_access" {
  type              = "egress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.postgres-sg.id
}

resource "aws_security_group_rule" "inbound_postgres_access" {
  type              = "ingress"
  from_port         = 5432
  to_port           = 5432
  protocol          = "TCP"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.postgres-sg.id
}

resource "aws_db_instance" "postgres" {
  identifier                      = "db-${var.environment}"

  engine                          = "postgres"
  engine_version                  = var.engine_version
  instance_class                  = var.instance_class
  allocated_storage               = 5
  storage_encrypted               = var.storage_encrypted
  storage_type                    = var.storage_type

  name                            = var.name
  username                        = var.username
  password                        = var.password
  iam_database_authentication_enabled = var.iam_database_authentication_enabled

  vpc_security_group_ids          = [aws_security_group.postgres-sg.id]
  db_subnet_group_name            = aws_db_subnet_group.postgres-db-subnet-group.name
}
