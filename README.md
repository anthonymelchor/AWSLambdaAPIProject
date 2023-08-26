# Building AWS Lambda Functions, Layers with API Gateway and DynamoDB Integration

Welcome to the GitHub repository dedicated to AWS Lambda functions, layers, API Gateway integration, and DynamoDB usage. This project is designed to guide you through the process of creating efficient and powerful serverless applications using AWS Lambda, API Gateway, and DynamoDB.

## Key Highlights

- **Lambda Brilliance:** Learn to design and deploy Lambda functions that execute seamlessly and efficiently.
- **Layer Up:** Explore the concept of Lambda layers to manage and reuse common code across multiple functions.
- **API Gateway Awesomeness:** Dive into API Gateway to create RESTful APIs that connect your Lambda functions to the world.
- **DynamoDB Integration:** Discover how to integrate DynamoDB, a fully managed NoSQL database service, into your serverless applications.

Whether you're a seasoned developer or just starting your journey with serverless, this repository offers valuable insights and resources to elevate your AWS Lambda and DynamoDB skills. Let's jump into the world of serverless computing and build amazing applications together!

### Creating a DynamoDB Database

- Navigate to the DynamoDB service in the AWS console and create a new Table.
- Enter "tennis_player" as the table name. Use "id" for the Partition key, and choose "String" as the key type.
- Tick the "Use default settings" box, and then click on "Create."
  
![1](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/da8e9d11-0aa1-4a0e-9f4e-d41b88fed6d5)

- Head to the 'tennis_player' table, scroll down to the bottom of the Overview section, and then click on "Additional info." Note down the ARN (Amazon Resource Name), as we will require it later.

![2](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/27708763-f029-4f5f-b7ca-10bff357a62b)

### Creating an IAM Role to attach to the Lambda function

We will create a role that grants the Lambda function access to write to Amazon CloudWatch logs and write items to the DynamoDB table.

- Go to the IAM service in the AWS console and create a new Role.

- For the 'Trusted Entity Type' option, choose AWS service. For 'Use case', pick Lambda, and then click Next.

![3](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/12f58ff6-a36d-4cca-91c4-494a658ef56a)

- In the search box for Permissions policies, enter "AWSLambdaBasicExecutionRole" and check the checkbox next to this role. Click on Next Step.

![4](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/6f0967b0-edf5-42c2-b92c-fd744215b6a7)

Enter TennisPlayerLambda as the Role Name, and keep other parameters as default. Click on Create Role

![5](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/6789b77d-a3c1-4a97-ae19-7a668185b1d0)

Access the role that was recently created. Within the Permissions tab, click on "Add permissions," then choose "Create Inline Policy."

![6](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/874610c8-1dde-4f21-84f0-5f32231d9bcb)

Search for "DynamoDB" in the filter box labeled "Select a service" and then click on it.

![7](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/93a9a23e-68e2-4055-9b12-5f53d55e2dab)

Now we need to select the specific permissions for the policy. Under the access level, choose 'scan', 'GetItem', 'DeleteItem', 'UpdateItem', and 'PutItem'.

![8](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/2e58f2df-14c3-4470-b91a-c7c1578ec4ea)

![9](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/b670f908-7e49-4ec6-8f05-2ed3ac389f97)

Paste the previously copied ARN of the DynamoDB table into the field displayed below, and the remaining fields will be automatically filled. Click on Add ARNs

![11](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/4466c795-0f1b-456d-8b72-93eacff9abb2)

Name the policy "TennisPlayerDynamoDBAccess," and then click on "Create policy."

![12](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/e5b1d354-24a8-4b10-b7ba-678c5257a018)

### Creating Layer in Lamdba

This layer will include custom runtimes that can be reused across multiple functions. This helps keep functions code clean and focused on its main logic

- Navigate to the Lambda service and select the Layers option from the left menu. Then, click on Create Layer.
- Enter 'my-layer' as the layer name. Download the file [my-layer.zip](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/my-layer.zip) from this repository, and then upload it. Choose 'Python 3.11' in the Runtimes option and click on Create.

![13](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/5ef2cd8c-fcd2-4d3d-ba07-7e7c7a41875c)

### Creating Lambda Functions

We will proceed to create four Lambda functions corresponding to CRUD operations: create_player, update_player, get_player, get_players, and delete_player.

- Go to the Lambda service and select Functions. Then, click on the "Create Function" button. Choose 'Author from scratch', add 'create_player' as the name, and select Python 3.11 in the Runtime option.

![14](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/7aa59fa5-a6fb-452f-9751-4c633bff7508)

