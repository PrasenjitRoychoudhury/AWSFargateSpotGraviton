import random
import time
import signal
import sys
import time
import datetime
import csv
import boto3
from io import StringIO

def sigterm_handler(signum, frame):
    print("Received SIGTERM2. Shutting down gracefully...")
    current_time = datetime.datetime.fromtimestamp(time.time())
    print(f"SIGTERM2 Current time: {current_time}")
    time.sleep(30)
    current_time = datetime.datetime.fromtimestamp(time.time())
    s3 = boto3.client('s3')
    s3.delete_object(Bucket=bucket_name, Key=file_name)
    print("SIGTERM2 Received. File is deleted...")
    print("SIGTERM2 Received SIGTERM2. Shutting down completed...")
    # Perform cleanup operations here
    # Perform SNS notification from here
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

def write_linkedlist_to_s3(linked_list, bucket_name, file_name):
    # Create a CSV file in memory
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    
    # Write header
    writer.writerow(['Name', 'Age'])
    
    print(f"linked_list+: {linked_list}")
    print(f"bucket_name+: {bucket_name}")
    print(f"file_name+: {file_name}")


    # Write data from linked list
    current = linked_list.head
    while current:
        writer.writerow([current.name, current.age])
        current = current.next
    
    # Create an S3 client
    s3_client = boto3.client('s3')
    
    # Upload the file to S3
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=csv_buffer.getvalue()
        )
        print(f"Successfully uploaded linked list data to {bucket_name}/{file_name}")
    except Exception as e:
        print(f"Error uploading to S3: {str(e)}")

class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, name, age):
        new_node = Node(name, age)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        while current:
            print(f"Name: {current.name}, Age: {current.age}")
            current = current.next

# Create a linked list
linked_list = LinkedList()
bucket_name = "prc-cw-anomaly-detection-lab-07092024"
file_name = "linked_list_data.txt"

# Generate and add nodes with random names and ages
names = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
for _ in range(10):
    name = random.choice(names)
    age = random.randint(18, 60)
    linked_list.add_node(name, age)

# write the code to find the sum of the ages of all the nodes

sum = 0     

current = linked_list.head

while current:
    sum += current.age
    current = current.next

# print the sum
# write the code to find the sum of the ages of all the nodes


print("Hello World17 arm64")
current_time = datetime.datetime.fromtimestamp(time.time())
print(f"Current time: {current_time}")
time.sleep(1)
current_time = datetime.datetime.fromtimestamp(time.time())
print(f"Current time+: {current_time}")
print(sum)



# Traverse and print the nodes
linked_list.traverse()
# write_linkedlist_to_s3(linked_list, bucket_name, file_name)



