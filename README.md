# Survey results analysis

This program is a tool that presents the results of Stack Overflow Annual Developer Survey 2021. It is designed to display survey results in a clear and concise manner, while also offering cross-tabulation analysis to help users gain deeper insights into the data. Another key feature of the program is editing. It allows the user to rename column names to customize the data to meet their specific needs.

The live link to the app - [Survey results analysis](https://survey-results-analysis.herokuapp.com/)

<br> 

## Features

- __Main menu__

  - Displays a list of available program options for the user to choose from.
  - The user can select an option by entering the corresponding option number.

<br>

![Main menu](/assets/images/main-menu.jpg)

<br>

- __Survey results__

  - Prompts the user to select a section and question number to display results.
  - Displays the survey results in a clear and concise format.
  

<br>

![Options](/assets/images/menu-selection.jpg)
![Results](/assets/images/surv-res.jpg)

<br>

- __Cross-tabulation analysis__

  - Provides a tool for analyzing the relationship between two datasets.
  - Allows the user to select two datasets by entering a section and question number for each dataset.
  - Displays the results of the cross-tabulation.

<br>

![Cross-tab1](/assets/images/cross-tab-set1.jpg)
![Results](/assets/images/cross-tab-res.jpg)

<br>

- __Edit column names__

  - Enables users to rename column names to better reflect their meaning or for ease of use.
  - Prompts the user to select the desired column by entering a section and question number.
  - Offers the option to rename the selected column.

<br>

![Edit section](/assets/images/edit-col.jpg)
![Edit result](/assets/images/edit-res.jpg)

<br>

- __Exit__

  - Allows the user to exit the program.

<br>

## Data Model

The program works with the survey, which includes both text and numerical data.
The program uses survey data provided in a file called "survey-res-halved.csv". This file is in .csv format and is read into the program using the Pandas library. In order to make the data more manageable, it has been pre-processed. Specifically, the original data was too large to work with efficiently, so it has been reduced in size by selecting a sample of respondents. The resulting dataset is used for all subsequent analyses and visualizations in the program.

The survey results are organized using the Pandas DataFrame, which allows for easy manipulation and analysis of the data.
The main entities in the survey are the survey questions and the responses provided by the participants.  Each survey question has a number of attributes associated with it, including the question text, response options, and the number of respondents who selected each response. Some survey questions have a multi-answer option, which are stored in the survey data in a single column with a delimiter (";").

The user is required to enter valid input when selecting menu options or choosing a specific question to view results for.

<br>

## Testing

I have manually tested the program by:

- Passing the code through a PEP8 linter to ensure that it adheres to standard Python coding conventions. 
- Testing the program with invalid inputs, such as strings when numbers are expected or numbers that are outside the range of possible indices for a given list.
- Running the program on my local terminal and the Code Institute Heroku terminal to test the program with different inputs and scenarios.

Overall, the testing process was thorough and helped to ensure that the program works as expected.

<br>

## Unfixed Bugs

No unfixed bugs.

<br>

## Validator Testing

- PEP8
  - no errors were returned from pep8ci.herokuapp.com

<br>

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku following the steps outlined below:

 
- in Heroku account choose 'Create new app' from the 'New' menu
- in 'Settings' configure 'Config Vars', scroll down to the 'Buildpack' section and add Python and NodeJS buildpacks
- in the 'Deploy' tab select 'GitHub' to connect to your GitHub repository
- choose the repository to deploy
- scroll down the page and press 'Deploy' button
- once the web app has been successfully deployed, you will see a link to the deployed app. This link can be used to access and test the application

The live link to the app - [Survey results analysis](https://survey-results-analysis.herokuapp.com/)

<br>

## Credits

- Stack Overflow Annual Developer Survey: the full survey version can be found [here](https://insights.stackoverflow.com/survey)

- "How to Analyze Survey Data with Python for Beginners" by Charlie Custer:  the article provided a comprehensive guide on how to analyze survey data using Python. It can be found [here]( https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/)

- "Machine Learning with Python: Foundations" by Frederick Nwanganga: the online course provided valuable insights. Sections 2 through 4 covering the topics on collecting, understanding and preparing data were particularly useful. The course can be found [here](https://www.linkedin.com/learning/machine-learning-with-python-foundations/)

- Printing Lists as Tabular Data: Stack Overflow discussion provided useful tips on how to print lists as tabular data. It can be found [here](https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data)

- The deployment terminal used for this project was provided by the [Code Institute](https://codeinstitute.net)