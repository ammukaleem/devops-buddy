from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['GET', 'POST'])
def command():
    result = ""
    if request.method == 'POST':
        resource = request.form['resource']
        action = request.form['action']
        result = f"kubectl {action} {resource}"
    return render_template('command.html', result=result)

@app.route('/yaml', methods=['GET', 'POST'])
def yaml_generator():
    yaml_output = ""
    if request.method == 'POST':
        name = request.form['name']
        image = request.form['image']
        replicas = request.form['replicas']

        yaml_output = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
spec:
  replicas: {replicas}
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
      - name: {name}
        image: {image}
"""
    return render_template('yaml.html', yaml_output=yaml_output)

@app.route('/cheat')
def cheat():
    return render_template('cheat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
