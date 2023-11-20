from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
from sumy.summarizers.text_rank import TextRankSummarizer


class summarizer:
    def __init__(self, text):
        nltk.download("punkt")
        # Utilisation de Sumy avec l'algorithme TextRank
        self.text = text
        self.parser = PlaintextParser.from_string(self.text, Tokenizer("english"))
        self.summarizer_instance = TextRankSummarizer()

    def getSummary(self):
        # Utilisez la méthode summarize() pour obtenir les phrases du résumé
        sentences = [
            str(sentence)
            for sentence in self.summarizer_instance(
                self.parser.document, sentences_count=3
            )
        ]

        # Joignez les phrases pour former le résumé sous forme de chaîne de caractères
        summary_text = " ".join(sentences)

        return summary_text


"""
su = summarizer(
    "Thank you for such a wonderful introduction. Great. I'm here today to talk about motivation. And I've learned, in my few years on this earth, that motivation is really the key to affecting change in anything that you do. You can put a paper that was written without any motivation, without any effort, and you can put a paper that was written with drive and passion next to each other, and it's clear which one is the winner. Motivation is the underlying factor. I believe in everything that we do on a daily basis. If you don't have motivation in something that you do, then you really can't achieve what it is that you want to achieve. Everyone has motivation for things that they're passionate about, things that interest you, things that inspire you. And of course you'll have motivation if you play a sport, if you're in drama, if you're in band, you'll have motivation to accomplish that task. But the true test of finding motivation is if you can find it in something that doesn't work. Personally, I'm interested in sitting through town council meetings and reading the 404 page town of art is a budget. But others might not find so much paper so interesting. However, motivation can be found in everything that you do. I like to look at it in terms of finding motivation as just putting yourself in someone else's shoes. When you're questioning why do I have to do this? Why do I have to put in the time? Why do I have to put in the effort? You can just look at what you're doing and say this helps this person because, where this person is going to appreciate my effort and my motivation on this task because. And I've always found that that appreciation that others have for the effort that you put in, that's what motivates me, the fact that someone's going to appreciate what I did. So when the teacher gives you a paper or something to do and you say this is stupid, I have better things to do. I'd much rather go outside and throw a football, whatever it is. Look at it and say this person is going to appreciate the work. This person put in the effort to create the assignment. Now they're going to see it and they're going to appreciate it. And I do that in every assignment that I'm given and everything that has ever brought before me. And that's always something that I think we need to go out and look at when we go out to tackle an issue. Filing papers. People might not find it interesting. But think about how much help you're doing to somebody else. Think about the responsibility that you're helping someone else fulfill. And that sort of help and appreciation motivates you. For me, fine dressing is something that I like to do every single day. And I don't just do it because I enjoy it. I do it because people appreciate it. People see that. I took the extra time to prepare myself for whatever it is that I'm doing. And they thank me for it. And that thanks that appreciation is truly what motivates me to go out and do whatever it is that has put before me. So I want to finish briefly. I just by saying that motivation is so important in anything that you do. And without it, you really can't accomplish what you want. But with it, you have the passion to affect change. You have the passion to make a difference. And you really do have the passion to go out and change the way things are done and make a difference in anything that you want to do. Thank you for your time and your ears. ?"
)
print(su.getSummary())

from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
import os

os.environ["OPENAI_API_KEY"] = "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"
loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
docs = loader.load()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
chain = load_summarize_chain(llm, chain_type="stuff")

chain.run(docs)

os.environ["REPLICATE_API_TOKEN"] = "r8_MKGiheOj59SybySlXrUlY6rdHdsrEN43F6zWo"
pre_prompt = "you are helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
prompt_input = "Thank you for such a wonderful introduction. Great. I'm here today to talk about motivation. And I've learned, in my few years on this earth, that motivation is really the key to affecting change in anything that you do. You can put a paper that was written without any motivation, without any effort, and you can put a paper that was written with drive and passion next to each other, and it's clear which one is the winner. Motivation is the underlying factor. I believe in everything that we do on a daily basis. If you don't have motivation in something that you do, then you really can't achieve what it is that you want to achieve. Everyone has motivation for things that they're passionate about, things that interest you, things that inspire you. And of course you'll have motivation if you play a sport, if you're in drama, if you're in band, you'll have motivation to accomplish that task. But the true test of finding motivation is if you can find it in something that doesn't work. Personally, I'm interested in sitting through town council meetings and reading the 404 page town of art is a budget. But others might not find so much paper so interesting. However, motivation can be found in everything that you do. I like to look at it in terms of finding motivation as just putting yourself in someone else's shoes. When you're questioning why do I have to do this? Why do I have to put in the time? Why do I have to put in the effort? You can just look at what you're doing and say this helps this person because, where this person is going to appreciate my effort and my motivation on this task because. And I've always found that that appreciation that others have for the effort that you put in, that's what motivates me, the fact that someone's going to appreciate what I did. So when the teacher gives you a paper or something to do and you say this is stupid, I have better things to do. I'd much rather go outside and throw a football, whatever it is. Look at it and say this person is going to appreciate the work. This person put in the effort to create the assignment. Now they're going to see it and they're going to appreciate it. And I do that in every assignment that I'm given and everything that has ever brought before me. And that's always something that I think we need to go out and look at when we go out to tackle an issue. Filing papers. People might not find it interesting. But think about how much help you're doing to somebody else. Think about the responsibility that you're helping someone else fulfill. And that sort of help and appreciation motivates you. For me, fine dressing is something that I like to do every single day. And I don't just do it because I enjoy it. I do it because people appreciate it. People see that. I took the extra time to prepare myself for whatever it is that I'm doing. And they thank me for it. And that thanks that appreciation is truly what motivates me to go out and do whatever it is that has put before me. So I want to finish briefly. I just by saying that motivation is so important in anything that you do. And without it, you really can't accomplish what you want. But with it, you have the passion to affect change. You have the passion to make a difference. And you really do have the passion to go out and change the way things are done and make a difference in anything that you want to do. Thank you for your time and your ears. ?"

output = replicate.run(
    "replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5",
    input={
        "prompt": f"{pre_prompt} {prompt_input} Assistant:",
        "temperature": 0.1,
        "top_p": 0.9,
        "max_length": 250,
        "repetion_penalty": 1,
    },
)
full_response = ""

for item in output:
    full_response += item
print(full_response)
"""
