import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('survey-res-halved.csv')


# Devide columns into sections
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
final_q = df[['SurveyLength', 'SurveyEase']]


def display_menu():  

    
    print('1- Survey Results\n2- Cross-tab Analysis\n3- Edit Column names')
    user_choice = input('Choose option number 1, 2 or 3:\n')

    # q = input('\nWould you like to continue?\nChoose Y or N\n')
    # if q == 'y':
    #     print('yes')
    #     qu = int(input('Would you like to go to:\n 1- Sections\n 2- Questions\n 3- Cross-tabulation analysis\n'))
    #     if qu == 1:
    #         print('sections')
    #         main()
    #     elif qu == 2:                    # to fix Qiestion option
    #         print('questions')
    #         display_questions(user_section)
    #     else:
    #         cross_tab()
    # else:
    #     print('no')
    # print('\n' *3)



def display_sections():
    """
    Display the enumerated sections, take the user's choice of a section;
    Display the enumerated questions, take the user's choice of a question;
    """
    print('\nSECTIONS:\n')
    print(' 1- Basic Information\n 2- Education, Work, and Career\n 3- Technology and Tech Culture\n 4- Stack Overflow Usage + Community\n 5- Demographic Information\n 6- Final Questions\n')
    section_number = int(input('Enter Section number:\n'))
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

    print('\nQUESTIONS:\n')
    # display the enumerated list of questions
    result = section.columns.tolist()
    for i, column in enumerate(result):
        print(f'{i+1}- {column}')

    question_num = int(input('\nEnter Question number\n'))
    # subtract 1 to get to zero-based index
    question_id = result[question_num -1] 
    
    print(f'You have chosen {question_id}')
    return question_id
    


def display_survey_results(question):
    """
    Take result from the user's input, check if 
    the question is multi- or single-answer,
    display first 15 survey results for the chosen question
    """
    
    print('\n' *3)
    print('\t\tRESULTS\n')
    if question in df.columns:
        if df[question].str.contains(';').any():
            count = df[question].str.split(';', expand = True).stack().value_counts()
        else:    
            count = df[question].value_counts()
        print(count.head(15))



def cross_tab():
    """
    Allow the user to select two datasets 
    for cross-tabulation chart
    """
     
    print('\n\t\tChoose DATASET 1\n')
    sec_group1 = display_sections()
    question_group1 = display_questions(sec_group1)

    print('\n\t\tChoose DATASET 2\n')
    sec_group2 = display_sections()
    question_group2 = display_questions(sec_group2)

    print('\n' *3)
    print('\t\tRESULTS\n')
    # display all columns of crosstab
    pd.set_option('display.max_columns', None)

    if df[question_group1].str.contains(';').any() and df[question_group2].str.contains(';').any(): # does not work as expected
        multi_q1 = df[question_group1].str.split(';', expand = True).stack().reset_index(drop=True)
        multi_q2 = df[question_group2].str.split(';', expand = True).stack().reset_index(drop=True)
        multi_multi = pd.crosstab(multi_q1, multi_q2)        
        print(multi_multi)
     
    elif df[question_group1].str.contains(';').any():     
        multi_q = df[question_group1].str.split(';', expand = True).stack().reset_index(drop=True)        
        multi_single = pd.crosstab(multi_q, df[question_group2])           
        print(multi_single)

    elif df[question_group2].str.contains(';').any():   
        multi_qu = df[question_group2].str.split(';', expand = True).stack().reset_index(drop=True)        
        single_multi = pd.crosstab(df[question_group1], multi_qu)
        print(single_multi)

    else: 
        single = pd.crosstab(df[question_group1], df[question_group2]) 
        print(single)

    display_menu()



def change_column_name(df, old_name):    
    
    new_name = input(f'Enter new column name for {old_name}')
    df.rename(columns={old_name: new_name}, inplace=True)
    print(df.columns)
    # return df.columns  



# def main():
    
#     user_section = display_sections()
#     user_question = display_questions(user_section)
#     display_survey_results(user_question)
#     display_menu()
    

# main()
print('2021 Stack Overflow Developer Survey')
display_menu()





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














