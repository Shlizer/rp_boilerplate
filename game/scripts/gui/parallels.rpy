###################################################
## 10
###################################################
transform update_pos_10:
    function update_pos_10_fn

init python:
    def update_pos_10_fn(tf,st,at):
        mx,my=renpy.get_mouse_pos()
        tf.pos=(mx/10,my/10)
        return 0

###################################################
## 16
###################################################
transform update_pos_16:
    function update_pos_16_fn

init python:
    def update_pos_16_fn(tf,st,at):
        mx,my=renpy.get_mouse_pos()
        tf.pos=(mx/16,my/16)
        return 0

###################################################
## 22
###################################################
transform update_pos_22:
    function update_pos_22_fn

init python:
    def update_pos_22_fn(tf,st,at):
        mx,my=renpy.get_mouse_pos()
        tf.pos=(mx/22,my/22)
        return 0

###################################################
## 26
###################################################
transform update_pos_26:
    function update_pos_26_fn

init python:
    def update_pos_26_fn(tf,st,at):
        mx,my=renpy.get_mouse_pos()
        tf.pos=(mx/26,my/26)
        return 0
