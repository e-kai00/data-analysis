import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('survey-res.csv')
#df_columns = df.columns.to_list()
#print(df_columns)

"""
Show most popular programming languages, 
database enviroments, cloud platforms and
development enviroments among Stack Overflow community
"""
p_languages = df['LanguageHaveWorkedWith'].str.split(';', expand = True).stack().value_counts()
p_languages.plot(kind='bar', figsize=(15,7), color='red')
plt.title('Programming Languages')
img_p_language = plt.savefig('img_charts/p_language.png', dpi=300, bbox_inches='tight')
plt.clf()

p_languages_fut = df['LanguageWantToWorkWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', figsize=(15,7), color='red')
plt.title('Programming Languages want to work with')
img_p_language_fut = plt.savefig('img_charts/p_language_fut.png', dpi=300, bbox_inches='tight')
plt.clf()
            
data_base = df['DatabaseHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='green')
plt.title('Database Enviroments')
img_data_base = plt.savefig('img_charts/data_base.png', dpi=300, bbox_inches='tight')
plt.clf()

cloud_platform = df['PlatformHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='blue')
plt.title('Cloud Platforms')
img_cloud_platform = plt.savefig('img_charts/cloud_platform.png', dpi=300, bbox_inches='tight')
plt.clf()

dev_enviroment = df['NEWCollabToolsHaveWorkedWith'].str.split(';', expand = True).stack().value_counts().plot(kind='bar', color='yellow')
plt.title('Development Enviroments')
img_dev_enviroment = plt.savefig('img_charts/dev_enviroment.png', dpi=300, bbox_inches='tight')
plt.clf()


"""
Show from what countries most of the student developers 
use Stack Overflow
"""
country = df['Country']
students = (country[(df['MainBranch'] == 'I am a student who is learning to code')]).head(20).value_counts().plot(kind='pie')
plt.title('Students Developers')
img_students = plt.savefig('img_charts/students.png', dpi=300, bbox_inches='tight')
plt.clf()

