- Go to the Permissions section. There, under 'Change default execution role,' select the radio button 'Use an existing role,' and in the 'Existing role' option, choose the Role that was created earlier. Finally, click on "Create function."

![15](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/8f9385e3-f138-4627-9c39-3954a319babe)

- Enter the recently created Lambda function and replace the original Python code with this one: [create_player](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/create_player/app.py)

![16](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/cef07659-6597-4991-98ff-1629f94d8def)
  
-  Scroll down to the bottom of the Code tab and click on the "Add a layer" button. Choose the 'Custom layers' option, select the layer 'my-layer' that was created earlier along with its version, and then click on the "Add" button

![17](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/20b108cc-2f34-41a5-9ecf-3cb7e6374fe4)

- In the same way as above, we need to create four more Lambda functions:

get_player - get the code from GitHub [here](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/get_player/app.py)
get_players - get the code from GitHub [here](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/get_players/app.py)
update_player - get the code from GitHub [here](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/update_player/app.py)
delete_player - get the code from GitHub [here](https://github.com/anthonymelchor/AWSLambdaAPIProject/blob/master/delete_player/app.py)

If you follow the instructions correctly, you should see something similar to this in your AWS console:

![18](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/7bb6db01-31db-4011-a9bf-14ee2acb861e)

### Creating an API Gateway

Now, we will create an API Gateway which interacts with a Lambda function by acting as a mediator between external requests and the Lambda function's execution. When a user makes a request through the API Gateway, the Gateway receives the request and directs it to the appropriate Lambda function based on the API route or endpoint. The Lambda function then processes the request, executes its logic, and can generate a response that is sent back through the API Gateway to the user.

- Navigate to the API Gateway service and click on the "Build" button under the REST API option.

![19](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/f9f84f43-55d9-4abd-90ea-da3e2421112b)

- Choose the protocol as REST.
- Click on the "New API" option.
- Enter "TennisPlayerAPI" as the name and select "Regional" as the Endpoint Type.
- Finally, click on the button Create API.
- 
![20](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/7b18a9f5-a6ea-45f5-87ca-c5cb11a02f88)

- On the left-hand navigation menu, locate and click on "Resources."
- From the dropdown menu labeled "Actions," choose "Create Resource."
- For both the Resource Name and Resource Path, enter 'tennis-player.'
- Make sure to select the option "Enable API Gateway CORS."
- Finally, click on the "Create Resource" button.
  
![21](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/b8bf9a8e-58cb-40a7-b488-630cbbf74d76)

- Choose the 'tennis-player' resource that you previously created. From the "Action" dropdown, select "Create Method."
- A new dropdown will appear. Choose "POST" from this dropdown, and then click the checkmark.
- For the integration type, select "Lambda Function."
- Ensure you check the box for "Use Lambda Proxy integration."
- Choose the appropriate Region that you're using for Lambda.
- Enter the name of the function you previously created, which is 'create_player.'
- Click the "Save" button to confirm the settings.
- When prompted to grant Amazon API Gateway permission to invoke your function, select "OK."

![22](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/2c9ead76-0f7f-42bc-b32c-3107b5416fe4)

- Similarly to the steps outlined above, you'll need to repeat the process for the other four Lambda functions: update_player, get_player, get_players, and delete_player:

POST /tennis-player (create_player)
GET /tennis-player (get_players)
GET /tennis-player/getPlayerById (get_player)
PUT /tennis-player (update_player)
DELETE /tennis-player (delete_player)

![23](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/849abb86-6dd8-43be-a190-c6753a984c4f)

Deploying the API:

-  click on "Actions" from the Amazon API Gateway console, and then select "Deploy API." This action will prompt you to create a new stage.

- From the "Deployment stage" drop-down list, choose "[New Stage]."

- Enter "test" as the Stage Name.

- Click "Deploy" to finalize the deployment.

- Make a note of the Invoke URL that is provided. This URL will be essential for verifying the functionality of your API Gateway.

![24](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/3c08a546-8cc2-47ee-ba4e-b7088f719189)

![25](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/7834ef54-5d69-46f1-bb80-32366d1e71c0)

Validating the API Gateway:
Here, you can observe our API Gateway in action. Everything is working just as intended! :)
![27](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/47b8dbc3-566f-4cec-a065-b57c2bb549fb)

![28](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/7a021a4e-ac39-45be-937c-963869a38778)

![29](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/5a814768-c304-4307-bb5e-5b3f5d04f71f)

![26](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/d9821c61-aa55-4533-93b7-5fba08616034)

![30](https://github.com/anthonymelchor/AWSLambdaAPIProject/assets/48603061/32b10d74-a404-4581-88da-73ce87f15b53)
