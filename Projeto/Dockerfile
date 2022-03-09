FROM solr:8.10

COPY solr/music.json /data/music.json

COPY clean_dataset/albums.csv /data/albums.csv

COPY clean_dataset/artists.csv /data/artists.csv

COPY clean_dataset/songs.csv /data/songs.csv

COPY solr/startup_docker.sh /scripts/startup.sh

COPY scripts/aliases.txt /data/aliases.txt

ENTRYPOINT ["/scripts/startup.sh"]
