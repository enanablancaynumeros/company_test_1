#!make

SHELL := /bin/bash

tests:
	pytest -sv --lf

build:
	cd docker && docker-compose build

up: build
	cd docker && docker-compose up

task_1:
	go run task_1.go

