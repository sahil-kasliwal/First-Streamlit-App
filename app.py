import streamlit as st
from datetime import datetime

# # Title
# st.title('Title GFG')

# # Header
# st.header("Header")

# # Sub Header
# st.subheader('Sub Header')

# # Text
# st.text('Text')


# # Markdown
# st.markdown('This is a list of tags (markdown) - paragraph tag')
# st.markdown(' # This is a markdown text - h1 tag')
# st.markdown(' ## This is a markdown text - h2 tag')
# st.markdown(' ### This is a markdown text - h3 tag')
# st.markdown(' #### This is a markdown text -  h4 tag')
# st.markdown(' ##### This is a markdown text -  h5 tag')
# st.markdown(' ###### This is a markdown text -  h6 tag')

# st.markdown('**GFG** Data Science - Bold')
# st.markdown('__GFG__ Data Science - Bold')

# st.markdown('*GFG* Data Science - Italic')
# st.markdown('_GFG_ Data Science - Italic')

# st.markdown('***GFG*** Data Science -BOLD +  Italic')
# st.markdown('___GFG___ Data Science - BOLD + Italic')


# st.markdown('1. First Point')
# st.markdown('- Second Point')
# st.markdown('* Second Point')

# st.write('This is a write function')

# st.write(range(1,10) , 'This will print the code write function')


# st.subheader('1. Text Input')
# name = st.text_input('Enter your name: ',value = 'Sahil Kasliwal')
# st.write('Hello', name)

# st.subheader('2. Password Input')
# password = st.text_input('Enter your passowrd: ',type = 'password',help = 'Atleast have 8 characters')


# st.subheader('3. Text Area')
# st.text_area('Tell me about yourself in 200 words: ',height = 200,max_chars = 500,help = 'Maximum 500 characters allowed ')

# st.subheader('4. Numeric Input')
# st.number_input('Enter your age: ',min_value = 0,max_value = 105,step = 1,value = 22)

# st.subheader('5. Date')
# today = datetime.now().date()

# date = st.date_input('Enter the date: ',value = today ,min_value = today,max_value = today.replace(year = today.year +1))
# st.write("You've selected: ",datetime.strftime(date,'%m/%d/%y'))


# st.subheader('1. Radio Button')
# gender = st.radio('Selct your gender: ',options = ('Male','Female','Other(Chakke)'),help = 'Choose 1 ',horizontal = True)

# st.write("You've selected :",gender)

# st.subheader('2. Select box')
# option = st.selectbox('Select your options: ',options = ('Data Analytics', 'Machine Learning', 'Deep Learning', 'Artifical Intelligence'),help ='Choose one')

# st.write("You've selected :",option)

# st.subheader('3. MultiSelect box')
# options = st.multiselect('Select your options: ',options = ('Data Analytics', 'Machine Learning', 'Deep Learning', 'Artifical Intelligence'),help ='Choose one',default = 'Data Analytics')

# st.subheader('4. Button')
# if st.button('Click this . I have a surprise for you!'):
#     st.write('Hutt Badwe')


# st.subheader('5. CheckBox')

# if st.checkbox('I agree to the terms and conditions. ',help = 'You must agree to proceed'):
#     st.write('Thank you , ab nikal lawde')

# st.subheader('6. Color Picker')

# color = st.color_picker('Selct your favourite color','#3649A2')
# st.write("You've selected :",color)

# st.button('Submit Your Response')
# 



# def rate_yourself():
#     with st.sidebar:
#         st.title('Rate Yourself')
#         languages = st.text_input('Enter the programming languages you know with comma separation', value='Python')
#         languages = [i.strip() for i in languages.split(',')]

#     st.subheader('How would you rate your experience in the following programming languages & tools?')

#     for language in languages:
#         st.write(language)
#         st.slider(language, min_value=0., max_value=10., step=0.5)

# def bmi_calc():
#     st.title("BMI Calculator:")

#     with st.form(key='BMI Calculator', clear_on_submit=False):
#         col1, col2, col3 = st.columns([3, 2, 1])

#         with col1:
#             weight = st.number_input("Enter your weight in KGS")

#         with col2:
#             height = st.number_input("Enter your height in mtrs")

#         with col3:
#             submit = st.form_submit_button(label='Calculate')

#     if submit:
#         BMI = round((weight / height**2), 2)
#         if BMI <= 18.5:
#             st.error("Underweight")
#         elif 18.5 < BMI <= 24.9:
#             st.success("Healthy/ Normal BMI")
#         elif 25 <= BMI <= 29.9:
#             st.warning("Overweight")
#         elif BMI >= 30.0:
#             st.error("OBESE")

# ch = st.sidebar.selectbox("Menu", ['BMI', 'Rate Yourself'])

