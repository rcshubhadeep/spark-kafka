# spark-kafka

This is an example repo featuring code to show different aspects of Stream Processing using [Apache Kafka](https://kafka.apache.org/)
and [Apache Spark](https://spark.apache.org/docs/latest/index.html). It has few interesting features. e.g.

* It has various different examples of producer and consumer (Plain Text, JSON, Apache Avro)

* It follows closely [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html)
by Martin Flower, thus making is extremely flexible to be extended and re-used. I can even make a case that one 
can easily use this as a template to create bigger production level applications.

* It shows some different use cases of Stream Processing.

## Installation

To install this repo - 

1.> Clone this repo

2.> Create a virtualenv and activate it.

3.> Once the virtualenv is activated run `pip install -r requirements.txt` 

4.> And then run `pip install -e .`

The above steps will install required libraries to run this project and also a local spark instance.
As now we can install `pyspark` using `pip`

However to install Kafka and other related confluent softwares the steps are following - 

1.> Ensure you have JAVA installed. (check using - `java -version`. In my case, I had 'openjdk version "1.8.0_151"')

2.> Download the Kafka tgz file from [here](https://www.apache.org/dyn/closer.cgi?path=/kafka/1.0.1/kafka_2.11-1.0.1.tgz)

3.> Unzip it in a directory.

4.> Open two terminals and input the following commands exactly in that order in each of them (you have to be in the Kafka dir that you just unzipped)

    
    bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties
    
5.> Download the latest confluent platform [here](https://www.confluent.io/download/) (Choose the Open Source version)

6.> Unzip it somewhere

7.> Open a new terminal. Navigate to that dir and then run the following command

    
    bin/schema-registry-start etc/schema-registry/schema-registry.properties
    
After these steps are done you are ready to roll. My usual setup looks like the image following - 

![Usual Setup](usual_setup.png)

__All these steps involving Kafka and other related softwares are going to run the entire setup in your 
local machine. As a single node setup. You can, however, set them up in a remote server / cluster if you so wish.
That practically changes nothing to the code; almost.__

## To test some producer and consumers

The code in this basic example project is almost self sufficient. If you have followed properly the instructions above then you need not to setup or configure anything else. Assuming that you had indeed followed the process of initial set up and had been successful in doing so here is what you need to do to run a sliding window based producer and consumer.

* Start two terminals.

* Activate the virtualenv that you had created and installed all the libraries and this package into

* from the first one issue this command - `./bin/start_consumer.sh`

* Wait few sec until it goes into consumption.

* Now, from the second terminal, issue this command - `./bin/start_producer.sh` 

* You will see the total number of visited event is getting reported on a sliding window based manner in the consumer terminal while the producer keeps on producing the messages.

* Additionally, if you want to experiment with other consumer and producers, you can do so. The scripts in the `interfaces` package uses [Python Fire](https://github.com/google/python-fire) as an entry point to the function they expose with the type of producer and/or consumer and the topic name totally configurable as a command line option. For an example to start a simple text (JSON) based consumer and producer you can issue the following commands in the same order as depicted - 


        spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 tkf/interfaces/consumer.py --consumer_type=simple_spark --topic_name=test2
        python tkf/interfaces/producer.py --producer_type=simple --topic_name=test2


## Improvement

To use this as a template for production grade projects you need to, at least, do the two following things -

* Implement a centralized anc configurable logging.

* Implement Configuration management.

## Conclusion

The code in this example repo is not doing anything complicated. The primary focus of this repo is to accompany my Medium post about Stream Processing. However, thanks to Clean Architecture, this code can be easily adapted as the template of any production grade project.