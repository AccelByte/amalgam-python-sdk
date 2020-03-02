# Copyright (c) 2020 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import orjson
import os
import requests
import kazoo

ZK_URI = os.getenv('ZOOKEEPER_URL', '127.0.0.1:2181')
ZK_PREFIX = '/amalgam/'

class SentryConfig(object):
    def watch(self, key, callback):
        try:
            zk = KazooClient(hosts=ZK_URI, read_only=True)
            zk.start()
        except Exception as e:
            return e
        key = ZK_PREFIX + key
        if zk.exists(key):
            zk.DataWatch(key, callback)
            zk.stop()
        return True

    def jwks(self):
        try:
            jwks = requests.get(str(os.environ['JWKS_URI']))
            return orjson.loads(jwks)
        except:
            return orjson.loads(str(os.environ['JWKS']).strip("'<>() ").replace('\'', '\"'))

    def get(self, key):
        try:
            zk = KazooClient(hosts=ZK_URI, read_only=True)
            zk.start()
        except Exception as e:
            return e
        key = ZK_PREFIX + key
        try:
            if zk.exists(key):
                data, stat = zk.get(key)
                return {'data': data.decode("utf-8"), 'source': 'ZK', 'stat': stat}
            else:
                return {'data': os.getenv(key, default), 'source': 'ENV', 'stat': None}
        except Exception as e:
            return None
        finally:
            zk.stop()
