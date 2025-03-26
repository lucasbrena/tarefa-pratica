from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.form.get('weight'))
    height = float(request.form.get('height'))

    if not weight or not height:
        return render_template('result.html', error="Weight and height are required")

    try:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            message = f"Seu IMC é: {bmi:.2f}. Você está abaixo do peso."
        elif bmi < 24.9:
            message = f"Seu IMC é: {bmi:.2f}. Você está com peso normal."
        elif bmi < 29.9:
            message = f"Seu IMC é: {bmi:.2f}. Você está acima do peso."
        else:
            message = f"Seu IMC é: {bmi:.2f}. Você está obeso."
        return render_template('result.html', message=message)
    except Exception as e:
        return render_template('result.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)