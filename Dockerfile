FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /server
WORKDIR /server
COPY server/requirements.txt /server/
RUN pip install -r requirements.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list \
    && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
	&& apt-get update \
	&& apt-get -y install postgresql-client-12
COPY server /server/
COPY frontend /frontend/ 
