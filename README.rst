
配置 AWS MSK Kafka 集群
------------------------------------------------------------------------------

.. contents::
    :depth: 1
    :local:

1. 为 MSK Cluster 创建 VPC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




This runbook is primarily from https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html


.. code-block:: bash

    # install java, kafka bin tool depends on java
    sudo yum install java-1.8.0 -y

    # install kafka (and bin tool)
    cd ~
    wget https://archive.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
    tar -xzf kafka_2.12-2.2.1.tgz

    # set default region
    aws configure

    # create a topic
    msk_arn="arn:aws:kafka:us-east-1:669508176277:cluster/sanhe-dev/3d5b6e3a-6077-47b0-9e6f-e20e4a988e43-17"
    zk_conn_str="$(aws kafka describe-cluster --region us-east-1 --cluster-arn ${msk_arn} | jq '.ClusterInfo.ZookeeperConnectString' -r)"
    ~/kafka_2.12-2.2.1/bin/kafka-topics.sh --create --zookeeper "${zk_conn_str}" --replication-factor 3 --partitions 1 --topic AWSKafkaExample

    ~/kafka_2.12-2.2.1/bin/kafka-topics.sh --list --zookeeper "${zk_conn_str}"

.. code-block:: bash

    cp /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.amzn2.0.1.x86_64/jre/lib/security/cacerts /tmp/kafka.client.truststore.jks
    kafka_home="${HOME}/kafka_2.12-2.2.1"
    msk_arn="arn:aws:kafka:us-east-1:669508176277:cluster/sanhe-dev/3d5b6e3a-6077-47b0-9e6f-e20e4a988e43-17"
    broker_str="$(aws kafka get-bootstrap-brokers --region us-east-1 --cluster-arn ${msk_arn} | jq '.BootstrapBrokerStringTls' -r)"
    ${kafka_home}/bin/kafka-console-producer.sh --broker-list "${broker_str}" --producer.config client.properties --topic AWSKafkaExample

.. code-block:: bash

    ${kafka_home}/bin/kafka-console-consumer.sh --bootstrap-server "${broker_str}" --consumer.config ${kafka_home}/bin/client.properties --topic AWSKafkaExample --from-beginning



    aws kafka get-bootstrap-brokers --cluster-arn ${msk_arn}