# if ch == 'BMI':
#     bmi_calc()
# elif ch == 'Rate Yourself':
#     rate_yourself()

# import streamlit as st
# import numpy as np
# import time

# col1,col2,col3 = st.columns(3)

# with col1:
#     st.header('Cat')
#     st.image('https://static.streamlit.io/examples/cat.jpg',width = 200)

# with col2:
#     st.header('Dog')
#     st.image('https://static.streamlit.io/examples/dog.jpg')

# with col3:
#     st.header('Owl')
#     st.image('https://static.streamlit.io/examples/owl.jpg')


# n = st.number_input('How many columns do you want?: ', 1,10)
# cols = st.columns(n)

# for i in cols:
#     with i:
#         st.image('https://static.streamlit.io/examples/dog.jpg')


# import time
# import numpy as np
# import pandas as pd
# import streamlit as st

# # Static
# tab1, tab2 , tab3 = st.tabs(['Cat', 'Dog','Owl'])
# tab1.image('https://static.streamlit.io/examples/cat.jpg', width = 200)
# tab2.image('https://static.streamlit.io/examples/dog.jpg', width = 200)
# tab3.image('https://static.streamlit.io/examples/owl.jpg', width = 200)

# # Dynamic

# imgs = pd.read_csv('/Users/sahilkasliwal/Desktop/Streamlit/imgs.csv')['img_link']
# tags = pd.read_csv('/Users/sahilkasliwal/Desktop/Streamlit/imgs.csv')['tags']

# tabs = st.tabs(["ID"]*30)
# for tab in tabs:
#     random_num = np.random.randint(1,1000)
#     img = imgs[random_num]
#     tag = tags[random_num]
#     tab.image(img, width = 800)
#     tab.write(tag)

# import time
# import numpy as np
# import pandas as pd
# import streamlit as st

# st.set_page_config(page_title = 'GeeksForGeeks')#,layout = 'wide'),page_icon = '')

# cases = []
# for _ in range(36):
#     cases.append(np.random.randint(1, 7))

# data = []
# for i in range(1, 7):
#     data.append(cases.count(i))

# st.header('Frequency of getting a Face')
# st.bar_chart({'data': data})

# with st.expander('See Explanation'):
#     st.write('''
#             Then chart above shows the numbers that I got on rolling the dice 100 times.
#             The number of values that occurs
#              ''')
#     st.image('https://static.streamlit.io/examples/dice.jpg')

# # with st.empty():

# #     for i in range(11):
# #         st.write('⏳ ' + str(i) + ' remaining')
# #         time.sleep(1)
# #     st.write('10 seconds completed')


# with st.spinner('Wait for it'):
#     time.sleep(5)
#     st.write('Thanks for being patient')

# with st.empty():
#     for percentage_completed in range(100):
#         time.sleep(.1)
#         st.progress(percentage_completed+1,text= 'Processing')
#     st.success('Congratualations!')

# st.balloons()
# st.snow()


# import time
# import numpy as np
# import pandas as pd
# import streamlit as st

# st.write('This is code inside write statement')

# st.code("st.write('This is code inside write statement')")


# def get_username():
#     return 'Sahil'



# with st.echo():
#     #st.write('This is code inside write statement')
#     def get_punc():
#         return '!'
    
#     greeting = 'Hi!, there'
#     name = get_username()
#     punc = get_punc()

#     st.write(greeting,name,punc)
    

# fist_name = st.text_input('Enter your first name: ')
# if not fist_name:
#     st.warning('Please enter your name.')
#     st.stop()
# # st.success('Thanks!')

# last_name = st.text_input('Enter your last name: ')
# if not last_name:
#     st.warning('Please enter your name.')
#     st.stop()
# st.success('Thanks!')


# import time
# import numpy as np
# import pandas as pd
# import streamlit as st
# from PIL import Image

# st.title('1. Image from Path')
# img = Image.open('/Users/sahilkasliwal/Desktop/Streamlit/Sahil.jpeg')
# st.image(img,width = 200)

# st.title('2. Image from Link')
# st.image('https://stimg.cardekho.com/images/carexteriorimages/930x620/BMW/M4-Competition/10580/1689672224717/front-left-side-47.jpg',width = 250)


# st.title('3. Video')
# video_file = open('/Users/sahilkasliwal/Desktop/Streamlit/IMG_1757.MOV','rb')
# st.video(video_file, start_time=5)

# st.title('4. Audio')
# audio_file = ''
# st.audio(audio_file.read())




# import pandas as pd
# import streamlit as st



# df = pd.read_csv('/Users/sahilkasliwal/Desktop/Streamlit/abalone.csv')

# st.subheader('Displaying whole the DataFrame')
# st.dataframe(df)

# st.subheader('Displaying the head of DataFrame')
# st.dataframe(df.head())

# st.subheader('Displaying the head of DataFrame')
# st.dataframe(df.tail())

