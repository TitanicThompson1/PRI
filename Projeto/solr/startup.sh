#!/bin/bash

docker exec my_solr bin/solr start -e techproducts -Dsolr.ltr.enabled=true

# Add core
docker exec my_solr bin/solr delete -c musics
docker exec my_solr bin/solr create_core -c musics


# Add schema
curl -X POST -H 'Content-type:application/json' \
    --data-binary @music.json \
    http://localhost:8983/solr/musics/schema


# Populate core
curl -X POST -H 'Content-type:application/csv' \
    --data-binary @../clean_dataset/songs.csv \
    http://localhost:8983/solr/musics/update?commit=true

curl -X POST -H 'Content-type:application/csv' \
    --data-binary @../clean_dataset/albums.csv \
    http://localhost:8983/solr/musics/update?commit=true

curl -X POST -H 'Content-type:application/csv' \
    --data-binary @../clean_dataset/artists.csv \
    http://localhost:8983/solr/musics/update?commit=true