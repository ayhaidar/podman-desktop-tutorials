FROM quay.io/fedora/python-312

LABEL org.opencontainers.image.authors="your-name@example.com"

# Make sure to change the proxy to the correct one, delete if no proxy is used.
ARG http_proxy=http://username@proxy:8080
ARG https_proxy=http://username@proxy:8080

WORKDIR /app

# Install Streamlit and pandas
RUN pip install --no-cache-dir streamlit pandas

COPY app.py .
RUN mkdir -p /app/dashboard_data

EXPOSE 8536

# Ensure Streamlit binds to all interfaces (0.0.0.0) so you can see it from Windows
CMD ["streamlit", "run", "app.py", "--server.port=8536", "--server.address=0.0.0.0"]
