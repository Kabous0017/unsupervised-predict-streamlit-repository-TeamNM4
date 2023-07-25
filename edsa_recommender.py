"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
import base64
from pathlib import Path


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid' style='border-radius: 50%; width: 80%'>".format(
      img_to_bytes(img_path)
    )
    return img_html

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","About Us","App Feedback","Analytics"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    if page_selection == "About Us":
        st.image('resources/imgs/2.png')
        st.write('''
Welcome to The ReelDeal, your ultimate destination for personalized movie recommendations! We are a cutting-edge technology company dedicated to revolutionizing the way you discover and enjoy movies. Our team of experts is passionate about film and committed to helping you find your next cinematic gem.

At The ReelDeal, we understand that the world of movies can be overwhelming. With thousands of films released each year across various genres and platforms, it can be challenging to navigate through the vast sea of choices. That's where we come in. We have developed state-of-the-art custom movie recommender systems that take into account your unique tastes, preferences, and viewing history to deliver highly tailored recommendations just for you.

Our sophisticated algorithms analyze an extensive database of movies, considering factors such as genre, director, actors, plot elements, and user reviews. By understanding your individual cinematic preferences and patterns, we curate a selection of films that align with your interests, ensuring that every movie you watch is a perfect match.

So, why settle for generic movie suggestions when you can have a tailored cinematic experience with The ReelDeal? Join our community of movie enthusiasts today and unlock a world of captivating stories, unforgettable characters, and boundless entertainment. Let us be your trusted companion in the realm of movies, guiding you towards the films that will truly speak to you. Get ready to discover, be inspired, and embark on a thrilling reel journey with The ReelDeal!''')
        
        st.header('Our Creative Team')
        col_team_1, col_team_2, col_team_3,col_team_4, col_team_5 = st.columns([0.125,0.25,0.25,0.25,0.125])
        with col_team_2:
            st.markdown(img_to_html('resources/imgs/Kobus.jpg'), unsafe_allow_html=True)
            st.write('**Kobus Le Roux**')
            st.write('Chairman')
        with col_team_3:
            st.markdown(img_to_html('resources/imgs/Tebogo.jpg'), unsafe_allow_html=True)
            st.write('**Tebogo Khoza**')
            st.write('Junior Developer')
        with col_team_4:
            st.markdown(img_to_html('resources/imgs/Devon.jpg'), unsafe_allow_html=True)
            st.write('**Devon Woodman**')
            st.write('Technical Director')
        
        col_team_4, col_team_5, col_team_6, col_team_7 = st.columns(4)
        with col_team_4:
            st.markdown(img_to_html('resources/imgs/Nhlanhla.jpg'), unsafe_allow_html=True)
            st.write('**Nhlanhla Mthembu**')
            st.write('Senior Developer')
        with col_team_5:
            st.markdown(img_to_html('resources/imgs/Cara.jpg'), unsafe_allow_html=True)
            st.write('**Cara Brits**')
            st.write('Design Director')
        with col_team_6:
            st.markdown(img_to_html('resources/imgs/Koketso.jpg'), unsafe_allow_html=True)
            st.write('**Koketso Maraba**')
            st.write('Data Scientist')
        with col_team_7:
            st.markdown(img_to_html('resources/imgs/Mxolisi.jpg'), unsafe_allow_html=True)
            st.write('**Mxolisi Zulu**')
            st.write('Data Analist')
        
        with st.form("feedback_form"):
            col_contact_1, col_contact_2 = st.columns(2)
            with col_contact_1:
                st.header("Let's Work Together")
                st.header("Do a Great Project")

                st.write('**Contact number**')
                st.write('+27 87 623 2732')

                st.write('**Contact address**')
                st.write('187 Long St, Cape Town City Centre, Cape Town, 8001')

                st.write('**Contact email**')
                st.write('info@thereeldeel.co.za')
                
            with col_contact_2:
                
                c_contact = st.container()
                with c_contact:
                    text_input = st.text_input("", label_visibility='hidden', placeholder='What should we call you?')
                    text_input = st.text_input("", label_visibility='hidden', placeholder='Please enter your email')
                    text_input = st.text_area("", label_visibility='hidden', placeholder='Please describe your problem')
                    
                submit_contact = st.form_submit_button("Submit")
                
        df = pd.DataFrame(
            [[-33.924852, 18.416760]],
            columns=['lat', 'lon'])

        st.map(df, zoom=13)
            
    if page_selection == "App Feedback":
        st.title("App Feedback")
        st.write("We appreciate your valuable feedback on our app! Your insights and suggestions are crucial in helping us improve and provide you with an exceptional user experience. Please take a few moments to share your thoughts by completing this feedback form. Your input will assist us in understanding what aspects of the app are working well and where we can make enhancements or address any issues you may have encountered.")
        
        with st.form("feedback_form"):
            c_feedback = st.container()

            with c_feedback:
                col_feedback_1, col_feedback_2 = st.columns(2)
                with col_feedback_1:
                    feedback_name = st.text_input(
                        "Name",
                        placeholder='Enter',
                    )
                with col_feedback_2:
                    feedback_email = st.text_input(
                        "Email",
                        placeholder='Enter',
                    )
                col_feedback_3, col_feedback_4 = st.columns(2)
                with col_feedback_3:
                    feedback_type = st.selectbox(
                    'Category',
                    ('Defect', 'Bug', 'Feature'))
                with col_feedback_4:
                    feedback_subject = st.text_input(
                        "Subject",
                        placeholder='Enter',
                    )
                col_feedback_5, col_feedback_6 = st.columns(2)
                with col_feedback_5:
                    feedback_description = st.text_area('Description', '''''')
                with col_feedback_6:
                    tab_low, tab_medium, tab_high = st.tabs(["Low", "Medium", "High"])
                    with tab_low:
                        feedback_priority = 0
                    with tab_medium:
                        feedback_priority = 1
                    with tab_high:
                        feedback_priority = 2

                    feedback_satisfaction = st.radio(
                    "Satisfaction",
                    ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'))

                    st.write('Additional Features')
                    feedback_additional_1 = st.checkbox('UI/UX')
                    feedback_additional_2 = st.checkbox('Performance')
                    feedback_additional_3 = st.checkbox('Functionality')
                    feedback_additional_4 = st.checkbox('Other')
            submit_feedback = st.form_submit_button("Submit Feedback")
    if page_selection == "Analytics":
        st.title("Uncovering Data Insights")
        #Movie ratings Histogram
        st.markdown("""<h4 style="text-align: center;">Movie Ratings Distribution</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        hist_data = pd.read_csv('resources/data/train.csv')
        
        fig, ax = plt.subplots()
        ax.hist(hist_data['rating'],rwidth=0.99,color = "Purple")
        st.pyplot(fig)
        
        st.subheader("Most Rated Overall Movies")
        df_ratings = pd.read_csv('resources/data/df_ratings.csv', encoding = "latin_1")
        top_movies = df_ratings.head(25)
        bottom_movies = df_ratings.tail(25)

        st.markdown("""<h4 style="text-align: center;">25 Most Rated Movies</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_movies=px.bar(top_movies,x='Reviews',y='Title', orientation='h')
        fig_top_movies.update_traces(marker_color='gold',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Title: %{y}</b><br><b>Review Count: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_movies)

        st.subheader("Genre Distribution and Average ratings")
        #Donut Chart
        st.markdown("""<h4 style="text-align: center;">Genre Distribution</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        df_genre_freq = pd.read_csv("resources/data/PieChartData.csv")
        labels = df_genre_freq["Genres"]
        sizes = df_genre_freq["Frequency"]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%0.1f%%',
                shadow=False, startangle=0,labeldistance = 1.05,pctdistance = 0.67,textprops={'fontsize': 5.9})
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        circle = plt.Circle( (0,0), 0.75, color='white')
        p=plt.gcf()
        p.gca().add_artist(circle)
        plt.gca().set_aspect('equal')
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.75)
        st.pyplot(fig1)
        #Ratings bar chart
        st.markdown("""<h4 style="text-align: center;">Average Rating of Genres</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        df_genre_rating = pd.read_csv("resources/data/df_genres_average_ratings.csv")
        fig=px.bar(df_genre_rating,x='Rating',y='Genres', orientation='h')
        fig.update_traces(marker_color='deepskyblue',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Genre: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig)
        #Directors
        #directors data frame
        directors = pd.read_csv("resources/data/df_top_directors.csv", encoding = "latin_1")
        st.subheader("Best and worst performing directors")
        #Best Directors
        st.markdown("""<h4 style="text-align: center;">Best Rated Directors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_directors=px.bar(directors.head(25),x='Rating',y='Director', orientation='h')
        fig_top_directors.update_traces(marker_color='yellowgreen',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Director Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_directors)
        #Worst Directors

        st.markdown("""<h4 style="text-align: center;">Worst Rated Directors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_worst_directors=px.bar(directors.tail(25),x='Rating',y='Director', orientation='h')
        fig_worst_directors.update_traces(marker_color='lightcoral',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Director Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_worst_directors)



        #Actors
        
        st.subheader("Best and worst performing actors")
        actors_df = pd.read_csv("resources/data/actor_ratings_to_plot.csv", encoding = "latin_1")
        best_actors = actors_df.head(30)
        worst_actors = actors_df.tail(30)
        
        st.markdown("""<h4 style="text-align: center;">Best Perfoming Actors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_top_actors=px.bar(best_actors,x='Average Actor Rating',y='Actor', orientation='h')
        fig_top_actors.update_traces(marker_color='green',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Actor Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_top_actors)


        st.markdown("""<h4 style="text-align: center;">Worst Perfoming Actors</h4><p style="text-align: center;"></p>""", unsafe_allow_html=True)
        fig_worst_actors=px.bar(worst_actors,x='Average Actor Rating',y='Actor', orientation='h')
        fig_worst_actors.update_traces(marker_color='red',  # Change the bar color
                      textfont_color='black',  # Change the label text color
                      hovertemplate='<b>Actor Name: %{y}</b><br><b>Rating: %{x}</b>',  # Change the tooltip text
                      selector=dict(type='bar'))  # Select only the bar traces
        st.write(fig_worst_actors)



if __name__ == '__main__':
    main()
