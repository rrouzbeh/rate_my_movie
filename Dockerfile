FROM python:3.9-alpine as base

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt


FROM base
RUN mkdir /app
COPY --from=builder /install /usr/local
WORKDIR /app
COPY . .
RUN python setup.py install

ENTRYPOINT ["rate-my-movie"]