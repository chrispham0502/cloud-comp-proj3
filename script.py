#Triet Pham

import os
import socket
from collections import Counter

# a. List name of all text files

file_names = os.listdir('/home/data')
# Filter only the .txt files
txt_files = [file for file in file_names if file.endswith('.txt')]

# b. Read and count words in each text file
word_counts = Counter()
for txt_file in txt_files:
    with open(txt_file, 'r') as file:
        words = file.read().split()
        word_counts.update(words)

# c. Total number of words in both files
total_words = sum(word_counts.values())

# d. Top 3 words in IF.txt
top_words = word_counts.most_common(3)

# e. Find the IP address of the machine
# Get the hostname of the machine
hostname = socket.gethostname()
# Get the IP address corresponding to the hostname
ip_address = socket.gethostbyname(hostname)

# f. Write output to a text file
with open('/home/output/result.txt', 'w') as result_file:
    result_file.write(f"List of text files: {txt_files}\n")
    result_file.write(f"Total number of words in .txt files: {total_words}\n")
    result_file.write(f"Top 3 words with counts in IF.txt: {top_words}\n")
    result_file.write(f"IP Address: {ip_address}")

# g. Print output to console (stdout)
with open('/home/output/result.txt', 'r') as result_file:
    print(result_file.read())