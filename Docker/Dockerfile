FROM docker.elastic.co/elasticsearch/elasticsearch:7.11.1

RUN elasticsearch-plugin install analysis-kuromoji
RUN elasticsearch-plugin install analysis-icu
RUN elasticsearch-plugin install -b https://github.com/vvanholl/elasticsearch-prometheus-exporter/releases/download/7.11.1.0/prometheus-exporter-7.11.1.0.zip