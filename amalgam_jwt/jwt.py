import json
import jwt
from jwt.algorithms import RSAAlgorithm
import requests
import typing
from functools import lru_cache

@lru_cache(maxsize=128)
def authenticate_jwt(jwk:str, token:str, permission_rule_json:str="{}", verify_aud:bool=False, verify_exp:bool=True, algorithms:list=['RS256']):
    jwt_payload = jwt.decode(token, jwk, options={'verify_aud': verify_aud, 'verify_exp': verify_exp} , algorithms=algorithms)

    try:
        permission_rule = json.loads(permission_rule_json)
        allowed = False
        roles_in_jwt = jwt_payload['roles']
        namespace_in_jwt = jwt_payload['namespace']

        for role in permission_rule[namespace_in_jwt]:
            if (role == '*'):
                #allow all role here
                allowed = True
                break
            if role in roles_in_jwt:
                allowed = True
                break
    except:
        pass
    return allowed, jwt_payload

@lru_cache(maxsize=128)
def decode_jwt(public_key:str, token: str):
    jwt_payload = jwt.decode(token, public_key, options={'verify_aud': False, 'verify_exp': False} , algorithms='RS256')
    return jwt_payload


def get_public_key(jwks_uri):
    try:
        jwks_data = requests.get(jwks_uri)
    except requests.exceptions.ConnectionError as e:
        jwks_data = requests.get("http://justice-iam-service.versusevil/iam/v3/oauth/jwks")

    jwks = jwks_data.text
    jwks = json.loads(jwks)
    jwk_key = json.dumps(jwks['keys'][0])
    return RSAAlgorithm.from_jwk(jwk_key)
