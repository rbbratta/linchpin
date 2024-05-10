# Use the official Red Hat Universal Base Image 8
FROM registry.access.redhat.com/ubi8/ubi
LABEL authors="rbrattai"

# Set environment variables to avoid Python buffering and facilitate logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install Python 3 and necessary system packages
RUN yum -y install python39 python3-libselinux \
    && yum -y module enable python39 \
    && yum clean all

# Upgrade pip and install required Python packages
RUN python3.9 -m pip install --upgrade pip \
    && python3.9 -m pip install ansible==2.9.* \
                               netaddr \
                               lxml \
                               jinja2==2.11.3 \
                               jmespath \
                               beautifulsoup4 \
                               dnspython \
                               markupsafe==2.0.1 \
                               Cython \
                               boto3==1.15.18 \
                               click==8.0.4

# Set the working directory
WORKDIR /app

COPY ./ /app/linchpin
RUN pip install /app/linchpin


# Set the default command for the container
CMD ["ansible-playbook"]
