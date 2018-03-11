#!/usr/bin/env bash
rm -rf /tmp/checkpoint_v01
spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 tkf/interfaces/consumer.py