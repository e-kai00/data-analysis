import pandas as pd
from tabulate import tabulate


df = pd.read_csv('survey-res-halved.csv')


# Devide DataFrame columns into sections
basic_info = df[['MainBranch', 'Employment', 'Country']]
ed_work = df[[
    'YearsCodePro',
    'DevType',
    'OrgSize',
    'Currency',
    'CompTotal',
    'CompFreq'
]]

tech_culture = df[[
    'LanguageHaveWorkedWith',
    'LanguageWantToWorkWith',
    'DatabaseHaveWorkedWith',
    'DatabaseWantToWorkWith',
    'PlatformHaveWorkedWith',
    'PlatformWantToWorkWith',
    'WebframeHaveWorkedWith',
    'WebframeWantToWorkWith',
    'MiscTechHaveWorkedWith',
    'MiscTechWantToWorkWith',
    'ToolsTechHaveWorkedWith',
    'ToolsTechWantToWorkWith',
    'NEWCollabToolsHaveWorkedWith',
    'NEWCollabToolsWantToWorkWith',
    'OpSys',
    'NEWStuck'
]]

community = df[[
    'NEWSOSites',
    'SOVisitFreq',
    'SOAccount',
    'SOPartFreq',
    'SOComm',
    'NEWOtherComms'
]]

demograph = df[[
    'Age',
    'Gender',
    'Trans',
    'Sexuality',
    'Ethnicity',
    'Accessibility',
    'MentalHealth'
]]

final_q = df[['SurveyLength', 'SurveyEase']]


def display_menu():
    """
    Display the menu of available program options for the user.

    Uses the 'tabulate' library to display menu options: survey
    results, cross-tab analysis, edit columns and exit the program.
    Prompts the user to select an option by entering a number 1 through 4
    and validates the input to ensure that it's integer between 1 and 4.

    Returns:
        int: the user's validated choice of menu option
    """

    list_length = range(1, 5)

    print('\n' * 2)
    print('\t\tMENU')
    print(tabulate([
        ['1- ', 'Survey Results'],
        ['2- ', 'Cross-tabulation Analysis'],
        ['3- ', 'Edit Column Names'],
        ['4- ', 'Exit']
    ]))
    user_choice = validate_input(list_length)

    if user_choice == 1:
        main()

    elif user_choice == 2:
        cross_tab()

    elif user_choice == 3:
        print('\nTo edit a column, specify its section and question number')
        user_section = display_sections()
        user_question = display_questions(user_section)
        change_column_name(df, user_question)

    else:
        print('You have exited the program.')
        exit()


def validate_input(lists):
    """
    Prompts the user to enter a number, validates that it is a valid
    integer and within the range of possible indices for the given
    list, returns the input. If the input is invalid, the
    function prompts the user until the valid input is received.

    Parameters:
        list: a list of any data type. Used to set the range of indices
        of the given list.
    Returns:
        int: the validated input from the user.
    Raises:
        ValueError: if input values cannot be converted into an integer
        UnboundLocalError: if input values are outside of the range of possible
        indices for the given list.
    """

    max_value = len(lists)
    print('\nTo select an option, enter the corresponding number')

    while True:
        try:
            input_box = int(input('\nEnter a number:\n'))
            if input_box > max_value or input_box == 0:
                raise UnboundLocalError
            break

        except ValueError:
            print('Invalid data! Please enter a number.')
        except UnboundLocalError:
            print('The number is out of range. Try again!')

    return input_box


def display_sections():
    """
    Display the enumerated sections.

    Displays all survey sections. Prompts the user to select
    an option by entering a number 1 through 6 and validates
    the input to ensure that it is an integer between 1 and 6.

    Returns:
        int: the user's validated choice of section number.
    """

    list_length = range(1, 7)

    print('\nSECTIONS:\n')
    print(' 1- Basic Information\n 2- Education, Work, and Career \
            \n 3- Technology and Tech Culture \
            \n 4- Stack Overflow Usage + Community \
            \n 5- Demographic Information\n 6- Final Questions')
    section_number = validate_input(list_length)

    if section_number == 1:
        choice = basic_info

    elif section_number == 2:
        choice = ed_work

    elif section_number == 3:
        choice = tech_culture

    elif section_number == 4:
        choice = community

    elif section_number == 5:
        choice = demograph

    elif section_number == 6:
        choice = final_q

    return choice


