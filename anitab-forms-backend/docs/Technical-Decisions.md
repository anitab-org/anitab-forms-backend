---
id: Technical-Decisions
title: Technical Decisions
---

### This page contains the details about the choice of tech stack and implementation methods chosen.
## Django 3.0.7

Django has been growing popularly ever since and has emerged as the first choice of any python developer who looks forward to trying one's hands on Web Development.

At the time the project was started, in the year 2020, Django 3.0.7 was the latest version of Django.

These are a few reasons why Django is considered as an apt framework for this project.

- A web application framework is basically a toolkit of components that all web applications need. The point of this is to let developers focus on the things that are new and unique about their project instead of implementing the same solutions over and over again. Django is even more fully featured than most other frameworks, coming with everything you need to build a web app right out-of-the-box.
- Part of what makes Django so powerful is its ability to be extended with ‘app’ plugins. There are hundreds of these packages that make it easy to do things. For example, in this particular project, we are using a number of libraries and plugins viz SimpleJWT, Corsheaders and a lot more are being used.
- Django, evolving as a very popular framework, has an excellent community of developers because of which easy help is available, just a google search away.

Anyone wishing to try their hands on Django can check out the excellent documentation by checking out this link.

## PostgreSQL

[PostgreSQL](https://www.postgresql.org/) is a powerful, open-source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

- All needed data types are supported in PostgreSQL. PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help you manage your data no matter how big or small the dataset.
- PostgreSQL is highly extensible. For example, you can define your own data types or build out custom functions. PostgreSQL tries to confirm with the SQL standard where such conformance does not contradict traditional features or could lead to poor architectural decisions.
