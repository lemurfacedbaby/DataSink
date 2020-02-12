# DataSink

### Setup Instructions
- Have Kafka installed (https://www.apache.org/dyn/closer.cgi?path=/kafka/2.4.0/kafka_2.12-2.4.0.tgzinstalled)
- Have MinIO installed `brew install minio/stable/minio`

##### On Mac
- Install Python Requirements
` pip install -r requirements.txt`
- Add the Data Folder for Minio
` sudo mkdir data `
` sudo chown bgcooper data && sudo chmod u+rxw data `
- Start the MinIO server
` minio server data `
- Unpack Kafka
`tar -xzf kafka_2.12-2.4.0.tgz`
- Move to the Kafka directory
- Start the Zookeeper server
` bin/zookeeper-server-start.sh config/zookeeper.properties `
- Start the Kafka server
` bin/kafka-server-start.sh config/server.properties `
- Create a Topic
` bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test `
- Move to the Python directory
- Start the Python Producer Script
` python main.py <minio_url> `