def display_questions(section):
    """
    Display the enumerated list of section's questions.

    Displays all questions of the chosen section. Prompts the user
    to select a question by entering a number of the question and
    validates the input to ensure that it is an integer within the allowed
    range. Assigns the chosen integer to the column name of the DataFrame.

    Parameters:
        section (int): validated section number.
    Returns:
        question_id (str): the user's choice of question as a column name
        of the DataFrame.
    """

    print('\nQUESTIONS:\n')
    # display the enumerated list of questions
    result = section.columns.tolist()
    for i, column in enumerate(result):
        print(f'{i+1}- {column}')

    question_num = validate_input(result)

    # subtract 1 to get to zero-based index
    question_id = result[question_num - 1]

    print(f'You have chosen {question_id}')
    return question_id


def display_survey_results(question):
    """
    Display results of the chosen question.

    Displays first 15 survey results for the chosen question.
    Check if the chosen question is multi- or single-answer type.
    If the question is the multi-answer type, the function splits
    the answers and then display results.

    Parameters:
        question (str): DataFrame column name.
    """

    print('\n' * 3)
    print('\t\tRESULTS\n')
    if question in df.columns:
        if df[question].str.contains(';').any():
            count = (
                df[question]
                .str.split(';', expand=True)
                .stack()
                .value_counts()
            )
        else:
            count = df[question].value_counts()
        print(count.head(15))


def cross_tab():
    """
    Allow the user to select two datasets for cross-tabulation.

    Displays options to choose - section number and question number
    for dataset 1 and dataset 2. Check if the chosen datasets contain
    multi- or single-answer questions. Displays cross-tabulation
    results. Displays the main menu.
    """

    print('\nChoose 2 datasets to analyse:\n')
    print('\t\tChoose DATASET 1')
    sec_group1 = display_sections()
    question_group1 = display_questions(sec_group1)
    print('\n' * 2)
    print('\t\tChoose DATASET 2')
    sec_group2 = display_sections()
    question_group2 = display_questions(sec_group2)

    print('\n' * 3)
    print('\t\tRESULTS\n')
    # display 10 columns of the cross-tab
    pd.set_option('display.max_columns', 10)

    if (
        df[question_group1].str.contains(';').any()
        and df[question_group2].str.contains(';').any()
    ):
        multi_q1 = (
            df[question_group1]
            .str.split(';', expand=True)
            .stack().reset_index(drop=True)
        )
        multi_q2 = (
            df[question_group2]
            .str.split(';', expand=True)
            .stack().reset_index(drop=True)
        )
        multi_multi = pd.crosstab(multi_q1, multi_q2)
        print(multi_multi)

    elif df[question_group1].str.contains(';').any():
        multi_q = (
            df[question_group1]
            .str.split(';', expand=True)
            .stack().reset_index(drop=True)
        )
        multi_single = pd.crosstab(multi_q, df[question_group2])
        print(multi_single)

    elif df[question_group2].str.contains(';').any():
        multi_qu = (
            df[question_group2]
            .str.split(';', expand=True).stack()
            .reset_index(drop=True)
        )
        single_multi = pd.crosstab(df[question_group1], multi_qu)
        print(single_multi)

    else:
        single = pd.crosstab(df[question_group1], df[question_group2])
        print(single)

    display_menu()


def change_column_name(df, old_name):
    """
    Allow the user to edit or rename DataFrame columns.

    Prompts the user to enter a new name for the specified DataFrame column.
    Renames the column using rename() pandas method.
    Uses the 'tabulate' library to display the updated list of all DataFrame
    columns. Displays the main menu.

    Parameters:
        df (pd.DataFrame): the DataFrame to modify.
        old_name (str): the name of the column to be modified.
    """
    print('\n')
    new_name = input(f'Enter new column name for {old_name}:\n')
    df.rename(columns={old_name: new_name}, inplace=True)

    cols = [[col] for col in df.columns]
    print(tabulate(cols, headers=['Columns'], tablefmt='grid'))

    display_menu()


def main():
    """
    Run all program functions.
    """
    user_section = display_sections()
    user_question = display_questions(user_section)
    display_survey_results(user_question)
    display_menu()


print('\n\t\t2021 Stack Overflow Developer Survey')
display_menu()
