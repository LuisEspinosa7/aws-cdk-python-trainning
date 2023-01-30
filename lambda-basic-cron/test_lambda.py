import pytest

from aws_cdk import App, Stack
from aws_cdk.assertions import Capture, Match, Template
from app import LambdaBasicCronStack

app = App()
stack = LambdaBasicCronStack(app, "LambdaBasicCronExample")
template = Template.from_stack(stack)

class TestOnlyLambda:
  def test_specified_resources_created(self):
    template.resource_count_is('AWS::Lambda::Function', 1) #Only1
    template.resource_count_is('AWS::Events::Rule', 1) #Only1

  def test_lambda_function_has_correct_properties(self):
    dependency_capture = Capture()
    template.has_resource('AWS::Lambda::Function', {
      'Properties':{
        'Handler': 'index.main',
        'Runtime': 'python3.9',
        'Timeout': 60,
      },
      'DependsOn':[dependency_capture]
    })

    assert 'SingletonServiceRole' in dependency_capture.as_string()

  def test_lambda_has_correct_iam_permissions(self):
    role_capture = Capture()
    template.has_resource_properties('AWS::IAM::Role', {
      'AssumeRolePolicyDocument': Match.object_like({
        'Statement': [{
          'Action': 'sts:AssumeRole',
          'Effect': 'Allow',
          'Principal': {
            'Service': 'lambda.amazonaws.com'
          },
        }],
      }),
      'ManagedPolicyArns': [{
        'Fn::Join': Match.array_with([
          [ 'arn:', { 'Ref': 'AWS::Partition' }, role_capture ],
        ]),
      }],
    })

    assert 'AWSLambdaBasicExecutionRole' in role_capture.as_string()

  def test_lambda_not_running_in_vpc(self):
    template.has_resource('AWS::Lambda::Function', {
      'Vpc': Match.absent()
    })

class TestEvents:
  def test_event_has_correct_rule(self):
    template.has_resource_properties('AWS::Events::Rule', {
      'ScheduleExpression': 'cron(* * ? * 1-7 *)',
      'State': 'ENABLED',
      'Targets': Match.any_value(),
    })