from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class KMeansLayout(FloatLayout):
    pass

class KMeansApp(App):
    def build(self):
        kmeans_layout = KMeansLayout()
        return kmeans_layout

if __name__ == '__main__':
    KMeansApp().run()