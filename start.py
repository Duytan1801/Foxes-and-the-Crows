import latex2markdown
with open("31076-t.tex", "r") as f:
    latex_string = f.read()

l2m = latex2markdown.LaTeX2Markdown(latex_string)

markdown_string = l2m.to_markdown()

with open("markdown_file.md", "w") as f:
    f.write(markdown_string)