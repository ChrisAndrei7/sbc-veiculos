#!/bin/bash
foi i in {1..1000}; do
  curl localhost:31000/veiculos
  sleep $1
  done