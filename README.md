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

### Creating Lambda functions







