import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        self._listCountry=self._model.getCountry()
        self._listYear=self._model.getYear()
        for c in self._listCountry:
            self._view.ddcountry.options.append(ft.dropdown.Option(c))
        for a in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        self._view.update_page()


    def handle_graph(self, e):
        country=self._view.ddcountry.value
        if country is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Seleziona un paese"))
            self._view.update_page()
            return
        anno=self._view.ddyear.value

        if anno is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Seleziona un anno"))
            self._view.update_page()
            return

        try:
            annoInt=int(anno)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Il valore inserito non è un intero"))
            self._view.update_page()
            return

        self._model.buildGraph(country,annoInt)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {self._model.getNumNodes()}, Numero archi: {self._model.getNumEdges()}"))
        self._view.update_page()


    def handle_volume(self, e):
        dizionario=self._model.getPesoVicini()
        for d in dizionario:
            self._view.txtOut2.controls.append(ft.Text(f"{d[0]} --> {d[1]}"))
        self._view.update_page()


    def handle_path(self, e):
        pass
