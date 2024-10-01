import flet as ft

def main(page):
    page.title = "Conversor de Moedas"
    page.scroll = "adaptive"

    def converter(e):
        try:
            valor = float(valor_input.value)
            if moeda_inicial.value == "BRL":
                if moeda_final.value == "USD":
                    result = valor / 5.25  # Taxa de exemplo
                elif moeda_final.value == "EUR":
                    result = valor / 5.70  # Taxa de exemplo
                else:
                    result = valor
            elif moeda_inicial.value == "USD":
                if moeda_final.value == "BRL":
                    result = valor * 5.25
                elif moeda_final.value == "EUR":
                    result = valor * 0.95  # Taxa de exemplo
                else:
                    result = valor
            elif moeda_inicial.value == "EUR":
                if moeda_final.value == "BRL":
                    result = valor * 5.70
                elif moeda_final.value == "USD":
                    result = valor * 1.05  # Taxa de exemplo
                else:
                    result = valor

            result_text.value = f"Resultado: {result:.2f} {moeda_final.value}"
        except Exception as e:
            result_text.value = f"Por favor, insira um valor numérico válido. {e}."
        
        page.update()

    title = ft.Text("Conversor de Moedas Básico", size=50, weight="bold", font_family="Cooper", color="white")
    valor_input = ft.TextField(label="Valor a converter:", width=400)
    moeda_inicial = ft.Dropdown(label="Converter de", width=400, options=[
        ft.dropdown.Option("BRL", "Real"),
        ft.dropdown.Option("USD", "Dólar"),
        ft.dropdown.Option("EUR", "Euro"),
    ])
    moeda_final = ft.Dropdown(label="Para", width=400, options=[
        ft.dropdown.Option("BRL", "Real"),
        ft.dropdown.Option("USD", "Dólar"),
        ft.dropdown.Option("EUR", "Euro"), 
    ])
    converter_button = ft.ElevatedButton("Converter", icon="ARROW_CIRCLE_RIGHT_OUTLINED", on_click=converter, width=250, bgcolor="white", color="Blue")
    result_text = ft.Text(size=30, font_family="Times New Roman")
    

    page.add(
        ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([valor_input], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([moeda_inicial], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([moeda_final], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([converter_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([result_text], alignment=ft.MainAxisAlignment.CENTER),
        
    )

ft.app(main)
