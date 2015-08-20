# Elasticsearch-Logstash-Kibana (ELK)
## ELK Stream for realtime Visual Analytics
Netflow is pushed to Logstash and decoded by the netflow filter codec. GeoIP lookup is performed in stream using the geoip filter which references a [MaxMind Datbase](http://dev.maxmind.com/geoip/legacy/geolite/).

You will also find in the [Real Time Stream Pipeline](./Real Time Stream Pipeline) directory the JSON files used to create the visualizations and dashboard in Kibana.

#### Setup Instructions
1. Follow references below to setup your Elasticsearch, Logstash, Kibana, and ES-Hadoop.
2. Copy netflow.conf file to "/etc/logstash/conf.d"
3. Restart Logstash `$bash> sudo service logstash restart`
4. Create Netflow Index in Elasticsearch `$bash> ./create_netflow_index.sh`
5. Start Netflow stream replay `$> replay_netflow_files.sh`(or point Netflow collector to the Logstash server and port)
6. Load Visualizatons and Dashboard using JSONs in [Kibana Directory](kibana)


## Stream to HDFS for Batch Analytics
In the [Long Term Data Pipeline](./Long Term Data Pipeline) directory you will find scripts to sto stream the data out of Elasticsearch using Hive. Registering the data as a new table and using Impala to query and create different views (i.e. edge list graphs for Gephi visualizations).

## Versions
* ELasticsearch [1.7] [(link)](https://www.elastic.co/products/elasticsearch)
* Logstash [1.5.3][(link)](https://www.elastic.co/products/logstash)
* Kibana [4.1][(link)](https://www.elastic.co/products/kibana)
* Elasticsearch for Apache Hadoop [2.1][(link)](https://www.elastic.co/products/hadoop)

## References
1. [Elasticsearch Documentation](https://www.elastic.co/guide/index.html)
2. [Step-by-Step Setup of ELK for NetFlow Analytics. Cisco Blog by Panos Kampanakis, 12/2/2014](http://blogs.cisco.com/security/step-by-step-setup-of-elk-for-netflow-analytics)
3. [Parsing Netflow using Kibana via Logstash to ElasticSearch, by Stephen Reese](https://www.rsreese.com/parsing-netflow-using-kibana-via-logstash-to-elasticsearch/)
