import concurrent.futures
import grpc

from pymemcache.client import base

import dataset_store_pb2_grpc
import dataset_store_pb2 as rpc


class DataSetServer(dataset_store_pb2_grpc.DataSetServiceServicer):


    def putDatapoint(self, request, context):
        client = base.Client(('memcached', 11211))
        print('Setting {} to {}'.format(request.k, request.v))
        client.set(request.k.k, request.v.v)
        return request

    def getDatapoint(self, request, context):
        client = base.Client(('memcached', 11211))
        try:
            result = client.get(request.k)
            return rpc.Value(v=result)
        except:
            return rpc.Value(v='')

    def createIterator(self, request, context):
        # load 
        return rpc.IteratorSpec(Id=1)
        

    def getNextBatch(self, request, context):
        return rpc.Dataset(data = 'ohellothere', schema='thisisalex')


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    dataset_store_pb2_grpc.add_DataSetServiceServicer_to_server(DataSetServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
