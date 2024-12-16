# Creative-Recipe-Generator

This is a training task on Prompt Engineering

## The idea behind this app

This app is a web-based application where users can specify details such as the **meal type**, **cuisine preference**, **dietary restrictions**, and **maximum cooking time**, and the app will generate a creative recipe based on those inputs.
The main idea of this app is to

- Generate recipes based on user input preferences.
- Adjust recipes to respect dietary restrictions.
- Optimize recipes to be prepared within the given time.
- Simple, easy-to-follow instructions and ingredients.

## How to Run the App Locally

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your **Google API Key**:

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## How Prompting Techniques Were Applied

I have used several **prompting techniques** to create a tailored recipe, the techniques used are as follows:

1. **Role-Based Prompting**:  
   The AI is assigned the role of a professional chef and culinary expert to guide the tone and style of the response.
   Example: "You are a professional chef and culinary expert."

2. **Direct Prompting**:  
   The AI was asked to do one specific task.
   Example: "Your task is to generate a creative, unique, and easy-to-follow recipe based on the user's preferences."

3. **Contextual Prompting**:

   The AI is provided with additional context based on the user's input like type, cuisine, dietary restrictions, ingredients, and cooking time.
   Example: "The user has requested: - **Meal Type:** {type} - **Cuisine Preference:** {cuisine} - **Dietary Restrictions:** {restrictions} - **Maximum Cooking Time:** {time}."

4. **Few-Shot Prompting**:  
    Two example recipes are provided within the prompt to guide the AI in producing recipes with the desired structure and formatting.
   Example: "**Example 1:**
   **Recipe Name:**  
    Lemon Herb Grilled Chicken ...
   **Example 2:**
   **Recipe Name:**  
    Vegetarian Pasta Primavera ..."

5. **Chain-of-Thought Prompting**:

   The AI is instructed to think through the recipe generation process step-by-step before producing the final recipe.
   Example: "Please think step-by-step: 1. Identify a recipe that fits the specified meal type and cuisine...."

## Parameters Tweaked and Why

- **Temperature**: Set to 0.7 to control the creativity of the response. I believed a value of 0.7 creates a good balance between creativity and coherence needed for the recipe genration.
- **Max Output Tokens**: Set to 500 to ensure the recipe response is sufficiently detailed but not too long.
