# OPENAI_API_KEY=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

import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
# from langchain_community.chat_models import ChatOpenAI   Deprecated
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    print("Langchain welcomes you")
    print(os.environ["OPENAI_API_KEY"])
    print(os.environ["PROXYCURL_API_KEY"])
    print(os.environ["SERPAPI_API_KEY"])
    # information="""Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is the second wealthiest person in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $182.6  billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6][7]
    #     A member of the wealthy South African Musk family, Elon was born in
    #     Pretoria and briefly attended the University of Pretoria before immigrating
    #     to Canada at age 18, acquiring citizenship through his Canadian-born mother.
    #     Two years later, he matriculated at Queen's University at Kingston in Canada.
    #     Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics.
    #     He moved to California in 1995 to attend Stanford University, but dropped out after two days and,
    #     with his brother Kimbal, co-founded online city guide software company Zip2.
    #     The startup was acquired by Compaq for $307 million in 1999, and,
    #     that same year Musk co-founded X.com, a direct bank.
    #     X.com merged with Confinity in 2000 to form PayPal."""

    summary_template = """
    given the information {information} about a person i want you to create:
    1. A short summary
    2. two interesting facts about then
    3. Age of Elon when he moved to California
    """
    linkedin_profile_url=linkedin_lookup_agent(name="Eden Macro Udemy")
    linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url=linkedin_profile_url#"https://www.linkedin.com/in/harrison-chase-961287118/"
)
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template     #information
    )
    llm = ChatOpenAI(temperature=0)  # model_name="gpt-3.5-turbo"

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # res=chain.invoke(input={"information":information})
  

    res = chain.run(information=linkedin_data)
    print(res)
