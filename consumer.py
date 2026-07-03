import json
from kafka import KafkaConsumer

# Connect to the Kafka container running on localhost
consumer = KafkaConsumer(
    'orders',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("📦 Shipping Service started. Waiting for incoming orders...")

try:
    for message in consumer:
        order = message.value
        print(f"✈️  [SHIPPING] Processing Order ID: {order['order_id']} | Item: {order['item']} (${order['price']})")
except KeyboardInterrupt:
    print("\nStopping Shipping Service...")
