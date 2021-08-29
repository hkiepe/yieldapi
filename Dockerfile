FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/

RUN python -m pip install --upgrade pip
RUN pip install python-multipart
RUN pip install python-jose
RUN pip install passlib[bcrypt]
