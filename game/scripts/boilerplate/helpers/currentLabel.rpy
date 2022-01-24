define current_label = None

init -5 python:
    def label_callback(name, abnormal):
        global current_label
        print "LABEL : " + name
        current_label = name
    config.label_callback = label_callback
