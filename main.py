import binascii
import flet as ft
from io import BytesIO
from smpp.pdu.pdu_encoding import PDUEncoder


def pdu(hex_input):
    """
    This is the function that processes the HEX variable.
    Replace the logic below with your specific PDU processing code.
    """
    binary = binascii.a2b_hex(hex_input)
    file = BytesIO(binary) 
    return PDUEncoder().decode(file)

def main(page: ft.Page):
    page.title = "RPTANGO - SMPP PDU Decoder"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # Define the result text field
    # Changed color to HEX string to avoid AttributeError
    result_text = ft.Text(value="", size=16, color="#263238") # Blue Grey 900

    # Define the input field for the HEX variable
    hex_input = ft.TextField(
        label="Enter PDU/HEX",
        hint_text="e.g., 001122AABB",
        width=600,
        text_align=ft.TextAlign.LEFT,
        # Changed color to HEX string
        border_color="#2196F3" # Blue 500
    )

    # Event handler for the button
    def on_run_click(e):
        # Get the variable from the input
        hex_variable = hex_input.value
       
        # Run the requested function: pdu(hex)
        output = pdu(hex_variable)
        # Update the UI with the result
        output_pre = str(vars(output))
        output_final = output_pre.replace(",", ",\n")
        result_text.value = output_final
        print (result_text.value)
        page.update()
        
    # Función para copiar al portapapeles
    def copy_to_clipboard(e):
        page.set_clipboard(result_text.value)
        page.open(ft.SnackBar(ft.Text("PDU has been copied to your clipboard!")))

    # Botón de copiar (inicialmente oculto)
    btn_copy = ft.IconButton(
        icon="content_copy",
        tooltip="Copy Decode",
        on_click=copy_to_clipboard,
        icon_color="#546E7A",
        visible=True 
    )
    # Define the button
    
    run_button = ft.ElevatedButton(
        text="Run PDU Decoder",
        on_click=on_run_click,
        # Changed icon to string name and colors to HEX strings
        icon="play_arrow",
        bgcolor="#1E88E5", # Blue 600
        color="#FFFFFF"    # White
    )

    def on_header_click(e):
        page.launch_url("https://github.com/rptango")

    header_image = ft.Container(
        content=ft.Image(
            src="https://brand.github.com/_next/static/media/logo-04.9a1517f0.png",
            width=150,
            height=150,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(75),# circular
            ),
            on_click=on_header_click,
            #cursor=ft.MouseCursor.CLICK,
            border_radius=ft.border_radius.all(75),
            ink=True,
            tooltip="Clicl to be redirected"
    )

    # Add elements to the page
    # Contenedor para el resultado y el botón de copiar alineados
    result_container = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=result_text,
                    expand=True, # Ocupar el espacio disponible
                ),
                btn_copy
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.START
        ),
        padding=10,
        bgcolor="#E3F2FD",
        border_radius=5,
        width=600 # Mismo ancho que el input
    )
    page.add(
        ft.Column(
            [
                header_image,
                ft.Text("SMPP PDU Decoder", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("Lightweight utility that converts hex-encoded SMPP packets into a structured PDU, making headers and payloads easy to inspect.", size=15),
                ft.Divider(height=20, thickness=1),
                hex_input,
                run_button,
                ft.Divider(height=20, thickness=1),              
                result_container
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
if __name__ == "__main__":
    ft.app(target=main)