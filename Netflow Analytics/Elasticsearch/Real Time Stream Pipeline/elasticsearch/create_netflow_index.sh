#!/bin/sh

# Delete Existing Index
curl -XDELETE 'http://scc:9200/netflow/'

# Create the netflow index
curl -XPUT 'http://scc:9200/netflow/' -d ' {
      "settings" : {
          "index" : {
              "number_of_shards" : 25,
              "number_of_replicas" : 1
          }
      }
}'

# Create a mapping for netflow geo_point data
curl -XPUT 'http://scc:9200/netflow/_mapping/logs' -d ' {
     "logs" : {
         "properties" : {
             "src_coords": {"type":"geo_point"},
             "dst_coords": {"type":"geo_point"}
        }
    }
}'

#  Default string fields to "not_analyzed"
curl -XPUT 'http://scc:9200/netflow/_mapping/logs' -d '
{
    "logs": {
        "dynamic_templates": [
            { "notanalyzed": {
                  "match":              "*",
                  "match_mapping_type": "string",
                  "mapping": {
                      "type":        "string",
                      "index":       "not_analyzed"
                  }
               }
            }
          ]
       }
}'
