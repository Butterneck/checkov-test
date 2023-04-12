import aws_cdk as core
import aws_cdk.assertions as assertions

from checkov_test.checkov_test_stack import CheckovTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in checkov_test/checkov_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CheckovTestStack(app, "checkov-test")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
