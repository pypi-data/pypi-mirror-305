import gradio as gr
from gradio_pagination import pagination

total=10000
current_page = 1
page_size = 10

def show_page_info_into_text_box(data):
    global current_page, page_size
    current_page = data.page
    page_size = data.page_size
    print(data)
    return str(current_page), str(page_size)

with gr.Blocks() as demo:
    gr.Markdown("## Pagination Demo")
    pagination_component = pagination(total=total, page=1, page_size=10)
        
    with gr.Row():
        page_display = gr.Textbox(label="Current Page", value=str(current_page), interactive=False)
        size_display = gr.Textbox(label="Page Size", value=str(page_size), interactive=False)

    pagination_component.change(
        fn=show_page_info_into_text_box,
        inputs=pagination_component,
        outputs=[page_display, size_display]
    )

if __name__ == "__main__":
    demo.launch()
