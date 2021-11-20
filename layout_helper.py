loginscreen_helper = """
ScreenManager:
    id: smn
    HelloScreen:
    MainScreen:

<HelloScreen>:
    id: screen1
    name: 'hello_user'
    username: username
    password: password

    FloatLayout:
        Image:
            source: "data-visualization-tools-concept_one.png"
            align: 'top'
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        BoxLayout:
            orientation: "vertical"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            size: root.width, root.height

            MDTextField:
                hint_text: "Username"
                id: username
                pos_hint: {'center_x': 0.5, 'center_y': 1}
                size_hint_x: None
                width: 220
                multiline:False

            MDTextField:
                hint_text: "Password"
                id: password
                pos_hint: {'center_x': 0.5, 'center_y': 0.1}
                size_hint_x: None
                width: 220
                multiline:False

            MDRectangleFlatButton:
                ripple_color: .5, .5, .8, .6
                background_color: 0, 0, 0, 0
                text: "Submit"
                pos_hint: {'center_x': 0.5, 'center_y': .1}
                size_hint_x: None
                on_release: root.loginbtn()

<MainScreen>:
    id: screen2
    name: 'main'
"""