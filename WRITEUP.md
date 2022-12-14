# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

#### For Virtual Machine
- Deploying to VMs for a lightweight project like this will be more time consuming 
- It is also more expensive than App Service

#### For App Service
- This is more suited for hosting lightweight web application
- Allows developers to focus on the application
- Easy integration of Continous deployment using Github
- It is very cheap, because I will used the free Dev/Test for deployment

#### The appropriate solution for deploying the app
- App Service is the appropriate solution for deploying the app

#### Reasons
- The app is a lightweight web application
- It is cheaper that VM. I used the free tier to deploy (Dev/Test)
- Very high availabilty, auto-scaling and support both Linux and Window environments

### Assess app changes that would change your decision.
- Only if many more features are added or demand changes in a way that requires vertical scaling

### Project Url
- https://chuzksyarticlewebapp.azurewebsites.net/


### Monitoring and Logging
- For some reason, I can not seem to log an INFO of a successful log-in. I have configured and set it's level to INFO
- Locally it logs as INFO. I attached a screenshot in the `example_images` directory
- When deployed logs are being displayed as ERROR. I also attached a screenshot
- I also attached a screenshot of an unsuccessful log-in in the `example_images` directory