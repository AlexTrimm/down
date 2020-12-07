# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dataset_store_pb2 as dataset__store__pb2


class DataSetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateIterator = channel.unary_unary(
                '/DataSetService/CreateIterator',
                request_serializer=dataset__store__pb2.DatSetSpec.SerializeToString,
                response_deserializer=dataset__store__pb2.IteratorSpec.FromString,
                )
        self.GetNextBatch = channel.unary_unary(
                '/DataSetService/GetNextBatch',
                request_serializer=dataset__store__pb2.IteratorSpec.SerializeToString,
                response_deserializer=dataset__store__pb2.Dataset.FromString,
                )


class DataSetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateIterator(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNextBatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataSetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateIterator': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIterator,
                    request_deserializer=dataset__store__pb2.DatSetSpec.FromString,
                    response_serializer=dataset__store__pb2.IteratorSpec.SerializeToString,
            ),
            'GetNextBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNextBatch,
                    request_deserializer=dataset__store__pb2.IteratorSpec.FromString,
                    response_serializer=dataset__store__pb2.Dataset.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataSetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataSetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateIterator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataSetService/CreateIterator',
            dataset__store__pb2.DatSetSpec.SerializeToString,
            dataset__store__pb2.IteratorSpec.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNextBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataSetService/GetNextBatch',
            dataset__store__pb2.IteratorSpec.SerializeToString,
            dataset__store__pb2.Dataset.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
