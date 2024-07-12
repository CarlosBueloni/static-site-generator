from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode

def main():
    t_node = TextNode("This is a text node",text_type_bold, "https://www.boot.dev")
    print(t_node)

    h_node = HTMLNode("<a>", "this is a link", props={"href": "https://www.google.com"})
    print(h_node)

if __name__ == "__main__":
    main()
