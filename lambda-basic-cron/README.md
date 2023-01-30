# Lambda basic cron

---

Lambda basic cron creates a lambda which executes a handler every 5 minutes, managed by a cron scheduled event.

## Build

Install the latest version of the AWS CDK CLI:

```shell
$ npm i -g aws-cdk
```

Execute the following command in the root folder:

```bash
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Tests

Execute the tests with the following command:

```bash
pytest test_lambda-cron.py
```

## Generate Cloudformation Template

To generate (Synthesize) the Cloudformation template run and give a look inside the "cdk.out" folder:

```
cdk synth
```

## Deploy

To deploy the Stack, run:
```
cdk deploy
```

As a result you will see the API's URL for the lambda.