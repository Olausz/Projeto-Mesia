from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Listas para tarefas e itens do glossário
tasks = []
glossary_items = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/glossario')
def glossario():
    return render_template('glossario.html', items=glossary_items)

@app.route('/lista')
def lista():
    return render_template('lista.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        if request.form.get('is_glossary'):
            glossary_items.append(item)
            return redirect('/glossario')
        else:
            tasks.append(item)
            return redirect('/lista')

@app.route('/remove/<int:index>')
def remove_item(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    elif 0 <= index < len(glossary_items):
        del glossary_items[index]
    return redirect('/lista') if request.args.get('is_glossary') else redirect('/glossario')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_item(index):
    if 0 <= index < len(tasks):
        items = tasks
        route_name = 'lista'
    elif 0 <= index < len(glossary_items):
        items = glossary_items
        route_name = 'glossario'
    else:
        return redirect('/lista') if request.args.get('is_glossary') else redirect('/glossario')

    if request.method == 'POST':
        new_item = request.form.get('item')
        items[index] = new_item
        return redirect(f'/{route_name}')
    else:
        return render_template('editar.html', item=items[index], index=index)

if __name__ == '__main__':
    app.run(debug=True)
