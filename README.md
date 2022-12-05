# Ireland's population Census Survey

Census survey is a data analytics program that runs on Heroku's mock Terminal.

Users can retrieve population data from the survey for the years 2011 to 2016, they can filter by either year(2011 or 2016 or both), gender, age, and region.
The program also has the feature of exporting the user's choices into a file.

Developed by Martin Fortuna.

![Am I Responsive Website Mockup](/readme/census-mock-up.png)


## Project Goals

I wanted to create an easy-to-manipulate program with data from Census, usable both to satisfy private users' curiosity and companies' marketing departments.
The data pulled can also be saved into a file for further analysis.

## Features

### Existing Features

- Welcome screen

The user is greeted with a description of the purpose of the program, he is given the option to analyze the survey data. 

![Welcome screen](/readme/welcome.png)


- User options

The user can select filters on year, gender, age, and region data.

![User options](/readme/options.png)

- Input validation and error checking

The user has to choose from the options of numbers given, he cannot enter an empty input.

![Input validation](/readme/validation.png)

- Rendered data 

The program prints the requested data

![Rendered data](/readme/data-rendered.png)

- File export option

The user is given the option of exporting the requested data.

![Rendered data](/readme/file-export.png)

### Future Features

- Allow users to select a wider range of years.
- Add all previous and future surveys for Ireland.
- Add data for other countries.

## Data Model

I decided to use a flat CSV file with a single table and use queries to filter and get only the relevant columns.
The queries are then used to get and render data back to the user.

## Testing

I have manually tested this project by doing the following:

- As the PEP8 linter is down I have used its replacement provided by Code Institute by downloading it to my IDE, and no validation errors were found.
- Given invalid inputs such as out-of-bounds inputs, non-integers, and strings when numbers are expected.
- I tested in my IDE local terminal and the Heroku terminal.

### Bugs

No known bugs were found and remain unsolved.

### Validator Testing

- PEP8

No errors are returned from the installed version of PEP8 in my IDE.

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
- Fork or clone this repository
- Create a new Heroku app
- Set the buildbacks to Python and NodeJS in the order
- Link the Heroku app to the repository
- Click on Deploy

## Credits

- To Census Ireland for providing the data source 
[Census Ireland](https://data.gov.ie/dataset/e2022-population-2011-to-2016/resource/ff12fd4b-63a7-48e3-9c8b-a8f309f78cfa)

## Acknowledgements

- To my friends Guillerme and Juliana for helping me with the project.