import streamlit as st
from groq import Groq
import base64

client = Groq(
    api_key=st.secrets["GROQ_API_CHATBOT"],
    )

context = '''
Here are the context of who i am and my working social handles, mails and 
what do i actually do, why you should hire me.
-  MAKE SURE YOU ACT LIKE MY ASSISTANT AND NOT A HUMAN, AND THE USER IS ASKING YOU QUESTIONS., ANSWER THEM LIKE I MAY WOULD.(TAKE DECISION ON YOUR OWN, SMARTLY)
- SO, my name is Shivam Verma, a 2nd year student at MSIT, Delhi. Pursuing B.Tech in Computer Science.
'''

# For rendering images in streamlit app
def render_image(filepath: str):
   """
   filepath: path to the image. Must have a valid file extension.
   """
   mime_type = filepath.split('.')[-1:][0].lower()
   with open(filepath, "rb") as f:
    content_bytes = f.read()
    content_b64encoded = base64.b64encode(content_bytes).decode()
    image_string = f'data:image/{mime_type};base64,{content_b64encoded}'
    st.image(image_string)

# Icon for this streamlit web app
# def icon(emoji: str):
#     """Notion-like page icon."""
#     st.write(
#         f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
#         unsafe_allow_html=True,
#     )
# icon("🏎️")

# Define a function to get completion from the Groq API
def get_completion(user_question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''{context}

 {user_question}''',
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Web Styling of Streamlit
st.set_page_config(page_title="Shivam Verma - @shivamm-verma", layout="centered")

st.title("Hey, Shivam Verma's bot here.🙌🏼")

# headline of the page
st.markdown("""
            
    Deputy Head @ GDG,MSIT | GSsOC'24 | Open-source Contributor | MSIT'27 | GGSIPU | Hackathons participated(x2)
            
    My major roles are:
    - Web Developer
    - Video Editor (ask for my work)
    - Freelancers (Reach out to my mail)
    - You can even ask me to build you this kind of bot, I can help you with that too.
    
    All handles: [Links Coming soon, but my GitHub](https://github.com/shivamm-verma)
        
    Want to Sponsor me?💌: [My GitHub Sponsors](https://github.com/sponsors/shivamm-verma)
""")
# Will add my social handles/`LinkAll` repo deployed website link here

# Add a sidebar with previous hackathon details and links
st.sidebar.title("Who am I?")

# Adding images to the sidebar
# st.sidebar.image("Images/Shivam_github_card.png")
st.sidebar.image("Images/shivam_pfp.jpg")
st.sidebar.markdown("""
    
                  

    ### My Mail to Contact/Hire me:
    - [shivam.verma256@outlook.com](mailto:shivam.verma256@outlook.com)
    - [sv35215@gmail.com](mailto:sv35215@gmail.com)
    
""")

# Separated by a line
st.sidebar.markdown("""___
                    """) 

st.sidebar.markdown("""
    ### Additionally, few of my GitHub Stats:
    ![Shivam's GitHub stats](https://github-readme-stats.vercel.app/api?username=shivamm-verma&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)  

    ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=shivamm-verma&layout=pie)
""")

# Separated by a line
st.sidebar.markdown("""___
                    """)

st.sidebar.markdown("""
    
""")

# Input Section with Loader text
user_question = st.text_input("Ask the bot about me:")

if st.button("Submit"):
    if user_question:
        with st.spinner("Taking my decision⌛..."):
            # Get completion from the Groq API
            response = get_completion(user_question)
            # Display the response
            st.markdown(f"**Response:** {response}")
    else:
        st.error("Please enter a question before submitting.")
