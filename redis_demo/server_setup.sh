#!/bin/bash

# Wait for the Redis server to start
echo "Waiting for Redis to start..."
sleep 5  # Adjust this time if necessary

# Run migrations
echo "Applying migrations..."
python /app/manage.py migrate

# Create a superuser (using a custom Django management command)
echo "Creating superuser..."
python /app/manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', '${DJANGO_SUPERUSER_PASSWORD}')
else:
    print("Superuser already exists.")
END

# Start the Daphne server
echo "Starting the Daphne server..."
exec daphne -b 0.0.0.0 -p 8000 redis_demo.asgi:application
