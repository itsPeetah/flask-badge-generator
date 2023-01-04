# Badge Generator Flask

Small web app to generate a badge with a name on it using a GET HTTP request.
This is an extremely WIP prototype, I just needed something to do the job quickly.

## Usage

- Of course, install the required modules with `pip`
- Execute `flask --app main run`
- Navigate or do a GET request to the home (`/?`) route and a `text` query parameter
  - e.g. "http://127.0.0.1:5000?text=hello%20world
