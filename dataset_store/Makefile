.PHONY: proto
proto:
	python -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. ./protos/dataset_store.proto

.PHONY: server
server:
	docker build -t ds_server .
