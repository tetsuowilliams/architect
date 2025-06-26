#!/bin/bash

mkdir -p postgres-data

docker run --rm \
  -e POSTGRES_PASSWORD=postgres \
  -p 54320:5432 \
  -v "$(pwd)"/postgres-data:/var/lib/postgresql/data \
  pgvector/pgvector:pg17 \
  postgres -c max_connections=200