# backend-API

# About

In this section there is the source code for the api that is deployed on the google compute engine. This API uses a compute engine because to read machine learning models it requires tensorflow which cannot be done using the app engine. The compute specifications used are as follows:


```
Region: asia-southeast1(Singapore)
Zona: asia-southeast1-b
Machine type: e2-medium (2 vCPU,4 GB memory)
```

and also we use cloud SQL for database space

```
Region: asia-southeast1(Singapore)
Machine type: db-lightweight-1 (1 vCPU,3.75 GB memory)
Size: 10GB SSD
```

# RESTful APIs

In making the **RESTful APIs** we use [Python](https://github.com/python) using the [Flask Framework](https://flask.palletsprojects.com/en/2.0.x/) and for responses using **JSON** format. For each URL that can be used will be explained below.

**Base url API** 

> http://34.126.139.160/api

## Documentation API

you can check the documentation of API in [here](https://agungprabowo8800.gitbook.io/babakbelur-aic/)
