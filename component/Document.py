from hmr.hmr import javascript


class Document:
    def __init__(self):
        self.head = ""
        self.body_ = ""

    def title(self, text):
        self.head += f"<title>{text}</title>\n"

    def meta(self, **attributes):
        meta_tag = "<meta "
        for key, value in attributes.items():
            meta_tag += f'{key}="{value}" '
        meta_tag += "/>\n"
        self.head += meta_tag

    def body(self, *elements: object) -> object:
        modified_elements = '\n'.join([str(element) for element in elements])
        self.body_ = f"{modified_elements}"

    def build(self):
        # Constructing the HTML content
        html_content = f"""
        <html>
        <head>
        {self.head}
        </head>
        <body>
        {self.body_}
        </body>
        {javascript}
        </html>
        """

        # Write modified content back to file
        with open('./output/index.html', 'w') as file:
            file.write(html_content)
            print(html_content)