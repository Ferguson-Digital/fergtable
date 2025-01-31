## Fergtable

This is a fork of Baserow. Here is what has been changed/added:

* The "User field names" option for the API now causes it to use API names for fields instead of the normal field names. Field API names can be configured on the frontend, and are unique per table.
* Tables can be interfaced with through the API using API names, which can be configured on the frontend. They do not have to be unique, and if they are not, the newest table with the same API name is preferred.
* "Super Admins" can be specified by email in `.env`. These are users that get automatically added to every group with admin permissions and cannot be removed.
* New users without a group invitation no longer get a new group created for them.
* Thumbnail generation for PDF & other office suite document formats (text, presentation, & spreadsheet), plus more thumbnail sizes.
* Better table navigation and selection with shift+arrows and shift+click.
* Tooltips showing full field name when column is too short to display the full name.
* Select fields' "edit field" popup is scrollable, doesn't have random option colors, and can be navigated with up/down/enter keys.
* All API documentation links open a new tab. Also added a link to the Baserow API's redoc page & to the Ferguson Digital wiki page on Baserow.
* Webhooks no longer get automatically disabled after failing too many requests.
* A Python script for automated backup & restore of the Postgres database and automated snapshots of all Baserow databases.

### Deploying

1. Copy `.env.defaults` to `.env` and fill in the required variables (The ones that aren't commented out).
1. Run `docker compose up`.
1. If changes have been made to the source code, run with `--build` flag.

### Local Hosting for Development

1. Copy `.env.defaults` to `.env` and: 
   1. Fill in the first three variables with some random strings. Just mash your keyboard or something.
   1. Set `BASEROW_PUBLIC_URL` to `http://localhost`.
   1. Comment out `BASEROW_CADDY_ADDRESSES`.
   1. Set `SUPER_ADMINS` to your email or a dummy email.
   1. Either comment out all the email variables or get the SMTP password and fill it in.
1. Make sure docker is running.
1. Run `docker compose up --build`.
1. Go to `http://localhost` in your browser.

Below is all of Baserow's README:

## Baserow is an open source no-code database tool and Airtable alternative.

Create your own online database without technical experience. Our user-friendly no-code
tool gives you the powers of a developer without leaving your browser.

* A spreadsheet database hybrid combining ease of use and powerful data organization.
* Easily self-hosted with no storage restrictions or sign-up on https://baserow.io to
  get started immediately.
* Alternative to Airtable.
* Open-core with all non-premium and non-enterprise features under
  the [MIT License](https://choosealicense.com/licenses/mit/) allowing commercial and
  private use.
* Headless and API first.
* Uses popular frameworks and tools like [Django](https://www.djangoproject.com/),
  [Vue.js](https://vuejs.org/) and [PostgreSQL](https://www.postgresql.org/).

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/bram2w/baserow/tree/master)

```bash
docker run -v baserow_data:/baserow/data -p 80:80 -p 443:443 baserow/baserow:1.15.2
```

![Baserow screenshot](docs/assets/screenshot.png "Baserow screenshot")

## Get Involved

**We're hiring remotely**! More information at https://baserow.io/jobs.

Join our forum on https://community.baserow.io/ or on Gitter via
https://gitter.im/bramw-baserow/community. See [CONTRIBUTING.md](./CONTRIBUTING.md) on
how to become a contributor.

## Installation

* [**Docker**](docs/installation/install-with-docker.md)
* [**Ubuntu**](docs/installation/install-on-ubuntu.md)
* [**Docker Compose** ](docs/installation/install-with-docker-compose.md)
* [**
  Heroku**: Easily install and scale up Baserow on Heroku.](docs/installation/install-on-heroku.md)
* [**
  Render**: Easily install and scale up Baserow on Render.](docs/installation/install-on-render.md)
* [**
  Cloudron**: Install and update Baserow on your own Cloudron server.](docs/installation/install-on-cloudron.md)

## Official documentation

The official documentation can be found on the website at https://baserow.io/docs/index
or [here](./docs/index.md) inside the repository. The API docs can be found here at
https://api.baserow.io/api/redoc/ or if you are looking for the OpenAPI schema here
https://api.baserow.io/api/schema.json.

## Become a sponsor

If you would like to get new features faster, then you might want to consider becoming a
sponsor. By becoming a sponsor we can spend more time on Baserow which means faster
development.

[Become a GitHub Sponsor](https://github.com/sponsors/bram2w)

## Development environment

If you want to contribute to Baserow you can setup a development environment like so:

```
$ git clone https://gitlab.com/bramw/baserow.git
$ cd baserow
$ ./dev.sh --build
```

The Baserow development environment is now running.
Visit [http://localhost:3000](http://localhost:3000) in your browser to see a working
version in development mode with hot code reloading and other dev features enabled.

More detailed instructions and more information about the development environment can be
found
at [https://baserow.io/docs/development/development-environment](./docs/development/development-environment.md)
.

## Plugin development

Because of the modular architecture of Baserow it is possible to create plugins. Make
your own fields, views, applications, pages or endpoints. We also have a plugin
boilerplate to get you started right away. More information can be found in the
[plugin introduction](./docs/plugins/introduction.md) and in the
[plugin boilerplate docs](./docs/plugins/boilerplate.md).

## Meta

Created by Baserow B.V. - bram@baserow.io.

Distributes under the MIT license. See `LICENSE` for more information.

Version: 1.15.2

The official repository can be found at https://gitlab.com/bramw/baserow.

The changelog can be found [here](./changelog.md).

Become a GitHub Sponsor [here](https://github.com/sponsors/bram2w).

Community chat via https://gitter.im/bramw-baserow/community.
