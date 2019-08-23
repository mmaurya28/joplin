#!/usr/bin/env bash
set -eo pipefail
CURRENT_DIR=`dirname $BASH_SOURCE`
source $CURRENT_DIR/helpers.sh
log() { log_base "create_review_app" "$1" "$2"; }

# Attaches postgresql database to heroku application
function attach_heroku_database {
    heroku addons:create heroku-postgresql:hobby-dev --version=10 --app $APPNAME
}

print_header "Build Heroku Review App"
log 1 ">>> Deployment details:"
log 1 "Deploying new app:         ${APPNAME}"
log 1 "Into Pipeline:             ${PIPELINE_NAME}"

# If the review app exists, then check if database exists
APP_EXISTS=$(app_exists)
if [ "$APP_EXISTS" = "true" ]; then
  # If the review app exists, then add a database if it doesn't have one already
  log 2 "App $APPNAME already exists, tagging & checking if database exists.";
  APP_DB_EXISTS=$(app_database_attached)
  if [ "${APP_DB_EXISTS}" = "false" ]; then
      log 3 "No database detected, attaching new database to $APPNAME.";
      attach_heroku_database
      log 3 "Done attaching database."
  else
      log 2 "The database already exists."
  fi
else
  # Create a new Heroku review app, if the app doesn't already exist
  log 2 "Creating app ${APPNAME}";

  # Create app with specified APPNAME
  heroku create $APPNAME --team $PIPELINE_TEAM

  # Add postgresql to the new app
  attach_heroku_database

  # Attach new app to pipeline (assign review (PR) stage):
  heroku pipelines:add $PIPELINE_NAME --app $APPNAME --stage review
fi

# Add or update environment variables for review app
# Environment variables for staging and production are handled manually within Heroku Console
# Vars prefixed with "CI_" are sourced from circleci
# Suppress stdout with "> /dev/null" to hide display of sensitive variables
log 1 "Adding environment variables to Heroku App: $APPNAME"

heroku config:set   \
  APPLICATION_NAME=$APPNAME \
  AWS_S3_KEYID=$AWS_ACCESS_KEY_ID \
  AWS_S3_ACCESSKEY=$AWS_SECRET_ACCESS_KEY \
  AWS_S3_USER=$CI_AWS_S3_USER \
  AWS_S3_BUCKET_STATIC=$CI_AWS_S3_BUCKET_STATIC \
  AWS_S3_BUCKET_ARCHIVE=$CI_AWS_S3_BUCKET_ARCHIVE \
  AWS_S3_BUCKET_ARCHIVE_LOCATION=$CI_AWS_S3_BUCKET_ARCHIVE_LOCATION \
  CIRCLE_BRANCH=$CIRCLE_BRANCH \
  DEBUG=1 \
  HEROKU_JANIS_APP_NAME="janis-staging" \
  JANIS_URL="https://janis-staging.herokuapp.com" \
  STYLEGUIDE_URL="https://cityofaustin.github.io/digital-services-style-guide" \
  --app $APPNAME > /dev/null
