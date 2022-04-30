# **Vaccination**

## **Technologies**

This project was developed using the following technologies:

- [Python](https://docs.python.org/3/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask-Migrate](https://flask-jwt-extended.readthedocs.io/en/stable/)

<br/>

## **Prerequisites**

### **Install**:

- Python 3.9
- Pip library

<br/>

## **To get started**

### **Follow the steps:**

#### Clone into the repository and go into project's folder:

```bash
$ git clone https://github.com/Kenzie-Academy-Brasil-Developers/q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
$ cd q3-sprint6-autenticacao-e-autorizacao-lsmescolotto
```

#### Create virtual enviroment:

```bash
$ python -m venv venv
```

#### Activate virtual enviroment:

```
 $ source venv/bin/activate
```

#### Install libraries:

```bash
$ pip install -r requirements.txt
```

#### Run flask:

```bash
$ flask run
```

#### Start sending requests:

- Use an API request sending platform like [Insomnia](https://docs.insomnia.rest/#)

  <br/>

## **base URL**

https://vaccination-lsmescolotto.herokuapp.com/vaccinations

<br/>

## **Endpoints**

This API has 2(two) endpoints to: add a new vaccination card and to get all of the cards.

<br/>

## **Authentication not required routes**

<br/>
<h2 align ='center'> Add new vaccination card </h2>
<br/>
 
`POST - REQUEST FORMAT`
```json
{
  "cpf": "01234567898",
  "name": "Pandora",
  "vaccine_name": "jansen",
  "health_unit_name": "COloninha"
}
```
 
If the request is corret, the vaccination card will be added:
 
`POST - RESPONSE FORMAT - STATUS 201`
```json
{
  "cpf": "01234567898",
  "first_shot_date": "Tue, 12 Apr 2022 14:19:46 GMT",
  "health_unit_name": "Coloninha",
  "name": "Pandora",
  "second_shot_date": "Mon, 11 Jul 2022 14:13:24 GMT",
  "vaccine_name": "Jansen"
}
```
If extra keys are sent:

`POST - RESPONSE FORMAT - STATUS 201`

```json
{
  "cpf": "01234567898",
  "first_shot_date": "Tue, 12 Apr 2022 14:19:46 GMT",
  "health_unit_name": "Coloninha",
  "name": "Pandora",
  "second_shot_date": "Mon, 11 Jul 2022 14:13:24 GMT",
  "vaccine_name": "Jansen"
}
```

If the cpf has more than 11 characters:

`STATUS 400`

```json
{
  "error": "cpf value too long"
}
```

If at least one of the inserted values is not a string:

`STATUS 400`

```json
{
  "error": "one or more of the inserted values are not strings"
}
```

If at least one of the keys is missing:

`STATUS 400`

```json
{
  "expected_keys": ["vaccine_name", "name", "health_unit_name", "cpf"],
  "invalid_sent_keys": []
}
```

<h2 align ='center'> Get all vaccination cards </h2>
<br/>

`GET - REQUEST FORMAT`
No Body

`GET - RESPONSE FORMAT - STATUS 200`

```json
[
  {
    "cpf": "01234567898",
    "first_shot_date": "Fri, 29 Apr 2022 20:12:42 GMT",
    "health_unit_name": "Coloninha",
    "name": "Pandora",
    "second_shot_date": "Thu, 28 Jul 2022 20:12:42 GMT",
    "vaccine_name": "Jansen"
  },
  {
    "cpf": "01234567893",
    "first_shot_date": "Fri, 29 Apr 2022 20:12:42 GMT",
    "health_unit_name": "Coloninha",
    "name": "Pandora",
    "second_shot_date": "Thu, 28 Jul 2022 20:12:42 GMT",
    "vaccine_name": "Jansen"
  }
]
```

Developed by [Luiza Schmidt Mescolotto](https://www.linkedin.com/in/luiza-schmidt-mescolotto/)
