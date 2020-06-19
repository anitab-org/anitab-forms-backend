# Open Source Programs (Backend)
Open Source Programs (OSP) is an application that simplifies the processing and selection procedure of Open Source Programs of AnitaB.org Open Source or other third-party programs. This is the Backend repo for OSP.

## Tech Stack
- Django 3.0.7
- Django REST Framework 3.11.0

## Setup 
To setup the project locally go through [this wiki page](https://github.com/anitab-org/open-source-programs-web/wiki/Fork,-Clone,-Remote-and-Pull-Request).
Make sure you have installed the following:
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [PostgreSQL](https://www.postgresql.org/docs/9.5/install-procedure.html)

Next follow these instructions.

1. **Database Setup:** Before starting with the project create a db in you local using PostgreSQL with the following details. Refer to `main/settings.py` if you have any confusion.

    ```
    NAME: osp
    USER: osp
    PASSWORD: osp
    HOST: localhost
    ``` 
    You may run the following commands for local setup of DB:

    ```
    sudo -i -u postgres
    createuser osp --pwprompt
    psql
    CREATE DATABASE osp;
    \c osp;
    GRANT ON PRIVILEGES ON DATABASE systersdb to osp;
    ```


2. To start the server:

    ```
    cd open-source-programs-backend
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py runserver
    ```
3. Navigate to `http://localhost:8000/` in your browser.
4. To change the port you may run `python manage.py runserver 0.0.0.0:<port_number>`
5. To run the migrations run: `python manage.py migrate`
6. You can terminate the process by `Ctrl+C` in your terminal.

## Contributing
Please read the Contibuting guidelines, [Code of Conduct](https://github.com/anitab-org/open-source-programs-backend/blob/develop/CODE_OF_CONDUCT.md) and [Reporting Guidelines](https://github.com/anitab-org/open-source-programs-backend/blob/develop/REPORTING_GUIDELINES.md)

## Contact
You can reach the admins, maintainers and our community on [AnitaB.org Open Source Zulip](https://anitab-org.zulipchat.com/). If you are interested in contributing to the OSP project, you may join the stream [#open-source-progs](https://anitab-org.zulipchat.com/#narrow/stream/237907-open-source-progs) and ask questions or intereact with the community. Join Us!
