#!/bin/sh
NF_REPLAY_DELAY=1000
NF_PORT=12345
LOGSTASH_SERVER=staging1
NFCAPD_DIR="./ingest/"

for x in `ls -1 $NFCAPD_DIR/nfcapd.*`
  do nfreplay -d $NF_REPLAY_DELAY -H $LOGSTASH_SERVER -p $NF_PORT -r $x
  echo "Replayed $x"
done
