# Step 1: Use the official Python image as a base
FROM python:3.9

# Step 2: Set the working directory
WORKDIR /

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the application code
COPY . .

# Step 5: Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=5000

# Step 6: Expose the port the app runs on
EXPOSE 5000

# Step 7: Run the application 
# CMD ["flask", "run"]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

