# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: plugin_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14plugin_service.proto\x12\x06plugin\"&\n\x16GetPluginByNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"L\n\x17GetPluginByNameResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\"\n\x06plugin\x18\x02 \x01(\x0b\x32\x12.plugin.PluginInfo\"/\n\x11\x46indPluginRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"G\n\x12\x46indPluginResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\x12\"\n\x06plugin\x18\x02 \x01(\x0b\x32\x12.plugin.PluginInfo\"\x8d\x01\n\nPluginInfo\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04host\x18\x06 \x01(\t\x12\x0c\n\x04port\x18\x07 \x01(\x05\x12\x0e\n\x06status\x18\x08 \x01(\t\"T\n\x13UpdatePluginRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"8\n\x14UpdatePluginResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"r\n\x12PluginRegistration\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0c\n\x04port\x18\x06 \x01(\x05\"K\n\x14RegistrationResponse\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\":\n\x10HeartbeatRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x13\n\x0bstatus_info\x18\x02 \x01(\t\":\n\x11HeartbeatResponse\x12\x10\n\x08received\x18\x01 \x01(\x08\x12\x13\n\x0bserver_time\x18\x02 \x01(\x03\"\"\n\rStatusRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\"A\n\x0eStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x02 \x01(\t\x12\x0e\n\x06uptime\x18\x03 \x01(\x03\"\xa3\x01\n\x0e\x43ommandRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\x12:\n\nparameters\x18\x03 \x03(\x0b\x32&.plugin.CommandRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"I\n\x0f\x43ommandResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t\" \n\x0bStopRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\"0\n\x0cStopResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xc3\x04\n\rPluginService\x12L\n\x0eRegisterPlugin\x12\x1a.plugin.PluginRegistration\x1a\x1c.plugin.RegistrationResponse\"\x00\x12\x42\n\tHeartbeat\x12\x18.plugin.HeartbeatRequest\x1a\x19.plugin.HeartbeatResponse\"\x00\x12<\n\tGetStatus\x12\x15.plugin.StatusRequest\x1a\x16.plugin.StatusResponse\"\x00\x12\x43\n\x0e\x45xecuteCommand\x12\x16.plugin.CommandRequest\x1a\x17.plugin.CommandResponse\"\x00\x12\x39\n\nStopPlugin\x12\x13.plugin.StopRequest\x1a\x14.plugin.StopResponse\"\x00\x12\x43\n\nFindPlugin\x12\x19.plugin.FindPluginRequest\x1a\x1a.plugin.FindPluginResponse\x12I\n\x0cUpdatePlugin\x12\x1b.plugin.UpdatePluginRequest\x1a\x1c.plugin.UpdatePluginResponse\x12R\n\x0fGetPluginByName\x12\x1e.plugin.GetPluginByNameRequest\x1a\x1f.plugin.GetPluginByNameResponseB2\n\x1a\x63om.owiseman.dataapi.protoB\x12PluginServiceProtoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'plugin_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.owiseman.dataapi.protoB\022PluginServiceProtoP\001'
  _globals['_COMMANDREQUEST_PARAMETERSENTRY']._loaded_options = None
  _globals['_COMMANDREQUEST_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_GETPLUGINBYNAMEREQUEST']._serialized_start=32
  _globals['_GETPLUGINBYNAMEREQUEST']._serialized_end=70
  _globals['_GETPLUGINBYNAMERESPONSE']._serialized_start=72
  _globals['_GETPLUGINBYNAMERESPONSE']._serialized_end=148
  _globals['_FINDPLUGINREQUEST']._serialized_start=150
  _globals['_FINDPLUGINREQUEST']._serialized_end=197
  _globals['_FINDPLUGINRESPONSE']._serialized_start=199
  _globals['_FINDPLUGINRESPONSE']._serialized_end=270
  _globals['_PLUGININFO']._serialized_start=273
  _globals['_PLUGININFO']._serialized_end=414
  _globals['_UPDATEPLUGINREQUEST']._serialized_start=416
  _globals['_UPDATEPLUGINREQUEST']._serialized_end=500
  _globals['_UPDATEPLUGINRESPONSE']._serialized_start=502
  _globals['_UPDATEPLUGINRESPONSE']._serialized_end=558
  _globals['_PLUGINREGISTRATION']._serialized_start=560
  _globals['_PLUGINREGISTRATION']._serialized_end=674
  _globals['_REGISTRATIONRESPONSE']._serialized_start=676
  _globals['_REGISTRATIONRESPONSE']._serialized_end=751
  _globals['_HEARTBEATREQUEST']._serialized_start=753
  _globals['_HEARTBEATREQUEST']._serialized_end=811
  _globals['_HEARTBEATRESPONSE']._serialized_start=813
  _globals['_HEARTBEATRESPONSE']._serialized_end=871
  _globals['_STATUSREQUEST']._serialized_start=873
  _globals['_STATUSREQUEST']._serialized_end=907
  _globals['_STATUSRESPONSE']._serialized_start=909
  _globals['_STATUSRESPONSE']._serialized_end=974
  _globals['_COMMANDREQUEST']._serialized_start=977
  _globals['_COMMANDREQUEST']._serialized_end=1140
  _globals['_COMMANDREQUEST_PARAMETERSENTRY']._serialized_start=1091
  _globals['_COMMANDREQUEST_PARAMETERSENTRY']._serialized_end=1140
  _globals['_COMMANDRESPONSE']._serialized_start=1142
  _globals['_COMMANDRESPONSE']._serialized_end=1215
  _globals['_STOPREQUEST']._serialized_start=1217
  _globals['_STOPREQUEST']._serialized_end=1249
  _globals['_STOPRESPONSE']._serialized_start=1251
  _globals['_STOPRESPONSE']._serialized_end=1299
  _globals['_PLUGINSERVICE']._serialized_start=1302
  _globals['_PLUGINSERVICE']._serialized_end=1881
# @@protoc_insertion_point(module_scope)
