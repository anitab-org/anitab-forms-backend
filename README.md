# Open Source Programs (Backend)
Open Source Programs (OSP) is an application that simplifies the processing and selection procedure of Open Source Programs of AnitaB.org Open Source or other third-party programs. This is the Backend repo for OSP.

## Tech Stack
- Django 3.0.7
- Django REST Framework 3.11.0
- Python 3.7+

## API Documentation
- [Postman Docs](https://documenter.getpostman.com/view/11324046/Szzoaw1q?version=latest)

## Setup 
To setup the project locally go through [this wiki page](https://github.com/anitab-org/open-source-programs-web/wiki/Fork,-Clone,-Remote-and-Pull-Request).
Make sure you have installed the following:
* [pip](https://pip.pypa.io/en/stable/installing/)
* [virtualenv](https://pypi.org/project/virtualenv/)
* [PostgreSQL](https://www.postgresql.org/docs/9.5/install-procedure.html)

Next follow these instructions.

1. You can register a new user by setting up SendGrid details in the settings.py , you can take a refrence from [here](https://sendgrid.com/docs/for-developers/sending-email/integrating-with-the-smtp-api/)

2. **Database Setup:** Before starting with the project create a db in you local using PostgreSQL with the following details. Refer to `main/settings.py` if you have any confusion.

    ```
    NAME: osp
    USER: osp
    PASSWORD: osp
    HOST: localhost
    ``` 
    You may run the following commands for local setup of DB in Linux:

    ```
    cd open-source-programs-backend
    sudo -i -u postgres
    createuser osp --pwprompt
    psql
    CREATE DATABASE osp;
    \c osp;
    GRANT ALL PRIVILEGES ON DATABASE osp to osp;
    ```
3. You need to download API key file from your user-settings on Zulip. The file you download is named as 'download' or rename that to 'download'.
4. Place that download file in the project's directory.

5. Move into the project's directory.

    ```
    cd open-source-programs-backend
    ```
6. Create virtual environment (this is not a hard requirement, but its advisable)
    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
7. To run the migrations run: 
   ```
   python manage.py migrate
   ```
8. To run the server:
    ```
    python manage.py runserver
    ```
9. Navigate to `http://localhost:8000/` in your browser.
10. To change the port you may run `python manage.py runserver 0.0.0.0:<port_number>`
11. To run the migrations run: `python manage.py migrate`
12. You can terminate the process by `Ctrl+C` in your terminal.

Follow the given instructions for Login into the app.

1. To create the superuser run:
   ```
   python manage.py createsuperuser
   ````
   Fill up the things it asked to and then Login into the app.

## Contributing
Please read the Contibuting guidelines, [Code of Conduct](https://github.com/anitab-org/open-source-programs-backend/blob/develop/CODE_OF_CONDUCT.md) and [Reporting Guidelines](https://github.com/anitab-org/open-source-programs-backend/blob/develop/REPORTING_GUIDELINES.md)

## Contact
You can reach the admins, maintainers and our community on [AnitaB.org Open Source Zulip](https://anitab-org.zulipchat.com/). If you are interested in contributing to the OSP project, you may join the stream [#open-source-progs](https://anitab-org.zulipchat.com/#narrow/stream/237907-open-source-progs) and ask questions or intereact with the community. Join Us!
