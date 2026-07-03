import json
import time
from kafka import KafkaProducer

# Connect to the Kafka container
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🛒 Order Service initialized.")

# Simulate sending 3 different orders
for i in range(1, 4):
    order_data = {
        "order_id": f"ORD-100{i}",
        "item": f"Gadget-{i}",
        "price": round(19.99 * i, 2)
    }
    
    print(f"📝 Placing order for {order_data['item']}...")
    producer.send('orders', value=order_data)
    time.sleep(1) # Pause 1 second between orders

# Force send any buffered messages
producer.flush()
print("✅ All orders sent to Kafka successfully!"
