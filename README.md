# FastAPI Challenge

Challenge project set up for CRUD APIs, using:

Backend:
* FastApi
* SQLAlchemy for ORM
* alembic for migrations
* psycopg2 for Postgres connection

Deploy:
* Terraform
* Amazon Web Services (ECS)
* Cognito+Google for identity


## Deployment Diagram

![Challenge Diagram](./terraform/deploy-diagram.jpg)

## API Usage:

**API Endpoint**: http://dev-dev-2008722471.us-east-1.elb.amazonaws.com  
**API documentation**: http://dev-dev-2008722471.us-east-1.elb.amazonaws.com/docs

In order to use the Rest API, you need to generate a JWT Token from Amazon Cognito:

1) Open the following URL on a browser.

https://rrobledo-dev.auth.us-east-1.amazoncognito.com/login?client_id=4jpqa5b9h3lpklg8j81o83up0i&response_type=token&scope=aws.cognito.signin.user.admin+email+openid+profile&redirect_uri=https://rrobledo.htmlsave.net/callback.html

2) Sign-in using a google account, Then shall be redirected to a page where the you can get te access token  

Some example how to use the rest api

Adding a new product
```
curl -X POST \
  http://dev-dev-2008722471.us-east-1.elb.amazonaws.com/v1/products \
  -H 'authorization: Bearer eyJraWQiOiJkNEVrM1owQ3FleGtRSFNWaVB5NHNDajg1TXBuVmhIWlV6ZWtYd0hrbnB3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ODQ2NGE2Ni1jY2E4LTQ3NjItYjUwZi0zMTdhNTBiMjM4MjQiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfTm96UXhEemRIX0dvb2dsZSJdLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNjAwNDUwNjE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Ob3pReER6ZEgiLCJleHAiOjE2MDA0NTQyMTQsImlhdCI6MTYwMDQ1MDYxNCwidmVyc2lvbiI6MiwianRpIjoiYWM5MThmMTctNTU5ZC00NGY0LWFlMzctOWZjMmIxY2NlM2YyIiwiY2xpZW50X2lkIjoiNGpwcWE1YjloM2xwa2xnOGo4MW84M3VwMGkiLCJ1c2VybmFtZSI6Ikdvb2dsZV8xMTA0OTA5MDkwMzY2MDI5MDkzNDgifQ.qwORtiS-nv7Ifkt0Phy55l3ateZr-cM6fFeo5orUDMea6QZenmYX24QxwjVB-0uqSQsu6vG0Fwi6tTsG2UO-WeTCjJpJZyZdzSs1UhMA5NLa-Pj07uyaS-4V3d3uX-84NaSqpoLSC_RFvwtsH1e9gNhRmxDIaxQYj_E0haTGD9IBZ8kiYaHDiyXK6OAzgxIP0UnOgEnOMrivJWnIAgHi_VQ9WVSahOV1ygDcl1YQND_k9iPXWjGS-tcaOC9W2MRj10t_OjlWz5Ncp_2cFA7ebGfKHS7KW2ftfaLWwChr514pRPk7qletQSwh1qdmVQGHEj0P_ORBvRbfuo0XvndRcw' \
  -H 'content-type: application/json' \
  -d '{
	"description":  "product 01"
}'
```

Get list of products
```
curl -X GET \
  http://dev-dev-2008722471.us-east-1.elb.amazonaws.com/v1/products \
  -H 'authorization: Bearer eyJraWQiOiJkNEVrM1owQ3FleGtRSFNWaVB5NHNDajg1TXBuVmhIWlV6ZWtYd0hrbnB3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ODQ2NGE2Ni1jY2E4LTQ3NjItYjUwZi0zMTdhNTBiMjM4MjQiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfTm96UXhEemRIX0dvb2dsZSJdLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNjAwNDUwNjE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Ob3pReER6ZEgiLCJleHAiOjE2MDA0NTQyMTQsImlhdCI6MTYwMDQ1MDYxNCwidmVyc2lvbiI6MiwianRpIjoiYWM5MThmMTctNTU5ZC00NGY0LWFlMzctOWZjMmIxY2NlM2YyIiwiY2xpZW50X2lkIjoiNGpwcWE1YjloM2xwa2xnOGo4MW84M3VwMGkiLCJ1c2VybmFtZSI6Ikdvb2dsZV8xMTA0OTA5MDkwMzY2MDI5MDkzNDgifQ.qwORtiS-nv7Ifkt0Phy55l3ateZr-cM6fFeo5orUDMea6QZenmYX24QxwjVB-0uqSQsu6vG0Fwi6tTsG2UO-WeTCjJpJZyZdzSs1UhMA5NLa-Pj07uyaS-4V3d3uX-84NaSqpoLSC_RFvwtsH1e9gNhRmxDIaxQYj_E0haTGD9IBZ8kiYaHDiyXK6OAzgxIP0UnOgEnOMrivJWnIAgHi_VQ9WVSahOV1ygDcl1YQND_k9iPXWjGS-tcaOC9W2MRj10t_OjlWz5Ncp_2cFA7ebGfKHS7KW2ftfaLWwChr514pRPk7qletQSwh1qdmVQGHEj0P_ORBvRbfuo0XvndRcw' \
  -H 'content-type: application/json'
```

