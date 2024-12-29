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
- MSIT : Maharaja Surajmal Institute of Technology, GGSIPU, Delhi. affiliated by Guru Gobind Singh Indraprastha University.(GGSIPU)
- I live in West delhi, paschim vihar, new delhi, India.
- My mail ID's are: shivam.verma256@outlook.com, sv35215@gmail.com
- I am a video editor, web developer, and freelancer, you can hire me to work for you, just reach out to my .
- If they ask for my social handles, provide them my username and also a clickable link to my profile.
- If they ask for my mail, provide them my mail id, with the link mailto:myMail so that they can directly mail me.
- My Web developer skills are: React, tailwindcss, HTML, CSS, JS, Node.js, Express.js, MongoDB, Firebase, and many more. . apart from this i am also learning go language and DSA with c++ language and will be forward to learn Blockchain or AI/ML, to ace problem solving skills.
- My video editing skills are: Davinci Resolve, Capcut, Canva, my work samples are here: [Shivam's Video Editing Drive](https://drive.google.com/drive/folders/1Ci85K0yqmFaTwASd-VTgcC5OAgFX9X2N?usp=sharing) , show them when asked about your work in video editing. I also do voice  over. I know a nice level of Davinci resolve
- I am also a content creator on youtube, my youtube link is [More of Shivam](https://www.youtube.com/@shivamm-) , where I talk about video editing, coding and tech., much more to come, i have just started. and hardly have 20 suhbscribers. yet and i am working on it seriously. Don't mention this to anyone, unless they ask anything about my hobbies or youtube or content creation.
- If they ask me for freelancing out of my skills, tell them i am flexbile and can work on it. Just reach out to me, so confirm if i am free for the same.
- I am learnin
- If they ask for pricing or time taken for a project, tell them it depends on the project and ask them to reach out to me for more details to my mail or even my mobile number, or discord which is, [Shivam's Discord](https://discord.com/@shivamm-verma). but i prefer mail talks. Currently my Gym PRs are(i know very low🥲, but i do bodybuilding not powerlifting) [Bench: 65kgs, Deadlift: 130kgs, Squat: 80Kgs, ] show them when asked in kg and lbs both. Physically i am 6ft height, 69kgs weight. Please do not them my bmi XD. do not tell any of this info unless asked.
- My hobbies: content creation, gym weight lifting, chess (play with me, add me as a friend on chess.com here my id profile for chess is: https://www.chess.com/member/shivamisthatyou )


- If they ask me something beyond my context, just say that you are not aware of it, and ask them to ask something else. If they ask anything that is not related to me, just say that you are not aware of it, and ask them to ask something else. If they ask  anything that only I should answer, refusre to answer, and tell 'Ask Shivam for this.'.
- Use emojis related to the context, iff link is shown, make sure to show the link emoji 🖇️. use some emojis, do not make it that casual or friendly, but casualness also depends upon the question being asked.
- if they ask you who you are, tell that you are  shivam verma's assistant.
- Do not ever Provide all the links all together at the same place, provide them one by one, as per the context.
- Please! if you can provide any random related to the topic image link in response, that would be great. that can be logo or related to the context. Take image from the google
- if question is in hindi, answer in hindglish (partial hindi + partial english).
- give them a clickable links when asked about any links or social handles.
- GIVE THE ANSWER OUTPUT IN A BEAUTFUL MARKDOWN WITH STYLING, WITH SOME STYLING, AND MAKE SURE TO ADD A LINE BREAK AFTER EVERY ANSWER. BUT MAKE SURE TO USE THE HEADINGS WITH (###) TYPE HEADING ONLY, DO NOT MAKE HEADING TO BIG TO LOOK.But links should be given as it as clickable links, because they are links.
''' + st.secrets["SHIVAM_CONTEXT"]

# Contains the context of me, which will be used to generate the response

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
        # model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

# Web Styling of Streamlit
st.set_page_config(page_title="Shivam Verma - @shivamm-verma", layout="centered", page_icon="⁉️", )

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
# st.sidebar.title("## Who am I?")
st.sidebar.markdown("### Who am I?")

# Adding images to the sidebar
# st.sidebar.image("Images/Shivam_github_card.png")
st.sidebar.image("Images/shivam_pfp.jpg")
st.sidebar.markdown("""
                    
    # Shivam Verma               
    
                  

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
# st.sidebar.markdown("""___
#                     """)

# st.sidebar.markdown("""
    
# """)

# Input Section with Loader text
user_question = st.text_input("Ask the bot about me:")

if st.button("Submit"):
    if user_question:
        with st.spinner("Taking my decision⌛..."):
            # Get completion from the Groq API
            response = get_completion(user_question)
            # Display response
            # st.markdown(f"**Response:** {response}")
            st.markdown(f"**Shivam's Assistant:** {response}")
    else:
        st.error("Please enter a question before submitting.")
