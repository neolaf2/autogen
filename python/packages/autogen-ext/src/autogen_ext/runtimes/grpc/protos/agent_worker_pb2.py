# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: agent_worker.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'agent_worker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import cloudevent_pb2 as cloudevent__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61gent_worker.proto\x12\x06\x61gents\x1a\x10\x63loudevent.proto\x1a\x19google/protobuf/any.proto\"$\n\x07\x41gentId\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"E\n\x07Payload\x12\x11\n\tdata_type\x18\x01 \x01(\t\x12\x19\n\x11\x64\x61ta_content_type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x89\x02\n\nRpcRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12$\n\x06source\x18\x02 \x01(\x0b\x32\x0f.agents.AgentIdH\x00\x88\x01\x01\x12\x1f\n\x06target\x18\x03 \x01(\x0b\x32\x0f.agents.AgentId\x12\x0e\n\x06method\x18\x04 \x01(\t\x12 \n\x07payload\x18\x05 \x01(\x0b\x32\x0f.agents.Payload\x12\x32\n\x08metadata\x18\x06 \x03(\x0b\x32 .agents.RpcRequest.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\t\n\x07_source\"\xb8\x01\n\x0bRpcResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12 \n\x07payload\x18\x02 \x01(\x0b\x32\x0f.agents.Payload\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x33\n\x08metadata\x18\x04 \x03(\x0b\x32!.agents.RpcResponse.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"(\n\x18RegisterAgentTypeRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"\x1b\n\x19RegisterAgentTypeResponse\":\n\x10TypeSubscription\x12\x12\n\ntopic_type\x18\x01 \x01(\t\x12\x12\n\nagent_type\x18\x02 \x01(\t\"G\n\x16TypePrefixSubscription\x12\x19\n\x11topic_type_prefix\x18\x01 \x01(\t\x12\x12\n\nagent_type\x18\x02 \x01(\t\"\xa2\x01\n\x0cSubscription\x12\n\n\x02id\x18\x01 \x01(\t\x12\x34\n\x10typeSubscription\x18\x02 \x01(\x0b\x32\x18.agents.TypeSubscriptionH\x00\x12@\n\x16typePrefixSubscription\x18\x03 \x01(\x0b\x32\x1e.agents.TypePrefixSubscriptionH\x00\x42\x0e\n\x0csubscription\"D\n\x16\x41\x64\x64SubscriptionRequest\x12*\n\x0csubscription\x18\x01 \x01(\x0b\x32\x14.agents.Subscription\"\x19\n\x17\x41\x64\x64SubscriptionResponse\"\'\n\x19RemoveSubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1c\n\x1aRemoveSubscriptionResponse\"\x19\n\x17GetSubscriptionsRequest\"G\n\x18GetSubscriptionsResponse\x12+\n\rsubscriptions\x18\x01 \x03(\x0b\x32\x14.agents.Subscription\"\x9d\x01\n\nAgentState\x12!\n\x08\x61gent_id\x18\x01 \x01(\x0b\x32\x0f.agents.AgentId\x12\x0c\n\x04\x65Tag\x18\x02 \x01(\t\x12\x15\n\x0b\x62inary_data\x18\x03 \x01(\x0cH\x00\x12\x13\n\ttext_data\x18\x04 \x01(\tH\x00\x12*\n\nproto_data\x18\x05 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x06\n\x04\x64\x61ta\";\n\x10GetStateResponse\x12\'\n\x0b\x61gent_state\x18\x01 \x01(\x0b\x32\x12.agents.AgentState\"\x13\n\x11SaveStateResponse\"\x99\x01\n\x07Message\x12%\n\x07request\x18\x01 \x01(\x0b\x32\x12.agents.RpcRequestH\x00\x12\'\n\x08response\x18\x02 \x01(\x0b\x32\x13.agents.RpcResponseH\x00\x12\x33\n\ncloudEvent\x18\x03 \x01(\x0b\x32\x1d.io.cloudevents.v1.CloudEventH\x00\x42\t\n\x07message2\x90\x04\n\x08\x41gentRpc\x12\x33\n\x0bOpenChannel\x12\x0f.agents.Message\x1a\x0f.agents.Message(\x01\x30\x01\x12\x35\n\x08GetState\x12\x0f.agents.AgentId\x1a\x18.agents.GetStateResponse\x12:\n\tSaveState\x12\x12.agents.AgentState\x1a\x19.agents.SaveStateResponse\x12T\n\rRegisterAgent\x12 .agents.RegisterAgentTypeRequest\x1a!.agents.RegisterAgentTypeResponse\x12R\n\x0f\x41\x64\x64Subscription\x12\x1e.agents.AddSubscriptionRequest\x1a\x1f.agents.AddSubscriptionResponse\x12[\n\x12RemoveSubscription\x12!.agents.RemoveSubscriptionRequest\x1a\".agents.RemoveSubscriptionResponse\x12U\n\x10GetSubscriptions\x12\x1f.agents.GetSubscriptionsRequest\x1a .agents.GetSubscriptionsResponseB\x1d\xaa\x02\x1aMicrosoft.AutoGen.Protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_worker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\032Microsoft.AutoGen.Protobuf'
  _globals['_RPCREQUEST_METADATAENTRY']._loaded_options = None
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_RPCRESPONSE_METADATAENTRY']._loaded_options = None
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_AGENTID']._serialized_start=75
  _globals['_AGENTID']._serialized_end=111
  _globals['_PAYLOAD']._serialized_start=113
  _globals['_PAYLOAD']._serialized_end=182
  _globals['_RPCREQUEST']._serialized_start=185
  _globals['_RPCREQUEST']._serialized_end=450
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_start=392
  _globals['_RPCREQUEST_METADATAENTRY']._serialized_end=439
  _globals['_RPCRESPONSE']._serialized_start=453
  _globals['_RPCRESPONSE']._serialized_end=637
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_start=392
  _globals['_RPCRESPONSE_METADATAENTRY']._serialized_end=439
  _globals['_REGISTERAGENTTYPEREQUEST']._serialized_start=639
  _globals['_REGISTERAGENTTYPEREQUEST']._serialized_end=679
  _globals['_REGISTERAGENTTYPERESPONSE']._serialized_start=681
  _globals['_REGISTERAGENTTYPERESPONSE']._serialized_end=708
  _globals['_TYPESUBSCRIPTION']._serialized_start=710
  _globals['_TYPESUBSCRIPTION']._serialized_end=768
  _globals['_TYPEPREFIXSUBSCRIPTION']._serialized_start=770
  _globals['_TYPEPREFIXSUBSCRIPTION']._serialized_end=841
  _globals['_SUBSCRIPTION']._serialized_start=844
  _globals['_SUBSCRIPTION']._serialized_end=1006
  _globals['_ADDSUBSCRIPTIONREQUEST']._serialized_start=1008
  _globals['_ADDSUBSCRIPTIONREQUEST']._serialized_end=1076
  _globals['_ADDSUBSCRIPTIONRESPONSE']._serialized_start=1078
  _globals['_ADDSUBSCRIPTIONRESPONSE']._serialized_end=1103
  _globals['_REMOVESUBSCRIPTIONREQUEST']._serialized_start=1105
  _globals['_REMOVESUBSCRIPTIONREQUEST']._serialized_end=1144
  _globals['_REMOVESUBSCRIPTIONRESPONSE']._serialized_start=1146
  _globals['_REMOVESUBSCRIPTIONRESPONSE']._serialized_end=1174
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_start=1176
  _globals['_GETSUBSCRIPTIONSREQUEST']._serialized_end=1201
  _globals['_GETSUBSCRIPTIONSRESPONSE']._serialized_start=1203
  _globals['_GETSUBSCRIPTIONSRESPONSE']._serialized_end=1274
  _globals['_AGENTSTATE']._serialized_start=1277
  _globals['_AGENTSTATE']._serialized_end=1434
  _globals['_GETSTATERESPONSE']._serialized_start=1436
  _globals['_GETSTATERESPONSE']._serialized_end=1495
  _globals['_SAVESTATERESPONSE']._serialized_start=1497
  _globals['_SAVESTATERESPONSE']._serialized_end=1516
  _globals['_MESSAGE']._serialized_start=1519
  _globals['_MESSAGE']._serialized_end=1672
  _globals['_AGENTRPC']._serialized_start=1675
  _globals['_AGENTRPC']._serialized_end=2203
# @@protoc_insertion_point(module_scope)
