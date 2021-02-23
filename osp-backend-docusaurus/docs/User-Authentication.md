---
id: User-Authentication
title: User Authentication
---

## User Authentication
To be able to use the application, a user needs to

- Register
- Confirm their Email
- Login

Currently, **JWT Authentication** is being used to authenticate users. There are 2 types of users now- **Admin** and **Student**. This feature needs to be extended to include various user-levels including; mentors, volunteers, applicants, contributors, maintainers and so on. Other Login and Register methods which need to be applied:

- OAuth using GitHub
- OAuth using Google

## How it works
User Authentication is JSONWebToken (JWT) based. To implement this we use a **djangorestframework** extension, `djangorestframework-simplejwt`. You can see an example of basic usage with this extension here.

In short, when a user logs in, the user will receive an authentication token (e.g.: access_token) which contains part of the user's identity and other token related fields, as the refresh token.

You can get an access token once you are registered into the backend.

The user can then use this `access_token` when using a protected/restricted API, such as GET /user API. To access this the client has to send the `access_token` in the header of the HTTP request, following this format: `Authorization: Bearer` `$(access_token)`. In this application, the `access_token` has been stored in the `localStorage` as an item and sent as a header in every request which requires authentication.
