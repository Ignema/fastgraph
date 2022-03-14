# Welcome to FastGraph 🌩️

FastGraph is a sandbox project to experiment with a GraphQL API using FastAPI &amp; Strawberry

## Installation

First thing that we need to do is clone the repository like so:
    
    git clone https://github.com/Ignema/fastgraph.git

### Building the project from source

To run this project you'll need Python installed on your system. Make sure it's version 3.10 or above.

    // Install dependencies
    cd fastgraph
    pipenv install

    // Initialze SQLite database with Prisma
    pipenv shell
    prisma db push

    // Run the server
    uvicorn src.main:app --reload

### Running the project with a container

You can either pull the image from docker hub or build it yourself. To get the image from the cloud use the following command:

    docker pull ignema/fastgraph

To build it locally run the following command:

    docker build -t ignema/fastgraph .

Now you can run the project in either cases like so:

    docker run -d --name fastgraph -p 8080:8080 ignema/fastgraph
