#!usr/bin/env/python

# The main method will read from the s3 buckets
# The previous should be multithreaded using multiple s3 instances
# Each file/master record will be converted to a Kafka valid message.
# The previous has no issue multithreading with the same instance
# The Kafka producer will be configured with serialization.

# How is everything being stored in S3?
# Assume that the minio server is running on localhost:9000
# Assume that the kafka server is running on localhost:9092
# Assume that the topics have already been setup
# Send the info equally to each of the topics
# Question: How to setup the Kafka topics?
# Ans: Use serial machine ids (topic_id)

import boto3
from botocore.client import Config
import sys
from kafka import KafkaProducer

topics = ['topic_0', 'topic_1']

def produceMessage(a, p, t):
	p.send(t, a.encode())

if __name__ == "__main__":
	url = 'http://localhost:9000'
	if (len(sys.argv) != 1):
		url = sys.argv[1]
	# Connect to MinIO
	#s3 = boto3.resource('s3',
						#endpoint_url=url,
						#aws_access_key_id='minioadmin',
						#aws_secret_access_key='minioadmin',
						#config=Config(signature_version='s3v4'),
                    	#region_name='us-east-1')
	#s3.Bucket('test').download_file('mock.txt', '/Users/bgcooper/code/CSC492/DataSink/boi.txt')
	## value serializer determines how to convert data put in producer.send into a byte array
	producer = KafkaProducer(bootstrap_servers='localhost:9092')
	metric = producer.metrics()
	produceMessage('Hello world', producer, topics[0])
	print(metric)
