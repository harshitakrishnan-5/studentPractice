From python:3.11
WORKDIR / swap_app
COPY . .
RUN pip install --no-cache-dir pytest
ENTRYPOINT ["pytest", "swap.py"]