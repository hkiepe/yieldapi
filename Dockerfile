FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/

RUN pip install python-multipart
RUN pip install python-jose
RUN pip install passlib[bcrypt]