# st.subheader('Displaying the DataFrame as Table(20rows)')
# st.table(df.head(20))


# import pandas as pd
# import streamlit as st
# from PIL import Image

# st.title('File Uploading')

# 1. Image
st.subheader('1. Uploading an Image')
img_file = st.file_uploader('Upload Image', type = ['png','jpeg','jpg'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))

# 2. Audio
st.subheader('2. Uploading an Audio')
img_file = st.file_uploader('Upload Image', type = ['wav','mp3'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(img_file)
    st.audio(img_file)

# 3. Video
st.subheader('2. Uploading an Video')
img_file = st.file_uploader('Upload Video', type = ['mov','mp4'])
if img_file is not None:
    file_details = {'file_name' : img_file.name, 'file_type' : img_file.type,
                    'file_size' : img_file.size}
    st.write(img_file)
    st.video(img_file)



# import streamlit as st
# from PIL import Image

# def convert_image(image_path, new_format):
#     with Image.open(image_path) as img:

#         new_name = image_path.name.split('.')[0] + '.' + new_format
#         final_path = '/Users/ashishzangra/Documents/Streamlit/' + new_name

#         img = img.convert('RGB')

#         st.subheader(final_path)
#         img.save(final_path)
#         st.success('Image Saved at ' + final_path)


# st.title('Image Converter')
# image_path = st.file_uploader('Upload your image', type = ['png','jpg','jpeg'])

# new_format = st.selectbox('Select the output format', ['png','jpeg','jpg'])

# if st.button('Convert'):
#     if image_path is not None:
#         convert_image(image_path, new_format)
#     else:
#         st.error('Please uplaod the image file')



# import numpy as np
# import pandas as pd
# import streamlit as st

# st.subheader('1. Line Chart')
# chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['L1','L2','L3'])
# st.line_chart(chart_data)

# st.subheader('2. Area Chart')
# chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['L1','L2','L3'])
# st.area_chart(chart_data)

# st.subheader('3. Bar Chart')
# chart_data = pd.DataFrame(np.random.randn(20,2),columns = ['L1','L2'])
# st.bar_chart(chart_data)


# import numpy as np
# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.title('Data Visualization with Seaborn and Matplotlib')

# st.text('1. Displaying the Dataset')
# df = pd.read_csv('iris.csv')

# st.dataframe(df)

# st.text('1. BarPlot using Matplotlib')

# fig = plt.figure(figsize=(15,8))
# df['Species'].value_counts().plot(kind = 'bar')
# st.pyplot(fig)

# st.text('2. PieChart using Matplotlib')
# fig = plt.figure(figsize=(15,8))
# df['Species'].value_counts().plot(kind = 'pie')
# st.pyplot(fig)

# st.text('3. Distplot using Seaborn')
# fig = plt.figure(figsize=(15,8))
# sns.distplot( df['SepalLengthCm'])
# st.pyplot(fig)

# st.text('4. Displat Multiple Graph')

# col1,col2 = st.columns(2)

# with col1:
#     col1.write('KDE = False')
#     fig1 = plt.figure()
#     sns.displot(df['SepalLengthCm'],kde = False)
#     st.pyplot(fig1)

# with col2:
#     col1.write('KDE = False')
#     fig2 = plt.figure()
#     sns.set_style('darkgrid')
#     sns.displot(df['SepalLengthCm'])
#     st.pyplot(fig2)


# st.text('5. Scatter Plot')
# fig,ax = plt.subplots(figsize = (15,8))
# ax.scatter(*np.random.random(size = (2,100)))
# st.pyplot(fig)

# st.text('6. Count Plot')
# fig = plt.figure(figsize=(15,8))
# sns.countplot(data = df,x = 'Species')
# st.pyplot(fig)


# st.text('6. Box Plot')
# fig = plt.figure(figsize=(15,8))
# sns.boxplot(x = 'Species',y = 'PetalLengthCm',data = df)
# st.pyplot(fig)



# st.text('6. Violin Plot')
# fig = plt.figure(figsize=(15,8))
# sns.violinplot(x = 'Species',y = 'PetalLengthCm',data = df)
# st.pyplot(fig)

# import numpy as np
# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt
# import seaborn as sns

# import plotly.express as px
# import plotly.figure_factory as ff


# st.title('Data Visualization with Plotly')

# st.text('1. Displaying the Dataset')
# df = pd.read_csv('tips.csv')

# st.dataframe(df)

# st.text('1. Pie Chart')
# fig = px.pie(df,values = 'total_bill',names = 'day')
# st.plotly_chart(fig)

# st.text('2. Pie Chart with a hole')
# fig = px.pie(df,values = 'total_bill',names = 'day',opacity = 0.7,hole = .5)
# st.plotly_chart(fig)










