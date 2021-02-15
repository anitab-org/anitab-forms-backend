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

1. **Database Setup:** Before starting with the project create a db in you local using PostgreSQL with the following details. Refer to `main/settings.py` if you have any confusion.

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
2. You need to download API key file from your user-settings on Zulip. The file you download is named as 'download' or rename that to 'download'.
3. Place that download file in the project's directory.

4. Move into the project's directory.

    ```
    cd open-source-programs-backend
    ```
5. Create virtual environment (this is not a hard requirement, but its advisable)
    ```
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
6. To run the migrations run: 
   ```
   python manage.py migrate
   ```
7. To run the server:
    ```
    python manage.py runserver
    ```
8. Navigate to `http://localhost:8000/` in your browser.
9. To change the port you may run `python manage.py runserver <port_number>`
10. To run the migrations run: `python manage.py migrate`
11. You can terminate the process by `Ctrl+C` in your terminal.

Follow the given instructions for Login into the app.

1. You can register a new user by setting up SendGrid details in the `settings.py`, you can take a reference from [here](https://sendgrid.com/docs/for-developers/sending-email/integrating-with-the-smtp-api/)

2. To create the superuser run:
   ```
   python manage.py createsuperuser
   ````
   Fill up the things it asked to and then Login into the app.

## Environment Variables

1. zulip_id : You can go [Zulip](https://anitab-org.zulipchat.com) and click on your name from the user list on the right. On the URL, you will see a number after user. That is your Zulip user ID.

2. SENDGRID_API_KEY : Follow the given steps to create a Sendgrid API key -

	- Go to [Sendgrid's website](https://app.sendgrid.com/guide)

	- Navigate to Settings on the left navigation bar, and then - select API Keys.

	- Click Create API Key.

	- Give your API key a name.

	- Select Full Access, Restricted Access, or Billing Access. If you're selecting Restricted Access, or Billing Access, select the specific permissions to give each category. For more information, see API key permissions.

	- Click Create & View.

	- The API KEY is generated and displayed to you just once. So be sure to copy and save it somewhere.

Add both of these variables to your .env file as follows:
```
export zulip_id=<your-zulip-id>
export SENDGRID_API_KEY=<your-sendgrid-api-key>
```

## Testing

To run the tests run: `python manage.py test`.

### Run with Docker

1. Make sure the latest version of docker and docker-compose are installed.

- For **docker** run ``docker -v`` from your terminal. If docker is not installed, install it from [here](https://docs.docker.com/engine/install/).
- For **docker-compose** run ``docker-compose -v`` from terminal. If it is not installed then install it by running ``pip install docker-compose`` or from [here](https://docs.docker.com/compose/install/).

2. Change Database HOST in ``settings.py``

- Go to ``main/settings.py``
- Under databases change host to db.

3. **Build docker image**

Execute ``sudo docker-compose run web`` to build the image.

4. **Run docker image**

Run ``sudo docker-compose up`` from the root directory of project. Navigate to `http://localhost:8000` in your browser.

**Note** 
- Run `docker-compose up --build` to rebuild the image.
- To **interact** with docker containers use ``docker exec -it {container id} bash`` from your terminal. Container id can be found using ``docker ps``.

## Documentation

- Read the [Meeting minutes](https://docs.google.com/document/d/1YF13IbBrU1ln4ZF1fOpgb-xGRgIF6tZLSjIBQgDmN7k/edit) notes from our open sessions about the project.
- For setting up the project locally watch [this video](https://youtu.be/_b2RQGbYN9w).
- To learn about the project's initial features, watch the video of [project demonstration](https://youtu.be/3A746GppZ0Y).
- [Design and Mocks Google Drive folder](https://drive.google.com/drive/folders/1MybSH3f8peXGUSRxhDydDtoAi8WJL1th).
- [Timeline deliverables for the project during GSoC 2020](https://docs.google.com/document/d/1xl9F5kMZrKo4mNhnP0SKpk7WkQc8PLca1ym7EZMpjSc/edit).
- [GSoC 2020 Project Meeting Minutes](https://docs.google.com/document/d/1YF13IbBrU1ln4ZF1fOpgb-xGRgIF6tZLSjIBQgDmN7k/edit).

For more information, you can read [backend project wiki](https://github.com/anitab-org/open-source-programs-backend/wiki) and the [web project wiki](https://github.com/anitab-org/open-source-programs-web/wiki).

## Contributing
Please read the [Contributing guidelines](.github/CONTRIBUTING.md), [Code of Conduct](CODE_OF_CONDUCT.md) and [Reporting Guidelines](REPORTING_GUIDELINES.md)

## Contact
You can reach the admins, maintainers and our community on [AnitaB.org Open Source Zulip](https://anitab-org.zulipchat.com/). If you are interested in contributing to the OSP project, you may join the stream [#open-source-progs](https://anitab-org.zulipchat.com/#narrow/stream/237907-open-source-progs) and ask questions or intereact with the community. Join Us!
