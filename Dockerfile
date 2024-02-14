FROM python:alpine

# Set working directory inside the container
WORKDIR /home/data

# Create output folder
RUN mkdir -p /home/output

# Copy Python script and text files into the container
COPY script.py /home/data/
COPY IF.txt /home/data/
COPY Limerick-1.txt /home/data/

# Run the Python script when the container starts
CMD ["python", "script.py"]