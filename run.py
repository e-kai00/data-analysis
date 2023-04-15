import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('survey-res-halved.csv')
df_columns = df.columns.to_list()
#print(df.columns)


"""
To count all answers in survey
"""
# for column in df.columns:   
#     print(column)
#     print(df[column].value_counts())


"""
Sections
"""
basic_info = df[['MainBranch', 'Employment', 'Country']]
ed_work = df[['YearsCodePro', 'DevType', 'OrgSize', 'Currency', 'CompTotal',
       'CompFreq']]
tech_culture = df[['LanguageHaveWorkedWith', 'LanguageWantToWorkWith',
       'DatabaseHaveWorkedWith', 'DatabaseWantToWorkWith',
       'PlatformHaveWorkedWith', 'PlatformWantToWorkWith',
       'WebframeHaveWorkedWith', 'WebframeWantToWorkWith',
       'MiscTechHaveWorkedWith', 'MiscTechWantToWorkWith',
       'ToolsTechHaveWorkedWith', 'ToolsTechWantToWorkWith',
       'NEWCollabToolsHaveWorkedWith', 'NEWCollabToolsWantToWorkWith', 'OpSys',
       'NEWStuck']]
community = df[['NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq', 'SOComm', 'NEWOtherComms']]
demograph = df[['Age', 'Gender', 'Trans', 'Sexuality',
       'Ethnicity', 'Accessibility', 'MentalHealth']]
final_q = df[['SurveyLength', 'SurveyEase', 'ConvertedCompYearly']]


def display_sections():
    """
    Display the enumerated sections, take the user's choice of a section;
    Display the enumerated questions, take the user's choice of a question;
    """
    print('Choose section you want to explore\n')
    print(' 1- Basic Information\n 2- Education, Work, and Career\n 3- Technology and Tech Culture\n 4- Stack Overflow Usage + Community\n 5- Demographic Information\n 6- Final Questions\n')
    section_number = int(input('Enter number of section:\n'))
    if section_number == 1:
        choice = basic_info
        print('Section 1')
    elif section_number == 2:
        choice = ed_work
        print('Section 2')
    elif section_number == 3:
        choice = tech_culture
        print('Section 3')
    elif section_number == 4:
        choice = community
        print('Section 4')
    elif section_number == 5:
        choice = demograph
        print('Section 5')
    elif section_number == 6:
        choice = final_q
        print('Section 6')
    
    return choice


def display_questions(section):

    # display an enumerated list of questions
    result = section.columns.tolist()
    for i, column in enumerate(result):
        print(f'{i+1}- {column}')

    question_num = int(input('Enter question number to see survey results\n'))
    # subtract 1 to get to zero-based index
    question_id = result[question_num -1] 
    
    return question_id
    


def display_survey_results(question):
    """
    Take result from the user's input, check if 
    the question is multi- or single-answer,
    display survey results for the chosen question
    """
    
    if question in df.columns:
        if df[question].str.contains(';').any():
            count = df[question].str.split(';', expand = True).stack().value_counts()
        else:    
            count = df[question].value_counts()
        print(count.head(15))
      

def back_to_selection():  # to finish later

    
    q = input('\nWould you like to continue?\nChoose Y or N\n')
    if q == 'y':
        print('yes')
        qu = input('Would you like to go back to Questions or Sections\nChoose Q or S\n')
        if qu == 'q':
            print('questions')
            display_questions(user_section)
        else:
            print('sections')
            display_sections()
    else:
        print('no')

#pd.set_option('display.max_columns', None)    # display all columns of crosstab

test_single = pd.crosstab(df['Age'], df['MainBranch'])  
# print(test_single)

lang = df['DatabaseHaveWorkedWith'].str.split(';', expand = True).stack().reset_index(drop=True)
tets_single_multi = pd.crosstab(df['Age'], lang)
# print(tets_single_multi)



# user_section = display_sections()
# user_question = display_questions(user_section)
# display_survey_results(user_question)
# back_to_selection()








# """
# Show most popular programming languages, 
# database enviroments, cloud platforms and
# development enviroments among Stack Overflow community
# """
# p_languages = df['LanguageHaveWorkedWith'].str.split(';', expand = True).stack().value_counts()
# p_languages.plot(kind='bar', figsize=(15,7), color='red')
# plt.title('Programming Languages')
# img_p_language = plt.savefig('img_charts/p_language.png', dpi=300, bbox_inches='tight')
# plt.clf()

# p_languages_fut = df['LanguageWantToWorkWith'].str.split(';', expand = True).stack().head(7).value_counts().plot(kind='pie')
# plt.title('Programming Languages want to work with')
# img_p_language_fut = plt.savefig('img_charts/p_language_fut.png', dpi=300, bbox_inches='tight')
# plt.clf()
            
# data_base = df['DatabaseHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='green')
# plt.title('Database Enviroments')
# img_data_base = plt.savefig('img_charts/data_base.png', dpi=300, bbox_inches='tight')
# plt.clf()

# cloud_platform = df['PlatformHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='blue')
# plt.title('Cloud Platforms')
# img_cloud_platform = plt.savefig('img_charts/cloud_platform.png', dpi=300, bbox_inches='tight')
# plt.clf()

# dev_enviroment = df['NEWCollabToolsHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='yellow')
# plt.title('Development Enviroments')
# img_dev_enviroment = plt.savefig('img_charts/dev_enviroment.png', dpi=300, bbox_inches='tight')
# plt.clf()

# problem_stuck = df['NEWStuck'].str.split(';', expand = True).stack().value_counts().plot(kind='pie')
# plt.title('Title')
# img_problem_stuck = plt.savefig('img_charts/problem_stuck.png', dpi=300, bbox_inches='tight')
# plt.clf()


# """
# Show from which countries most of the student developers 
# on StackOverflow
# """

# students = df[df['MainBranch'] == 'I am a student who is learning to code']
# country = students['Country'].head(15).value_counts().plot(kind='pie')
# plt.title('Students from different countries')
# img_students = plt.savefig('img_charts/students.png', dpi=300, bbox_inches='tight')
# plt.clf()

# """
# Show which age group code primarily as a hobby
# """

# hobby_coders = df[df['MainBranch'] == 'I code primarily as a hobby']
# age_hobby = hobby_coders['Age'].value_counts()
# age_hobby.plot(kind='bar', xlabel='Age group', ylabel='Number of people coding as a hobby')
# plt.title('Hobby Coders')
# img_age_hobby = plt.savefig('img_charts/age_hobby.png', dpi=300, bbox_inches='tight')
# plt.clf()


# for i in df['DevType'].unique():
#     print(df['DevType'][i])














