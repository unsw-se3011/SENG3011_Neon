# Testing

We use Swagger for black-box testing, documented in Reports/TestingDoc.md on github.

## Whitebox testing

We use Django unit tests, defined in [test.py](../API_SourceCode/report/tests.py) and sample result is in [django.out](./django.out).

## Black Box testing

Black box testing is described in [Testingdoc.md](../../Reports/TestingDoc.md)

### REST Client

We use the plugin in the vscode and documented as [api.http](../API_Documentation/api.http)

### Swagger

We are required to use [swagger](http://neon.whiteboard.house/swagger/#/Report/get_reports_) to document our api.

### JMeter

We use JMeter to test our performance and script is [API_test.jmx](./API_test.jmx).

### Shell

We use shell script to test it as scipts: [test.sh](./test.sh) and [testReport.sh](./testReport.sh).
The expect format is in [curl-format.txt](./curl-format.txt)
