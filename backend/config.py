class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'  # For local dev; use PostgreSQL in production
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'supersecretkey'  # Replace with a more secure secret in production
    KINESIS_STREAM_NAME = 'UserActivityStream'
    KINESIS_REGION = 'us-east-1'
    ELASTICSEARCH_URL = 'http://localhost:9200'
