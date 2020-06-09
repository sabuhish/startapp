prestart = """
#! /usr/bin/env bash

# Let the DB start
echo "db_driver://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
until db_driver "db_driver://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}" -c '\q'; do
  >&2 echo "Database is unavailable - sleeping"
  sleep 1
done


# Run migrations
alembic upgrade head

"""
