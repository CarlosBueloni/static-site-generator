from textnode import TextNode, text_type_bold
from htmlnode import HTMLNode, LeafNode

def main():
    t_node = TextNode("This is a text node",text_type_bold, "https://www.boot.dev")
    print(t_node)

    h_node = HTMLNode("<a>", "this is a link")
    print(h_node.props_to_html())
    
    l_node = LeafNode(value="This is a paragraph of text.")
    print(l_node.to_html())
    l_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(l_node2.to_html())
if __name__ == "__main__":
    main()
