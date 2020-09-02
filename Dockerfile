FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN python -m venv venv
ENV DEBUG 1

ENV PORT 5000

WORKDIR /code
COPY requirements.txt /code/
COPY boot.sh /code/

RUN pip3 install -r /code/requirements.txt
WORKDIR /code
COPY backend /code/backend/

ENV FLASK_APP backend/main.py

RUN chmod +x /code/boot.sh

EXPOSE 5000

USER root
RUN chmod 755 /code/boot.sh
# RUN chmod +x boot.sh
ENTRYPOINT ["sh", "/code/boot.sh"]

