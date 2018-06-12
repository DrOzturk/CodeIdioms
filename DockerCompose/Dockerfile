FROM python:3.4-alpine
# We still need COPY, as docker-compose will bind mount the volume after this image is built
# ADD vs COPY:
# ADD allows <src> to be an URL
# If the <src> parameter of ADD is an archive in a recognised compression format, it will be unpacked
# Use copy if these are not needed!
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]