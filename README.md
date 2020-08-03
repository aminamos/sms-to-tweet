# SMS-to-Tweet

## About

Some time ago, Twitter allowed users to add a phone number and send tweets from that verified number. This functionality was [removed](https://mashable.com/article/twitter-sms-changes-account-removals/) but I knew that tweets could still be produced using [Twitter's API](https://developer.twitter.com/en/docs).

Twilio provides a phone number service for individuals and organizations at various sizes. I was able to test and complete this project using their free trial credit amounts.

## Architecture

I used a [Twilio tutorial](https://www.twilio.com/docs/sms/tutorials/how-to-receive-and-reply-python-amazon-lambda) (with a few modifications) to set this up.

The process starts with a text from my cell phone to a number provided by Twilio. The contents of the message are received by Twilio and a request is made to an [AWS API Gateway](https://aws.amazon.com/api-gateway/) endpoint, which invokes an [AWS Lambda](https://aws.amazon.com/lambda/) function. The function communicates with Twitter's API and sends the tweet after successful authentication with my account's credentials.

To summarize:

Text from cell phone -> Twilio phone number -> Twilio request to API Gateway - Lambda function invoked by API Gateway -> Twitter API.

## Contributing

Open an issue in this repository