# Weather API Service

A simple weather API service using FastAPI that fetches weather data from an external public API. The service uses asynchronous programming to handle high traffic and interacts with local equivalents of AWS S3 and DynamoDB for storing and caching data.

## Features

- Fetch weather data asynchronously from an external API
- Store weather data as JSON files in a local directory
- Log events in a local SQLite database
- Cache weather data to reduce API calls
- Deployable using Docker

## Requirements

- Docker
- Docker Compose

## Setup Instructions

### Running Locally with Docker

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

3. The FastAPI app will be available at `http://localhost:8000`.

### API Endpoint

- `GET /weather?city={city}`
    - Fetches weather data for the specified city.
    - Example:
        ```
        GET /weather?city=London
        ```

## Directory Structure

## License

This project is licensed under the MIT License.

## Author
- Enkhbat E
