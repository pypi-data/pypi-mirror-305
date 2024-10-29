# import requests
# import os
# import requests
# import json
# import logging
#
# from typing import Tuple
#
#
# def make_rest_call(json_data):
#     fabric = 'prod-ltx1'
#     topic = 'T3SearchDBTPOC'
#     headers = {'Content-Type': 'application/json'}
#     schema_url = f"http://1.schemaregistry.corp-lva1.atd.corp.linkedin.com:10252/schemaRegistry/api/v2/name/{topic}/latest"
#     response = requests.get(schema_url, headers=headers)
#     schema_details = response.json()
#     schema_id = schema_details.get('md5Hash')
#     schema = schema_details.get('schema')
#     # event = json_rdd.collect()
#     url = f"https://1.tracking-rest.prod-ltx1.atd.prod.linkedin.com:16869/tracking-rest/kafka/topics/{topic}?schemaId={schema_id}"
#     cert = ('/tmp/identity.cert', '/tmp/identity.key')
#     cacert = '/etc/riddler/ca-bundle.crt'
#     response = requests.post(url, json=json_data, headers=headers, verify=cacert, cert=cert)
#     print('Response JSON:', response.json() if response.status_code == 200 else response.text)
#     return response.text
#
#
# def process_partition(partition):
#     import os
#     import requests
#     import json
#     import logging
#
#     from typing import Tuple
#
#     from OpenSSL import crypto  # type: ignore
#
#     class HadoopTokenParser:
#         HEAD_BYTES = b'HDTS'
#         CERT_FILE_NAME = "identity.cert"
#         KEY_FILE_NAME = "identity.key"
#
#         def __init__(self):
#             self.token_map = {}
#             self.secret_keys_map = {}
#             self.byte_list = []
#
#         def parse_hadoop_token(self, hadoop_token_path):
#             self.token_map.clear()
#             self.secret_keys_map.clear()
#             self.byte_list.clear()
#             with open(hadoop_token_path, "rb") as file_in:
#                 while (b := file_in.read(1)):
#                     self.byte_list.append(b)
#
#             head_bytes = self._read_n_bytes(4)
#             assert all([b1 == b2 for b1, b2 in zip(head_bytes, self.HEAD_BYTES)]), \
#                 "Token file's format is wrong, expect header to be HDTS"
#             version = self.byte_list.pop(0)[0]
#             assert version == 0, f"Unknown version {version} in token storage."
#
#             size = self._read_int()
#             for _ in range(size):
#                 field_name = self._read_text_field()
#                 token = self._read_token_field()
#                 self.token_map[field_name] = token
#
#             size = self._read_int()
#             for _ in range(size):
#                 secret_name = self._read_text_field()
#                 secret_size = self._read_int()
#                 secret = self._read_n_bytes(secret_size)
#                 self.secret_keys_map[secret_name] = secret
#
#             assert len(self.byte_list) == 0, "Hadoop token file has unparsed bytes."
#
#         def write_cert(self, cert_folder) -> Tuple[str, str]:
#             p12 = crypto.load_pkcs12(
#                 self.secret_keys_map["li.datavault.identity"],
#                 self.secret_keys_map["li.datavault.identity.key.password"]
#             )
#
#             cert_path, key_path = f"{cert_folder}/{self.CERT_FILE_NAME}", f"{cert_folder}/{self.KEY_FILE_NAME}"
#             with open(key_path, "wb") as file_out:
#                 file_out.write(crypto.dump_privatekey(type=crypto.FILETYPE_PEM, pkey=p12.get_privatekey()))
#             with open(cert_path, "wb") as file_out:
#                 file_out.write(crypto.dump_certificate(type=crypto.FILETYPE_PEM, cert=p12.get_certificate()))
#             return cert_path, key_path
#
#         def _read_n_bytes(self, n):
#             assert len(self.byte_list) >= n, "Not enough bytes to read from the token file."
#             result = []
#             for _ in range(n):
#                 result.append(self.byte_list.pop(0))
#             return b''.join(result)
#
#         def _read_int(self):
#             n = self._read_long()
#             assert n >= -2147483648 and n <= 2147483647, "Invalid version number, out of interger bound."
#             return n
#
#         def _read_long(self):
#             first_byte = int.from_bytes(self.byte_list.pop(0), byteorder="little", signed=True)
#             if first_byte >= -112:
#                 n_byte = 1
#             elif first_byte < -120:
#                 n_byte = -119 - first_byte
#             else:
#                 n_byte = -111 - first_byte
#             if n_byte == 1:
#                 return first_byte
#             x = 0
#             for _ in range(n_byte - 1):
#                 b = self.byte_list.pop(0)[0]
#                 x = x << 8
#                 x = x | (b & 0xFF)
#             is_negative = first_byte < -120 or (first_byte >= -112 and first_byte < 0)
#             assert not is_negative, "Something wrong while parsing token, number must be positive."
#             return x
#
#         def _read_text_field(self):
#             field_size = self._read_int()
#             field_bytes = self._read_n_bytes(field_size)
#             return field_bytes.decode("utf-8")
#
#         def _read_token_field(self):
#             identifier_size = self._read_int()
#             identifier_bytes = self._read_n_bytes(identifier_size)
#             password_size = self._read_int()
#             password_bytes = self._read_n_bytes(password_size)
#             kind = self._read_text_field()
#             service = self._read_text_field()
#             return {
#                 "identifier": identifier_bytes,
#                 "password": password_bytes,
#                 "kind": kind,
#                 "service": service
#             }
#
#     token_parser = HadoopTokenParser()
#     token_parser.parse_hadoop_token(os.getenv("HADOOP_TOKEN_FILE_LOCATION"))
#     token_parser.write_cert("/tmp")
#     a = []
#     c = 0
#     import json
#     import base64
#
#     def convert_bytearray(obj):
#         if isinstance(obj, bytearray):
#             # Convert the bytearray to a base64-encoded string to handle binary data
#             return base64.b64encode(obj).decode('ascii')  # Base64 for binary data
#         elif isinstance(obj, dict):
#             return {k: convert_bytearray(v) for k, v in obj.items()}
#         elif isinstance(obj, list):
#             return [convert_bytearray(elem) for elem in obj]
#         else:
#             return obj
#
#     for row in partition:
#         print(row.asDict(True))
#         print("***********")
#         row_dict = row.asDict(True)
#         # print(row_dict)
#         # print(json.loads(json.dumps(convert_bytearray(row_dict))))
#         json_data = json.loads(json.dumps(convert_bytearray(row_dict)))
#         a.append(make_rest_call(json_data))
#         c = c + 1
#     return [c]
#
#
# fabric = 'prod-ltx1'
# topic = 'T3SearchDBTPOC'
# headers = {
#     'Content-Type': 'application/json', 'Mode-Type': 'sync'
# }
# # from pyspark.sql.functions import rand, expr
# # token_parser = HadoopTokenParser()
# # token_parser.parse_hadoop_token(os.getenv("HADOOP_TOKEN_FILE_LOCATION"))
# # token_parser.write_cert("/tmp")
# # schema_url = f"http://1.schemaregistry.corp-lva1.atd.corp.linkedin.com:10252/schemaRegistry/api/v2/name/{topic}/latest"
# # response = requests.get(schema_url, headers=headers)
# # schema_details = response.json()
# # schema_id = schema_details.get('md5Hash')
# # schema = schema_details.get('schema')
# # event = {"key": {"string": "key1"}, "value": {"string": "value1"}}
# # url = f"https://1.tracking-rest.prod-lva1.atd.prod.linkedin.com:16869/tracking-rest/kafka/topics/{topic}?schemaId={schema_id}"
# # cacert = '/etc/riddler/ca-bundle.crt'
# # response = requests.post(url, json=event, headers=headers, verify=cacert, cert=('/tmp/identity.cert', '/tmp/identity.key' ))
# # print(f'Status Code: {response.status_code}')
# # print('Response JSON:', response.json() if response.status_code == 200 else response.text)
#
# df = spark.sql("code_sql")
# for k in df.rdd.mapPartitions(process_partition).collect():
#     print(k)
