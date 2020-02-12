# DataSink

### Setup Instructions
- Have Minio, Python, and kafka installed

##### On Mac
Install Python Requirements
` pip install -r requirements.txt`
Add the Data Folder for Minio
` sudo mkdir data `
` sudo chown bgcooper data && sudo chmod u+rxw data `
Start the MinIO server
` minio server data `
Move to the Kafka directory
` cd /Users/bgcooper/downloads/kafka_2.12-2.4.0 `
Start the Zookeeper server
` bin/zookeeper-server-start.sh config/zookeeper.properties `
Start the Kafka server
` bin/kafka-server-start.sh config/server.properties `
Create a Topic
` bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test `
Start the Python Producer Script
` python main.py <minio_url> `