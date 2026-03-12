FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Bundle app source
COPY . .

ENV HOST=0.0.0.0
ENV PORT=8080
ENV DEBUG=false

EXPOSE 8080
CMD [ "python", "app.py" ]
