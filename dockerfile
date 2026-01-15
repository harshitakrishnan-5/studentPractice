FROM python:3.11
WORKDIR /swap
COPY . .
RUN pip install --no-cache-dir pytest
ENTRYPOINT ["pytest", "swap.py"]