# chime-ice-breaker

This serverless application periodically sends a random ice breaker question to the given Chime or Slack webhook URL based on the provided schedule.

This app was built for teams that are 100% remote, for example, due to COVID-19, and use Amazon Chime or Slack as their key team collaboration tool. While we've solved a lot of the barriers to getting work done while remote, there are fewer replacements for the informal human interactions that happen organically when physically sharing an office space. Things like small talk, jokes, and learning random things about one another.

This app is meant to help address this by periodically sending a random ice breaker question like this to your team Chime or Slack room:

Chime example:

![chime screenshot](https://github.com/jlhood/chime-ice-breaker/raw/master/images/example-chime-screenshot.png)

Slack example:

![slack screenshot](https://github.com/jlhood/chime-ice-breaker/raw/master/images/example-slack-screenshot.png)

## Installation Instructions

### Webhook URL

#### Amazon Chime

To create a Chime Webhook URL for your Chime room using the Chime client application, click on the gear icon in the upper right corner of your Chime room and select "Manage webhooks and bots". Note, you must be an administrator of the Chime room to set this option.

![webhook setup 1](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-1.png)

A popup dialog should appear. Click the "Add webhook" link.

![webhook setup 2](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-2.png)

Enter a name for your Webhook, e.g., "Ice Breaker", and click the Create button.

![webhook setup 3](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-3.png)

You now have a new Chime webhook. Click the "Copy URL" link to copy the Chime webhook URL to your clipboard. This is the URL you should enter as the `ChimeUrl` parameter value when installing the chime-ice-breaker app.

![webhook setup 4](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-4.png)

#### Slack

To create a [Slack Workflow](https://slack.com/help/articles/360053571454-Set-up-a-workflow-in-Slack#:~:text=step%201%3A%20open%20workflow%20builder) with a webhook, from your desktop Slack application, click your workspace name in the top left.

![webhook setup 5](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-5.png)

Select "Tools" > "Workflow Builder" from the menu.

From the Workflow Builder, click "Create" in the top right.

![webhook setup 6](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-6.png)

Enter a name for your workflow, then click "Next".

![webhook setup 7](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-7.png)

Select "Webhook" as the workflow trigger.

Click "Add variable". For "key", enter "Content". Choose "Text" data type. Click "Next".

![webhook setup 8](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-8.png)

Click "Add Step".

![webhook setup 9](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-9.png)

Select "Send a message".

Choose the channel where you'd like ice breaker questions to be posted. For the message text, click "Insert new variable" and choose "Content". Click "Save".

![webhook setup 10](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-10.png)

Click "Publish" in the top right corner to publish the workflow and generate a webhook URL.

![webhook setup 11](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-11.png)

You now have a new Slack webhook. Click the "Copy" button to copy the Slack webhook URL to your clipboard. This is the URL you should enter as the `ChimeUrl` parameter value when installing the chime-ice-breaker app.

![webhook setup 12](https://github.com/jlhood/chime-ice-breaker/raw/master/images/webhook-setup-12.png)

### Installing the app

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login
1. Go to the app's page on the [Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:277187709615:applications~chime-ice-breaker) and click "Deploy"
1. Provide the required app parameters (see parameter details below) and click "Deploy"

## App Parameters

1. `ChimeUrl` - Chime or Slack webhook URL to send the ice-breaker question to.
1. `ScheduleExpression` - An EventBridge schedule expression dictating the frequency at which ice-breaker questions will be sent (see https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html). Default: `cron(30 18 ? * MON-FRI *)`
1. `LogLevel` (optional) - Log level for Lambda function logging, e.g., ERROR, INFO, DEBUG, etc. Default: INFO

## License Summary

This code is made available under the MIT license. See the LICENSE file.