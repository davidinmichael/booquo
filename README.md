```markdown
# Bookstore API and Quotes App

This project consists of two apps:

1. **Bookstore API**: An API that provides fictional book titles, prices, stock availability, and categories.

2. **Quotes App**: An app that delivers inspirational quotes.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/davidinmichael/booquo
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```shell
   python manage.py runserver
   ```

4. Access the APIs in your web browser or a tool like [Postman](https://www.postman.com/).

## Bookstore API

### Endpoints

- `/books/`: Get a list of fictional books with titles, prices, availability, and categories.

### Example Usage

- Get a list of books:
  ```
  GET /books/
  ```

## Quotes App

### Endpoints

- `/quotes/`: Get inspirational quotes.

### Example Usage

- Get a random quote:
  ```
  GET /quotes/
  ```

## Dependencies

- Python 3.x
- Django
- Django Rest Framework

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bugfix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Your message here"`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Create a pull request from your fork to the main repository.
