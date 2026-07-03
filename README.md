# Event-Driven Microservices with Apache Kafka and Docker

A simple, lightweight demonstration of an event-driven architecture using **Apache Kafka**, **Docker Compose**, and **Python**. This project simulates an e-commerce workflow where an **Order Service** (Producer) sends event messages to a Kafka topic, and a **Shipping Service** (Consumer) processes them concurrently in real-time.

## 🚀 Architecture Overview

- **Producers**: Microservices that publish events to Kafka topics (`producer.py`).
- **Kafka Broker**: The core event streaming engine running inside a Docker container.
- **ZooKeeper**: Handles cluster management, coordinator actions, and metadata tracking.
- **Consumers**: Microservices that subscribe to topics and process events asynchronously (`consumer.py`).

---

## 🛠️ Prerequisites

Ensure you have the following installed on your local machine:
- [Docker Desktop](https://docker.com)
- [Python 3.11+](https://python.org)

---

## 🏃‍♂️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com
cd YOUR_REPO_NAME
```

### 2. Start the Kafka Infrastructure
Launch the background Kafka and ZooKeeper infrastructure using Docker Compose:
```bash
docker compose up -d
```
*Verify that the containers are healthy by running `docker ps`.*

### 3. Install Python Dependencies
Install the required asynchronous Kafka client library:
```bash
pip install kafka-python-ng
```

### 4. Run the Consumer (Shipping Service)
Open a terminal window and start listening for real-time traffic:
```bash
python consumer.py
```

### 5. Run the Producer (Order Service)
Open a second terminal window and publish test events into the stream:
```bash
python producer.py
```

---

## 🧹 Clean Up
To stop the streaming servers and clear out background container resources:
```bash
docker compose down
```
