# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from jolt.plugins.remote_execution import scheduler_pb2 as jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2
from jolt.plugins.remote_execution import worker_pb2 as jolt_dot_plugins_dot_remote__execution_dot_worker__pb2


class WorkerStub(object):
    """The scheduler interface for workers and executors.
    Workers prepare the build environment by deploying and
    running executors (Jolt clients) to execute tasks.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInstructions = channel.stream_stream(
                '/Worker/GetInstructions',
                request_serializer=jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerUpdate.SerializeToString,
                response_deserializer=jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerRequest.FromString,
                )
        self.GetTasks = channel.stream_stream(
                '/Worker/GetTasks',
                request_serializer=jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskUpdate.SerializeToString,
                response_deserializer=jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskRequest.FromString,
                )


class WorkerServicer(object):
    """The scheduler interface for workers and executors.
    Workers prepare the build environment by deploying and
    running executors (Jolt clients) to execute tasks.
    """

    def GetInstructions(self, request_iterator, context):
        """Called by a worker to get build instructions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTasks(self, request_iterator, context):
        """Called by an executor (Jolt client) to get task execution requests.
        Task updates, including status and logs are sent back to the scheduler.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInstructions': grpc.stream_stream_rpc_method_handler(
                    servicer.GetInstructions,
                    request_deserializer=jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerUpdate.FromString,
                    response_serializer=jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerRequest.SerializeToString,
            ),
            'GetTasks': grpc.stream_stream_rpc_method_handler(
                    servicer.GetTasks,
                    request_deserializer=jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskUpdate.FromString,
                    response_serializer=jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskRequest.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """The scheduler interface for workers and executors.
    Workers prepare the build environment by deploying and
    running executors (Jolt clients) to execute tasks.
    """

    @staticmethod
    def GetInstructions(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Worker/GetInstructions',
            jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerUpdate.SerializeToString,
            jolt_dot_plugins_dot_remote__execution_dot_worker__pb2.WorkerRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTasks(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Worker/GetTasks',
            jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskUpdate.SerializeToString,
            jolt_dot_plugins_dot_remote__execution_dot_scheduler__pb2.TaskRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
