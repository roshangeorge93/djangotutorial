#!/bin/bash
set -e
cmd="$@"

if [ -z "$DATABASE_URL" ]; then
    export DATABASE_URL=postgres://postgres:password@postgres:5432/postgres
fi

function postgres_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect("$DATABASE_URL")
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

# Keep the container up without running the server. Comment the following if using in production.
sleep infinity

# # Run Django migrations
# echo "Applying migrations..."
# python /app/manage.py migrate --noinput

# # Collect static files
# echo "Collecting static files..."
# python /app/manage.py collectstatic --noinput

# # Start the application
# exec "$cmd"