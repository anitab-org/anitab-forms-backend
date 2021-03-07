---
id: Quality-Assurance-Test-Cases
title: Quality Assurance Test Cases
---

Currently, all the APIs are being run through common tests to verify their working. You get to view the status codes in your Network tab too.
## User Registration

**Possible test cases**

| Test Case                                                                                                       | Result  |
| ----------------------------------------------------------------------------------------------------------------|:-------:|
| Status Code is `201` or `403`(403 means user already exists, but API working correctly so test case should pass)| Success |
| Content type header is present                                                                                  | Success |
| Status Code `400` & `500`                                                                                       | Fail    | 
| Content type header not present                                                                                 | Fail    |

## POST

**Possible test cases**

| Test Case                                                                                                       | Result  |
| ----------------------------------------------------------------------------------------------------------------|:-------:|
| Status Code is `201` or `200`                                                                                   | Success |
| Content type header is present                                                                                  | Success |
| Status Code `400`, `404` & `500`                                                                                | Fail    | 
| Content type header not present                                                                                 | Fail    |

## PATCH

**Possible test cases**

| Test Case                                                                                                       | Result  |
| ----------------------------------------------------------------------------------------------------------------|:-------:|
| Status Code is `201` or `200`                                                                                   | Success |
| Content type header is present                                                                                  | Success |
| Status Code `400`, `404` & `500`                                                                                | Fail    | 
| Content type header not present                                                                                 | Fail    |

## GET

**Possible test cases**

| Test Case                                                                                                       | Result  |
| ----------------------------------------------------------------------------------------------------------------|:-------:|
| Status Code is `200`                                                                                            | Success |
| Content type header is present                                                                                  | Success |
| Status Code `400`, `404` & `500`                                                                                | Fail    | 
| Content type header not present                                                                                 | Fail    |

## DELETE

**Possible test cases**

| Test Case                                                                                                       | Result  |
| ----------------------------------------------------------------------------------------------------------------|:-------:|
| Status Code is `204`                                                                                            | Success |
| Content type header is present                                                                                  | Success |
| Status Code `400`, `404` & `500`                                                                                | Fail    | 
| Content type header not present                                                                                 | Fail    |
