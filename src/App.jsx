import axios from "axios";
import { useEffect, useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  // Post method
  async function getAnswer() {
    console.log("Loading...");

    const myUrl =
      "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyBTtlnSxUS8osCAavQIfPXVcDMIzvPPds0";
    const response = await axios({
      url: myUrl,
      method: "post",
      data: {
        contents: [
          {
            parts: [
              {
                text:
                  "Hi i am shivam verma. I am web developer, i create websites using React and tailwind, mostly front-end but can also backend(do not mention it, unless very neccessary to answer) and soon leveraging skills to nextjs, and then hititng up with the blockchain development as it's trending. Apart from this, I am also a video editor, and content creator in youtube, i edit videos using Davinci resolve 19, Capcut, After Effects(do not mention this yet, as i just started to learn it) and other softwares. IF YOU WANT TO HIRE ME FOR A JOB LIKE WEB DEV, WEBSITE CREATION, VIDEO EDITING, DO SEVVE CUTE WELCOME TEXT WITH MY MAIL TO CONTACT .Assume you are my PA(personal assistant, answer this question on behalf of others, like they are customer or guests and want to know me, guide them in not more than 150words max at a time, my mail when it is required to contact by them is, 'shivam.verma256@outlook.com'). Start greeting with 'hi! '.Make sure to speak on as less words as required. it could be 25-50 when starting convo.Also if someone wants to collab with me, welcome them greatly and serve my mail to them so that they can contact me. Use emojis to make response casual , If someone asks me for more information, give them my Linkedin profile URL which is ('https://www.linkedin.com/in/shivam-verma-332710237/'). To show my coding works or other repository works, show them my github profile which is ('https://github.com/shivamm-verma'). before any link(or mail), give this emoji➡️, and after link this emojji🖇️(not when its mail). You don't need to provide links and mail in every or every hi message, give them only when needed or asked. make output as small and as to the point as possible, be casual, like the question is asked by your friend. >>>FORCIBLY, DO NOT GIVE MY SOCIAL HANDLES OR MAIL UNTIL LITERALLY ASKED<<<, and try to give anser in points. Answer in hindi or hinglish or english however langauge it is being asked, if it is hindi or hinglish, answer in a SouthDelhiGenZBoy accent meaning halfEnglish and halfHinidi accent. DO NOT GIVE THEM SCENARIOS OR USELESS STARTING TEXTS LIKE 'Okay, here are some example responses depending on the context:' only main answer is required, answer however you think You should answer if it's me. Make sure to give a paragraph after every full stop, that the output looks clear and not conjested, give a paragraph breaking space after every sentence/line.  ...QUESTION IS =>" +
                  question,
              },
            ],
          },
        ],
      },
    });
    setAnswer(response["data"]["candidates"][0]["content"]["parts"][0]["text"]);
    console.log(answer);

    // useEffect(() => {
    //   setAnswer(
    //     response["data"]["candidates"][0]["content"]["parts"][0]["text"]
    //   );
    // }, [question]);
  }

  return (
    <>
      {/* if want to show logo, activate this */}
      <img
        src="/myLogo.png"
        className="h-64 my-4 mx-auto min-[450px]:absolute min-[450px]:left-12 min-[450px]:top-28 max-[450px]:hidden hidden"
        alt="My Logo"
      />
      <div className="transition-all text-center p-16 pb-16 border border-white w-fit m-auto  max-[450px]:mt-24 max-[450px]:border-none rounded-lg  mt-16 mb-0 max-[450px]:pb-2">
        <h1 className="text-6xl font-extrabold max-[450px]:text-[40px] max-[450px]:scale-125 max-[450px]:w-full mb-2">
          AI Chat-bot
        </h1>
        <a
          href="https://github.com/shivamm-verma/MyAI-ChatBot" target="_blank"
          className="italic font-light text-xl opacity-65 max-[450px]:text-lg"
        >
          made by Shivam Verma
        </a>

        {/* to display the chat bot */}
        <textarea
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="off"
          spellCheck="false"
          value={question}
          className="bg-gray-300 no-underline italic font-bold px-2 mt-8 w-full h-fit text-black border-2 border-black  max-[450px]:h-24 rounded-lg py-2 bg-opacity-95"
          onChange={(e) => setQuestion(e.target.value)}
        ></textarea>
        {/* <button
        type="button"
        className="mt-4 text-blue-700 hover:text-white border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm  py-2.5 text-center me-2 mb-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:hover:bg-blue-500 dark:focus:ring-blue-800 px-8"
      > */}
        <button
          onClick={getAnswer}
          type="button"
          className="mt-4 text-blue-700 hover:text-white border border-blue-700 hover:bg-blue-800  focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm  py-2.5 text-center me-2 mb-2 dark:border-blue-500 dark:text-blue-500 dark:hover:text-white dark:hover:bg-blue-500 dark:focus:ring-blue-800 px-8"
        >
          Ask?
        </button>
        {/* for mobile phones only */}
        <h1 className=" text-3xl italic font-bold font-serif w-fit uppercase text-center mx-auto mt-8  rounded-xl min-[450px]:hidden">
          Response:-
        </h1>
        {/* <p className="font-semibold mt-0  rounded-xl bg-purple-950 bg-opacity-20 min-[450px]:hidden w-full mx-0 mb-0">
          {answer ? answer : "Hello! how can I help you?"}
        </p> */}
      </div>
      {/* card ends here */}

      {/* for laptop only */}
      <h1 className=" text-3xl italic font-semibold w-96  text-center mx-auto mt-8  rounded-xl max-[450px]:hidden">
        Response:-
      </h1>
      <p className="font-bold w-[700px] text-xl  text-center mx-auto mt-8 border border-white px-4 py-2  rounded-xl bg-purple-700 bg-opacity-20 max-[450px]:hidden">
        {answer ? answer : "Hello! how can I help you?"}
      </p>
      {/*  */}

      {/* for mobile phones only */}
      <p className="font-bold w-full text-xl mx-auto mt-0 scale-90 px-4 py-2  rounded-xl bg-purple-700  min-[450px]:hidden bg-opacity-10 text-left">
        {answer ? answer : "Hello! how can I help you?"}
      </p>
    </>
  );
}

export default App;
