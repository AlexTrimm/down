import grpc
import dataset_store_pb2_grpc
import dataset_store_pb2 as rpc

channel = grpc.insecure_channel('localhost:50051')
stub = dataset_store_pb2_grpc.DataSetServiceStub(channel)
ds_spec = rpc.DatSetSpec(Id=123)
ret = stub.createIterator(ds_spec)
print(ret)


k = rpc.Key(k='thing1')
v = rpc.Value(v='{"var1":12, "var2":.312}')
kv = rpc.KVPair(k=k, v=v)
stub.putDatapoint(kv)
stub.getDatapoint(k)
