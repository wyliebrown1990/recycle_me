### README.md Content:

```markdown
# Flask Recycling App

This is a Flask web application designed to help users check whether items are recyclable in their location based on provided data. The application utilizes Python, Flask, and FuzzyWuzzy for matching user inputs against a dataset of recyclable materials.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker is installed on your system (For Docker installation, visit [Docker's website](https://www.docker.com/get-started))

## Project Structure

```
/your-flask-app
    /templates
        - form.html
        - response.html
    /static
        - styles.css
    app.py
    requirements.txt
    Dockerfile
    README.md
```

## Setup

To set up the Flask application, follow these steps:

1. Clone the repository or download the source code to your local machine.
2. Navigate to the project directory where the Dockerfile is located.

## Building the Docker Image

Run the following command to build the Docker image:

```bash
docker build -t flask-recycling-app .
```

This command builds a Docker image named `flask-recycling-app` based on the instructions in the `Dockerfile`.

## Running the Application

To run the application, use the following command:

```bash
docker run -p 5000:5000 flask-recycling-app
```

This command starts a Docker container running the Flask application, mapping port 5000 of the container to port 5000 on your host machine.

## Accessing the Application

Open a web browser and navigate to `http://localhost:5000` to use the application.

## Contributing to the Application

To contribute to the Flask Recycling App, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact me you can reach me at `<wyliebrown1991@gmail.com>`.

## License

This project uses no licensing.
```