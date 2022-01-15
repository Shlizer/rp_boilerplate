define current_label = None

init -5 python:
    def label_callback(name, abnormal):
        global current_label
        current_label = name
    config.label_callback = label_callback
