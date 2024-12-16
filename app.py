from flask import Flask, render_template, request, jsonify
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

template = """
You are a professional chef and culinary expert. Your task is to generate a creative, unique, and easy-to-follow recipe based on the user's preferences.

### Example Recipes:
**Example 1:**
**Recipe Name:**  
Lemon Herb Grilled Chicken  

**Ingredients:**  
- 4 chicken breasts  
- 2 tbsp olive oil  
- 1 lemon, juiced  
- 1 tsp garlic powder  
- Salt and pepper to taste  

**Instructions:**  
1. Preheat grill to medium-high heat.  
2. In a bowl, combine olive oil, lemon juice, garlic powder, salt, and pepper.  
3. Marinate chicken breasts in the mixture for 30 minutes.  
4. Grill chicken for 6-8 minutes per side until fully cooked.  
5. Serve hot with your favorite side dish.

**Example 2:**
**Recipe Name:**  
Vegetarian Pasta Primavera  

**Ingredients:**  
- 2 cups spaghetti  
- 1 bell pepper, diced  
- 1 zucchini, sliced  
- 1/2 cup cherry tomatoes, halved  
- 1 tbsp olive oil  
- Salt and pepper to taste  

**Instructions:**  
1. Cook spaghetti according to package instructions.  
2. In a pan, heat olive oil and sauté the bell pepper, zucchini, and cherry tomatoes until tender.  
3. Toss the cooked spaghetti with the sautéed vegetables.  
4. Season with salt and pepper, and serve warm.

---

The user has requested:
- **Meal Type:** {type}
- **Cuisine Preference:** {cuisine}
- **Dietary Restrictions:** {restrictions}
- **Maximum Cooking Time:** {time}.

Please think step-by-step:
1. Identify a recipe that fits the specified meal type and cuisine.
2. Ensure the recipe aligns with any dietary restrictions provided.
3. Optimize the recipe to be prepared within the given cooking time.
4. Make the recipe easy to follow, using simple steps and ingredients common in the specified cuisine.

Respond in the following format:

**Recipe Name:**  
[Creative Recipe Name]  

**Ingredients:**  
- Ingredient 1  
- Ingredient 2  
- Ingredient 3  

**Instructions:**  
1. Step 1  
2. Step 2  
3. Step 3  
"""

prompt = PromptTemplate(
    input_variables=["type", "cuisine", "restrictions", "time"],
    template=template,
)

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.7,
    max_output_tokens=500,
    api_key=os.getenv("GOOGLE_API_KEY"),
)

chain = prompt | llm

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    meal_type = request.form.get("type")
    cuisine = request.form.get("cuisine")
    restrictions = request.form.get("restrictions")
    time = request.form.get("time")

    try:
        response = chain.invoke(
            {
                "type": meal_type,
                "cuisine": cuisine,
                "restrictions": restrictions,
                "time": time,
            }
        )
        recipe_content = response.content
        return jsonify({"recipe": recipe_content})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
