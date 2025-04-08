# Countries API

The Countries API is a Django-based RESTful API that provides information about different countries. It allows users to retrieve, create, update, and delete country data.

## Introduction

The Countries API is built using Django, a powerful and flexible web framework for Python. It utilizes Django REST framework to expose the country data through a RESTful API.

## Features

- List all countries with their details
- Retrieve information about a specific country by its ID
- Create new countries
- Update country details
- Delete countries

## Setup

1. Clone the repository:

```bash
git clone https://github.com/sosmongare/countries_api.git
cd countries_api
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv env
# For Windows:
. env/Scripts/activate

# For macOS/Linux:
source . env/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the database settings:

   - Open `countries_api/settings.py` and update the `DATABASES` settings to use your MySQL database credentials.

5. Apply migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

The API will now be accessible at `http://localhost:8000/countries/`.

## API Endpoints

The Countries API provides the following endpoints:

- `GET /countries/`: Retrieve a list of all countries.
- `GET /countries/<id>/`: Retrieve information about a specific country by its ID.
- `POST /countries/`: Create a new country.
- `PUT /countries/<id>/`: Update details of a specific country by its ID.
- `DELETE /countries/<id>/`: Delete a specific country by its ID.

## Usage

You can interact with the Countries API using tools like cURL, Postman, or any other HTTP client. For example:

- To retrieve all countries:
```bash
curl -X GET http://localhost:8000/countries/
```

- To create a new country:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"New Country", "capital":"Capital City", "population":1000000}' http://localhost:8000/countries/
```

- To update a country:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Country", "capital":"Updated Capital City"}' http://localhost:8000/countries/<id>/
```

- To delete a country:
```bash
curl -X DELETE http://localhost:8000/countries/<id>/
```

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---