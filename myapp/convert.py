import markdown

# Function open the Picnic.md file and passing the value r
with open('helper.md', 'r') as f:

# save the file object in variable f
    text = f.read()
# save the result in variable html
    html = markdown.markdown(text)

with open('helper.html', 'w') as f:
    f.write(html)
