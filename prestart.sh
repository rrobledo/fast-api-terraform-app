#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
ls -la
cd /app
ls -la
alembic upgrade head
cd -
