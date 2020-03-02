import pytest
from amalgam_jwt import jwt
import json
from jwt.algorithms import RSAAlgorithm

def test_decode_jwt():
    jwt_token = """eyJhbGciOiJSUzI1NiIsImtpZCI6IjJlM2VlYjc2ODM2YWViNjBjMzA2MzNkYjM3ZGU4ZDgwOWE4MTE0YzciLCJ0eXAiOiJKV1QifQ.eyJiYW5zIjpbXSwiY2xpZW50X2lkIjoiZTdkZTkyMjZkZjRkNDAxYmJhNDRkMjQzZTkzNzgyMDQiLCJjb3VudHJ5IjoiR2xvYmFsIiwiZGlzcGxheV9uYW1lIjoiU3VwZXJ1c2VyIiwiZXhwIjoxNTgyODAwNTUxLCJpYXQiOjE1ODI3ODYxNTEsImpmbGdzIjoxLCJuYW1lc3BhY2UiOiJ2ZXJzdXNldmlsIiwicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJkMzJiMzM1NGRjOTg0ZjQ2YmJlMjk5ZDcwZDJlY2M3NCJdLCJzY29wZSI6ImFjY291bnQgY29tbWVyY2Ugc29jaWFsIHB1Ymxpc2hpbmcgYW5hbHl0aWNzIiwic3ViIjoiYjkzY2JlYWNhMGQwNGJiZGIxZWIxNjBjZWY4OGE0ZWIifQ.mAR7QCsp2VqSconomgNwse_aYek3T1XKmaRKGVGU0VRQYp_-wDodrA35yypswwbtjX9qhRfsK28E9lhMf9C8UAf5lLG8p0lpejFpuPJAlKe0h6g_n3iylBWZronpa0_KxF0KCHh3DZERXMUXA7Jm8GWAIerrBX6tAj1PXw4EYQ_Cm9x-Issj8hffNPcvPrH61pdvQItIgx_lA8wDgyaGZvpFmHSzjKtWkZHpvBVRh5NZzJE-8FrLYdgwipJ6wKLF6kVA8rhqSMxqC9YfuwQ58GYSyS4jFw_LQyOe_d-RKDJS-0-pphsfd8rvqGROhhmImZEo9Pr1unOYT4MgEdW28w"""

    jwks  = """{
      "keys": [
        {
          "kty": "RSA",
          "use": "sig",
          "kid": "2e3eeb76836aeb60c30633db37de8d809a8114c7",
          "n": "uEvSt8ecPmI8-8_z9K5F1IzSeBze9OvR-y9U1AqUX6vncMZjJWQti05VbXUk8-UsJUI-5OkBxJ8XYy_8PIUArsTC-naoer7_XM7gvdWH_y20Vbwibbpy7ONhgACZOaeA0iUXyuKu7f5L78gyY7AedY7JJ5shvgMBeR8HJKbVSBq1H4fJqGIjPss6k5C62shiKrMbpm4q1Tg8o8tmCWm7CyyUbiUggzJusKAqc7ZccsSLRkTF5G3fN4nzBP4rwthYf2aSOVNC4Lcnqx7QsEQvpauVdR0rRuiB8ERyikWjGSVMXoZ-1YxaAUkKHtz1J4jMtNvOJa6Qw_UMbiAVhrz0Gw",
          "e": "AQAB"
        }
      ]
    }"""

    jwks = json.loads(jwks)
    jwk_key = json.dumps(jwks['keys'][0])
    public_key = RSAAlgorithm.from_jwk(jwk_key)
    decoded = jwt.decode_jwt(public_key, jwt_token)

    result = {'bans': [], 'client_id': 'e7de9226df4d401bba44d243e9378204', 'country': 'Global', 'display_name': 'Superuser', 'exp': 1582800551, 'iat': 1582786151, 'jflgs': 1, 'namespace': 'versusevil', 'permissions': [], 'roles': ['d32b3354dc984f46bbe299d70d2ecc74'], 'scope': 'account commerce social publishing analytics', 'sub': 'b93cbeaca0d04bbdb1eb160cef88a4eb'}
    print(decoded)

    assert result == decoded

