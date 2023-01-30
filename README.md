# AWS CDK Python Trainning

This repository contains several example implementations of infraestructure as code in python using AWS CDK. This is part of my
personal trainning as well as my portfolio.

## Installation

### Step 1
1. Install CDK
```
$ npm install -g aws-cdk
```

2. Create a Python virtual environment
```
$ python3 -m venv .venv
```

3. Activate virtual environment

Example for Linux and MacOS 
```
$ source .venv/bin/activate
```

Example for Windows
```
% .venv\Scripts\activate.bat
```

4. Install dependencies.

```
$ pip install -r requirements.txt
```

5. Synthesize (`cdk synth`) or deploy (`cdk deploy`) the example

```
$ cdk deploy
```

### Cleaning

Only the resources with no dependencies and data will be deleted.
```
$ cdk destroy
```

## Examples

| Name    | Description |
|---------|-------------|
| [lambda-basic-cron](https://github.com/LuisEspinosa7/aws-cdk-python-trainning/tree/main/lambda-basic-cron) | Basic Lambda with EventBridge scheduled event |
