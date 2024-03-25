#!/usr/bin/env bash

# Ensure jq is installed
if ! command -v jq &> /dev/null
then
    echo "jq could not be found. Attempting to install."
    # Use apt-get for Debian/Ubuntu, modify if using a different package manager
    sudo apt-get update && sudo apt-get install -y jq
fi

# Path to the JSON file with database credentials
CREDENTIALS_FILE="db_creds.json"

DB_NAME=$(jq -r '.db_name' $CREDENTIALS_FILE)
DB_USER=$(jq -r '.db_user' $CREDENTIALS_FILE)
DB_PASSWORD=$(jq -r '.db_password' $CREDENTIALS_FILE)
DB_HOST=$(jq -r '.db_host' $CREDENTIALS_FILE)
DB_PORT=$(jq -r '.db_port' $CREDENTIALS_FILE)

# Display the credentials (optional, for debugging purposes)
echo "Database Name: $DB_NAME"
echo "Database User: $DB_USER"
echo "Database Password: $DB_PASSWORD"
echo "Database Host: $DB_HOST"
echo "Database Port: $DB_PORT"

# Connect to PostgreSQL and execute commands
# Create a new PostgreSQL database
echo "Creating database: $DB_NAME"
psql -h $DB_HOST -p $DB_PORT -U postgres -c "CREATE DATABASE \"$DB_NAME\";"

# Create a new user and set the password
echo "Creating user: $DB_USER"
psql -h $DB_HOST -p $DB_PORT -U postgres -c "CREATE USER \"$DB_USER\" WITH PASSWORD '$DB_PASSWORD';"

# Grant all privileges of the new database to the new user
echo "Granting privileges to user $DB_USER on database $DB_NAME"
psql -h $DB_HOST -p $DB_PORT -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE \"$DB_NAME\" TO \"$DB_USER\";"

# Grant CREATE privilege on the public schema to the new user
echo "Granting CREATE privilege on public schema to $DB_USER"
psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U postgres -c "GRANT CREATE ON SCHEMA public TO \"$DB_USER\";"

psql -h $DB_HOST -p $DB_PORT -d $DB_NAME -U postgres -c "ALTER SCHEMA public OWNER TO \"$DB_USER\";"

echo "Database and user setup completed."
