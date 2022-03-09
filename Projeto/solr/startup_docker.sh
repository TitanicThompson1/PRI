#!/bin/bash

sleep 3

precreate-core musics

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/musics.json \
    http://localhost:8983/solr/courses/schema

sleep 1

# Populate collection
bin/post -c musics /data/albums.csv
sleep 1

bin/post -c musics /data/artists.csv
sleep 1

bin/post -c musics /data/songs.csv
sleep 1

# Restart in foreground mode so we can access the interface
solr restart -f
