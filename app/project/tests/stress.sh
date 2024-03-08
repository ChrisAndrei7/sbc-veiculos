#!/bin/bash
foi i in {1..1000}; do
  curl localhost:31000/users
  sleep $1
  done