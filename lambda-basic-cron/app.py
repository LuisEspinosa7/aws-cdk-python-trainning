from aws_cdk import (
    aws_lambda as _lambda,
    aws_events as _events,
    aws_events_targets as targets,
    App, Duration, Stack
)

class LambdaBasicCronStack(Stack):
    def __init__(self, app:App, id: str) -> None: # Constructor
        super().__init__(app, id)
    
        with open("lambda-handler.py", encoding="utf-8") as file: # Load handler method
            handler = file.read()
        
        lambdaFuntion = _lambda.Function(
            self,
            "Singleton",
            code=_lambda.InlineCode(handler),
            handler="index.main",
            timeout=Duration.seconds(60),
            runtime=_lambda.Runtime.PYTHON_3_9
        )
        
        event_rule = _events.Rule(
            self, 
            "Rule",
            schedule=_events.Schedule.cron(
                minute='1',
                hour='*',
                month='*',
                week_day='MON-FRI',
                year='*'
            )
        )
        
        event_rule.add_target(targets.LambdaFunction(lambdaFuntion))


app = App()
LambdaBasicCronStack(app, "LambdaBasicCronExample")
app.synth()