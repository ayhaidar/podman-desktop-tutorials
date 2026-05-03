FROM quay.io/fedora/python-312

LABEL org.opencontainers.image.authors="your-name@example.com"

USER root

# 1. Global SSL and proxy setup - strongly discouraged for production environments
RUN echo "sslverify=0" >> /etc/dnf/dnf.conf


# 1. DEFINE PROXY (Replace with your actual corporate proxy details)
# Make sure to change the proxy to the right one
ENV http_proxy=http://username@proxy:8080
ENV https_proxy=https://username@proxy:8080
ENV ftp_proxy=http://username@proxy:8080
ENV no_proxy=localhost,127.0.0.1

# 2. Install basic tools first
RUN dnf install -y gcc-c++ unixODBC-devel && dnf clean all

# 3. INSTALL LOCAL RPM
# We copy the file you downloaded into the container
COPY msodbcsql18-18.4.1.1-1.x86_64.rpm /tmp/msodbcsql18.rpm

# Install it locally. This ignores the broken mssql-release repo entirely.
RUN ACCEPT_EULA=Y dnf localinstall -y /tmp/msodbcsql18.rpm && rm /tmp/msodbcsql18.rpm

WORKDIR /app

# 7. PIP CONFIG (Must trust hosts due to proxy SSL inspection)
# Make sure to change the proxy to the right one
COPY requirements.txt .
RUN pip install --no-cache-dir \
    --proxy http://username@proxy:8080 \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host packages.microsoft.com \
    -r requirements.txt

COPY pull_script.py .
RUN mkdir -p /var/lib/exports

CMD ["python", "pull_script.py"]

