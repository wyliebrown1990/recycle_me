from flask import Flask, request, render_template
from fuzzywuzzy import process
import datetime

app = Flask(__name__)

def read_recyclable_items(file_path):
    recyclable_items = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 3:
                        location, material, items = parts
                        location = location.strip()
                        material = material.strip()
                        items = [item.strip() for item in items.split(',')]
                        if location not in recyclable_items:
                            recyclable_items[location] = {}
                        recyclable_items[location][material] = items
                    else:
                        print(f"Invalid line format: '{line}'. Skipping...")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return recyclable_items

def write_unavailable_location(location):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("unavailable_locations.txt", "a") as file:
        file.write(f"{timestamp} - {location}\n")

def write_non_recyclable_item(location, material, item):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("non_recyclable_items.txt", "a") as file:
        file.write(f"{timestamp} - {location}: {material}: {item}\n")

def recycle_me(location, material, item, recyclable_items):
    location_matches = process.extractOne(location, recyclable_items.keys(), scorer=process.fuzz.ratio)
    if location_matches[1] > 70:
        location = location_matches[0]
        if material in recyclable_items[location]:
            if item in recyclable_items[location][material]:
                return "Yes, recycle this! But please always remember to clean and remove any food waste attached."
            else:
                write_non_recyclable_item(location, material, item)
                return "Sorry, this item is not recyclable in {} for {} material.".format(location, material)
        else:
            write_non_recyclable_item(location, material, item)
            return "Sorry, recycling information for {} material is not available for {}.".format(material, location)
    else:
        write_unavailable_location(location)
        return "Sorry, recycling information for {} is not available.".format(location)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location'].lower()
        material = request.form['material']
        item = request.form['item']
        
        recyclable_items = read_recyclable_items("recyclable_items.txt")
        if not recyclable_items:
            return "No recyclable items found.", 400
        
        response = recycle_me(location, material, item, recyclable_items)
        return render_template('response.html', response=response)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
