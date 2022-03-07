FROM python:3.8-slim-buster as basic

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN  apt-get update \
  && python -m pip install --upgrade pip \
  # setting master user for file permmission purposes
  && useradd -m master 

RUN chown master:master -R /var/

WORKDIR /code

RUN chown master:master -R /code/

USER master

COPY --chown=master:master . /code/

RUN python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements/requirements.txt




# ===== SETUP =====
FROM basic AS django-dev

RUN chmod +x boot/boot_setup.sh

ENTRYPOINT [ "./boot/boot_setup.sh" ]