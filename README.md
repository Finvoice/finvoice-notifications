# finvoice-notifications
This repo will contain lambda's to send out notifications (emails for now) to finvoice users.  

### We have the following lambda's
1. event_notification --> triggered for every message sent to the SNS topic (staging_platform_events in staging and production_platform_events in production)  

### Setting up local environment
1. Install serverless 
2. Install python 3.6
3. Validate following commands returns 3.6
```
python --version
``` 
4. If not add following alias (add it to bash profile so its applied every time)
```
alias python=python3.6
```
### Run tests
```python -m unittest src/tests/email_helper_tests.py```

### To run the lambda locally
1. Run following command to check the version
```python --version```
2. If above does not return 3.6 then run the following command
```alias python=python3.6```
3. Check version again - you may want to add above alias command to ~/.bash_profile if you do not want to set it manually everytime
4. Install boto3 library
```pip3 install boto3```
5. Run the lambda locally  
```sls invoke local --function event_notification --stage local```

### deploy to staging
```serverless deploy -v --stage dev```

### Trigger lambda that is deployed in staging
```serverless invoke -f analytics_email_trigger --stage dev```

### deploy to production
```serverless deploy -v --stage prod```