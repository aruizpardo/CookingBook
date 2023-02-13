FROM python:3.9

# Environment
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install requirements
RUN pip install --upgrade pip
COPY docker/requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Copy entrypoint
COPY docker/entrypoint.sh /
RUN chmod 755 /entrypoint.sh

# Copy code
COPY code /app
WORKDIR /app

# Expose and command
EXPOSE 5000
CMD ["sh", "/entrypoint.sh"]