FROM python:3.9

# Environment
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install requirements
COPY docker/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy code
COPY code /app
WORKDIR /app

# Expose and command
EXPOSE 5000
CMD ["flask", "run"]