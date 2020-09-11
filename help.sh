#!/usr/bin/env bash

jsTplPath="./frontend/translateToPigLatin.js.tpl"
jsFilePath="./frontend/translateToPigLatin.js"

buildJsFile() {
  if [[ -z "$TRANS_URL" ]]; then
    echo "TRANS_URL defaulting to http://127.0.0.1:8080/translate"
    export TRANS_URL="http://127.0.0.1:8080/translate"
    sed "s|{TRANS_URL}|'${TRANS_URL}'|g" $jsTplPath > $jsFilePath
  else
    sed "s|{TRANS_URL}|'${TRANS_URL}'|g" $jsTplPath > $jsFilePath
  fi
}

start() {
  export TRANS_URL="http://127.0.0.1:8080/translate"
  sed "s|{TRANS_URL}|'${TRANS_URL}'|g" $jsTplPath > $jsFilePath

  docker-compose build
  docker-compose up
}

start-backend() {
  docker-compose build backend
  docker-compose up backend
}

start-frontend() {
  if [[ -e $jsFilePath ]]; then
    docker-compose build frontend
    docker-compose up frontend
  elif [[ -n "$TRANS_URL" ]]; then
    sed "s|{TRANS_URL}|'${TRANS_URL}'|g" $jsTplPath > $jsFilePath
    docker-compose build frontend
    docker-compose up frontend
  else
    echo "TRANS_URL defaulting to http://127.0.0.1:8080/translate"
    export TRANS_URL="http://127.0.0.1:8080/translate"
    sed "s|{TRANS_URL}|'${TRANS_URL}'|g" $jsTplPath > $jsFilePath

    docker-compose build frontend
    docker-compose up frontend
  fi
}

$1