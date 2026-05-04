# # 2.31
# from kivy.app import App
# from kivy.uix.textinput import TextInput
#
# class MyApp(App):
#     def build(self):
#         my_text = TextInput(font_size=20)
#         return my_text
#
# MyApp().run()

# # 2.32
# from kivy.app import App
# from kivy.lang import Builder
#
# KV = """
# TextInput:
#     font_size:40
# """
# class MyApp(App):
#     def build(self):
#         return Builder.load_string(KV)
#
# MyApp().run()

# # 2.33
# from kivy.app import App
# from kivy.uix.togglebutton import ToggleButton
#
# class MainApp(App):
#     def build(self):
#         t_but = ToggleButton(text='кнопка',
#         font_size=100)
#
#         return t_but
#
# MainApp().run()

# # 2.34
# from kivy.app import App
# from kivy.lang import Builder
#
# KV = """
# ToggleButton:
#     text: "Кнопка"
#     font_size:40
# """
# class MainApp(App):
#     def build(self):
#         return Builder.load_string(KV)
#
# MainApp().run()

# # 2.35
# from kivy.app import App
# from kivy.lang import Builder
# KV = '''
# BoxLayout:
#     orientation: 'vertical'
#     ToggleButton:
#         text: 'Moskow'
#         group:'city'
#         state:'down'
#     ToggleButton:
#         text: 'Other'
#         group:'city'
#         state:'down'
#     ToggleButton:
#         text: 'Another'
#         group:'city'
#         state:'down'
# '''
#
# class MainApp(App):
#     def build(self):
#         return Builder.load_string(KV)
#
# MainApp().run()
