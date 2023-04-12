from aws_cdk import (
    Stack,
    aws_s3,
)
from constructs import Construct

class CheckovTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline_artifact_bucket = aws_s3.CfnBucket(
            self,
            "PipelineArtifactBucket",
            access_control="Private",
            bucket_encryption=aws_s3.CfnBucket.BucketEncryptionProperty(
                server_side_encryption_configuration=[
                    aws_s3.CfnBucket.ServerSideEncryptionRuleProperty(
                        server_side_encryption_by_default=aws_s3.CfnBucket.ServerSideEncryptionByDefaultProperty(
                            sse_algorithm="AES256"
                        )
                    )
                ]
            ),
            public_access_block_configuration=aws_s3.BlockPublicAccess.BLOCK_ALL
        )
        pipeline_artifact_bucket.cfn_options.metadata = {
          'checkov': {
            'skip': [
              {
                'id': 'CKV_AWS_18',
                'comment': 'No need to ensure the S3 bucket has access logging enabled'
              }
            ]
          }
        }
