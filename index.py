from flask import Flask, request, jsonify
import openai

app = Flask(_name_)

api_key = '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'

categories = ['Family Law', 'Corporate Law', 'Criminal Law', 'Intellectual Property Law', 'Tax Law', 'Civil Law',
              'Constitutional Law', 'Medical Law', 'Human Rights Law', 'Real Estate Law', 'Media and Entertainment Law',
              'Environmental Law', 'Consumer Protection Law', 'Banking and Finance Law', 'Immigration Law', 'Labor Law']

@app.route('/user-classify', methods=['POST'])
def user_classify():
    try:
        data = request.get_json()
        text_to_classify = data.get('label', '')

        categories_prompt = f"Classify the following case description into two of these categories: {', '.join(categories)}\n"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text_to_classify + categories_prompt,
            max_tokens=30,
            stop=None,
            temperature=0.0,
            api_key=api_key
        )

        predicted_category = response.choices[0].text.strip()

        return jsonify({'predicted_category': predicted_category})

    except Exception as e:
        return jsonify({'error': str(e)})

if _name_ == '_main_':
    app.run(debug=True)
