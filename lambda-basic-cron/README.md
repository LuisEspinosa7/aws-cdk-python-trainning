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

## Screenshots

<table style="width:100%">
  <tr>
    <td>
  		<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215543939-be3ea620-5ea4-434e-9ebf-e216fd0c2d8b.png">
	  </td>
    <td>
  	<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215544042-1812c28d-5005-4745-9690-0ae1c2f6b8e4.png">
    </td>
  </tr>
</table>


<table style="width:100%">
  <tr>
    <td>
  		<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215544233-8e27dd82-547b-4f5c-bb96-033ccded25cd.png">
	  </td>
    <td>
  	<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215544398-2bd28357-213b-4c71-bd36-1f75ac9e73ef.png">
    </td>
  </tr>
</table>



<table style="width:100%">
  <tr>
    <td>
  		<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215544614-64736ea3-c567-4413-95bd-8aef36f09408.png">
	  </td>
    <td>
  	<img width="450" alt="Image" src="https://user-images.githubusercontent.com/56041525/215544693-908e2f78-9df8-41ad-8197-725e9ce77226.png">
    </td>
  </tr>
</table>