Add a new transaction
```
curl -X POST \
  http://dev-dev-2008722471.us-east-1.elb.amazonaws.com/v1/transactions \
  -H 'authorization: Bearer eyJraWQiOiJkNEVrM1owQ3FleGtRSFNWaVB5NHNDajg1TXBuVmhIWlV6ZWtYd0hrbnB3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ODQ2NGE2Ni1jY2E4LTQ3NjItYjUwZi0zMTdhNTBiMjM4MjQiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfTm96UXhEemRIX0dvb2dsZSJdLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNjAwNDUwNjE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Ob3pReER6ZEgiLCJleHAiOjE2MDA0NTQyMTQsImlhdCI6MTYwMDQ1MDYxNCwidmVyc2lvbiI6MiwianRpIjoiYWM5MThmMTctNTU5ZC00NGY0LWFlMzctOWZjMmIxY2NlM2YyIiwiY2xpZW50X2lkIjoiNGpwcWE1YjloM2xwa2xnOGo4MW84M3VwMGkiLCJ1c2VybmFtZSI6Ikdvb2dsZV8xMTA0OTA5MDkwMzY2MDI5MDkzNDgifQ.qwORtiS-nv7Ifkt0Phy55l3ateZr-cM6fFeo5orUDMea6QZenmYX24QxwjVB-0uqSQsu6vG0Fwi6tTsG2UO-WeTCjJpJZyZdzSs1UhMA5NLa-Pj07uyaS-4V3d3uX-84NaSqpoLSC_RFvwtsH1e9gNhRmxDIaxQYj_E0haTGD9IBZ8kiYaHDiyXK6OAzgxIP0UnOgEnOMrivJWnIAgHi_VQ9WVSahOV1ygDcl1YQND_k9iPXWjGS-tcaOC9W2MRj10t_OjlWz5Ncp_2cFA7ebGfKHS7KW2ftfaLWwChr514pRPk7qletQSwh1qdmVQGHEj0P_ORBvRbfuo0XvndRcw' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 1737b47c-bab6-6ad8-0978-31a678538dbb' \
  -d '{
	"type": "PAYMENT",
	"description": "Transaction 01",
	"amount": 100.00,
	"user_id": "68464a66-cca8-4762-b50f-317a50b23824",
	"items": [
	  {
	    "product_id": "9c4ef9f0-575f-4e2f-b820-2989ceddf22a",
	    "quantity": 1,
	    "amount": 100.00
	  }
	]
}
'
```

Get list of transactions
```
curl -X GET \
  http://dev-dev-2008722471.us-east-1.elb.amazonaws.com/v1/transactions \
  -H 'authorization: Bearer eyJraWQiOiJkNEVrM1owQ3FleGtRSFNWaVB5NHNDajg1TXBuVmhIWlV6ZWtYd0hrbnB3PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2ODQ2NGE2Ni1jY2E4LTQ3NjItYjUwZi0zMTdhNTBiMjM4MjQiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfTm96UXhEemRIX0dvb2dsZSJdLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNjAwNDUwNjE0LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Ob3pReER6ZEgiLCJleHAiOjE2MDA0NTQyMTQsImlhdCI6MTYwMDQ1MDYxNCwidmVyc2lvbiI6MiwianRpIjoiYWM5MThmMTctNTU5ZC00NGY0LWFlMzctOWZjMmIxY2NlM2YyIiwiY2xpZW50X2lkIjoiNGpwcWE1YjloM2xwa2xnOGo4MW84M3VwMGkiLCJ1c2VybmFtZSI6Ikdvb2dsZV8xMTA0OTA5MDkwMzY2MDI5MDkzNDgifQ.qwORtiS-nv7Ifkt0Phy55l3ateZr-cM6fFeo5orUDMea6QZenmYX24QxwjVB-0uqSQsu6vG0Fwi6tTsG2UO-WeTCjJpJZyZdzSs1UhMA5NLa-Pj07uyaS-4V3d3uX-84NaSqpoLSC_RFvwtsH1e9gNhRmxDIaxQYj_E0haTGD9IBZ8kiYaHDiyXK6OAzgxIP0UnOgEnOMrivJWnIAgHi_VQ9WVSahOV1ygDcl1YQND_k9iPXWjGS-tcaOC9W2MRj10t_OjlWz5Ncp_2cFA7ebGfKHS7KW2ftfaLWwChr514pRPk7qletQSwh1qdmVQGHEj0P_ORBvRbfuo0XvndRcw' \
  -H 'content-type: application/json' 
```

## Development Usage

The commands for operating are included in the `Makefile`.