def test_authenticate_jwt():
    jwt_token = """eyJhbGciOiJSUzI1NiIsImtpZCI6IjJlM2VlYjc2ODM2YWViNjBjMzA2MzNkYjM3ZGU4ZDgwOWE4MTE0YzciLCJ0eXAiOiJKV1QifQ.eyJiYW5zIjpbXSwiY2xpZW50X2lkIjoiZTdkZTkyMjZkZjRkNDAxYmJhNDRkMjQzZTkzNzgyMDQiLCJjb3VudHJ5IjoiR2xvYmFsIiwiZGlzcGxheV9uYW1lIjoiU3VwZXJ1c2VyIiwiZXhwIjoxNTgyODAwNTUxLCJpYXQiOjE1ODI3ODYxNTEsImpmbGdzIjoxLCJuYW1lc3BhY2UiOiJ2ZXJzdXNldmlsIiwicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJkMzJiMzM1NGRjOTg0ZjQ2YmJlMjk5ZDcwZDJlY2M3NCJdLCJzY29wZSI6ImFjY291bnQgY29tbWVyY2Ugc29jaWFsIHB1Ymxpc2hpbmcgYW5hbHl0aWNzIiwic3ViIjoiYjkzY2JlYWNhMGQwNGJiZGIxZWIxNjBjZWY4OGE0ZWIifQ.mAR7QCsp2VqSconomgNwse_aYek3T1XKmaRKGVGU0VRQYp_-wDodrA35yypswwbtjX9qhRfsK28E9lhMf9C8UAf5lLG8p0lpejFpuPJAlKe0h6g_n3iylBWZronpa0_KxF0KCHh3DZERXMUXA7Jm8GWAIerrBX6tAj1PXw4EYQ_Cm9x-Issj8hffNPcvPrH61pdvQItIgx_lA8wDgyaGZvpFmHSzjKtWkZHpvBVRh5NZzJE-8FrLYdgwipJ6wKLF6kVA8rhqSMxqC9YfuwQ58GYSyS4jFw_LQyOe_d-RKDJS-0-pphsfd8rvqGROhhmImZEo9Pr1unOYT4MgEdW28w"""

    jwks  = """{
      "keys": [
        {
          "kty": "RSA",
          "use": "sig",
          "kid": "2e3eeb76836aeb60c30633db37de8d809a8114c7",
          "n": "uEvSt8ecPmI8-8_z9K5F1IzSeBze9OvR-y9U1AqUX6vncMZjJWQti05VbXUk8-UsJUI-5OkBxJ8XYy_8PIUArsTC-naoer7_XM7gvdWH_y20Vbwibbpy7ONhgACZOaeA0iUXyuKu7f5L78gyY7AedY7JJ5shvgMBeR8HJKbVSBq1H4fJqGIjPss6k5C62shiKrMbpm4q1Tg8o8tmCWm7CyyUbiUggzJusKAqc7ZccsSLRkTF5G3fN4nzBP4rwthYf2aSOVNC4Lcnqx7QsEQvpauVdR0rRuiB8ERyikWjGSVMXoZ-1YxaAUkKHtz1J4jMtNvOJa6Qw_UMbiAVhrz0Gw",
          "e": "AQAB"
        }
      ]
    }"""

    jwks = json.loads(jwks)
    jwk_key = json.dumps(jwks['keys'][0])
    public_key = RSAAlgorithm.from_jwk(jwk_key)

    permission_rule_json = """{
        "accelbytetesting": ["rolesidaccelbytetesting", "adminrolesidaccelbytetesting", "accelbyteadminrole"],
        "samplegame": ["rolesidsamplegame", "accelbyteadminrole"],
        "public": ["*"],
        "accelbyte": ["accelbyteadminrole"],
        "versusevil": ["d32b3354dc984f46bbe299d70d2ecc74"]
    }"""

    allowed, decoded = jwt.authenticate_jwt(public_key, jwt_token, permission_rule_json, verify_exp=False)

    result = {'bans': [], 'client_id': 'e7de9226df4d401bba44d243e9378204', 'country': 'Global', 'display_name': 'Superuser', 'exp': 1582800551, 'iat': 1582786151, 'jflgs': 1, 'namespace': 'versusevil', 'permissions': [], 'roles': ['d32b3354dc984f46bbe299d70d2ecc74'], 'scope': 'account commerce social publishing analytics', 'sub': 'b93cbeaca0d04bbdb1eb160cef88a4eb'}
    print(allowed, decoded)

    assert result == decoded
