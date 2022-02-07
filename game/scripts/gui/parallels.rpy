###################################################
## X
###################################################
transform float_with_mouse(x):
    function float_with_mouse_fn(x)

init python:
    def float_with_mouse_fn(x):
        def float_with_mouse_fn_inner(tf,st,at):
            mx,my=renpy.get_mouse_pos()
            tf.pos=(mx/x,my/x)
            return 0
        return float_with_mouse_fn_inner
       