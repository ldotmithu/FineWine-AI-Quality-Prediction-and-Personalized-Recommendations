from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pandas as pd
import os
from dotenv import load_dotenv
import groq
from src.Pipeline.prediction import Predication_Pipeline  
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



client = groq.Client(api_key=GROQ_API_KEY)


prediction_pipeline = Predication_Pipeline()

class GenAI:
    def __init__(self):
        self.llm = ChatGroq(temperature=0.5, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")
        
    def system_prompt(self):


        prompt_template = PromptTemplate(
    input_variables=["input_data", "quality"],
    template="""
    You are a professional **AI Wine Sommelier** with extensive expertise in wine chemistry, tasting, and pairing. 
    Your task is to **analyze the provided wine characteristics** and explain why it has been classified as "Good" or "Bad." 
    Additionally, offer **actionable recommendations** to enhance the wine's overall quality.

    ---
    ### 🍷 **Wine Quality Analysis**
    - **Wine Properties:** {input_data}
    - **Predicted Quality:** {quality} (0 = Bad, 1 = Good)

    ---
    ### 🔍 **Reason for Classification**
    - Provide a thorough explanation of how the wine’s **acidity**, **alcohol balance**, **body**, and **overall flavor profile** contribute to the classification as "Good" or "Bad."
    - Highlight specific characteristics like **fixed acidity**, **volatile acidity**, **pH**, **sugar content**, and **alcohol percentage** to justify the classification.

    ---
    ### 🛠️ **Improvement Strategies**
    - If the wine is **Bad**, offer detailed and practical recommendations to improve its quality:
      - **Aeration & Decanting**: Explain how exposing the wine to air can enhance flavors and aromas.
      - **Blending**: Suggest blending with complementary wines (e.g., higher acidity or fruit-forward wines) to achieve better balance.
      - **Serving Temperature**: Recommend optimal temperature adjustments to improve flavor perception.
      - **Food Pairing**: Propose suitable food pairings that can balance or mask any undesirable flavors in the wine.
    - If the wine is **Good**, highlight its strengths and suggest **ways to further elevate the experience**:
      - Emphasize ideal food pairings, best glassware, and serving methods.

    ---
    ### 🎉 **Good Wine Cheers! (Only if Quality is Good)**
    - If the wine is classified as **Good**, provide a cheerful and encouraging note to enhance the user's experience with the wine.  
      - Example: "This is a beautifully balanced wine with rich flavors—perfect for a delightful evening! 🍷 Cheers!"

    ---
    🎉 **Enjoy your wine experience!** 🍷
    """
)


        return prompt_template
    
    def response(self, input_data):
        try:
            column_names = ['fixed acidity', 'volatile acidity', 'citric acid','chlorides','total sulfur dioxide', 'density', 'pH','sulphates','alcohol']
            prompt_template = self.system_prompt()

            input_data_df = pd.DataFrame(input_data, columns=column_names)

            input_data_processed = prediction_pipeline.transform(input_data_df)

            predicted_value = prediction_pipeline.prediction(input_data_processed)[0]
            quality_label = "Good" if predicted_value == 1 else "Bad"

            rag_chain = LLMChain(llm=self.llm, prompt=prompt_template)
            response = rag_chain.invoke({"input_data": input_data, "quality": quality_label})

            return response["text"]

        except Exception as e:
            return f"Error generating response: {str(e)}"
