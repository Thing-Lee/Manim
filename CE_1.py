from manimlib.imports import *

class TEXT1(Scene):
    def construct(self):
        text1 = TextMobject("SCENE 1")
        self.play(Write(text1))
        self.wait()
        
class TEXT2(Scene):
    def construct(self):
        text2 = TextMobject("SCENE 2")
        self.play(FadeIn(text2))
        self.wait()
        
class TEXT3(Scene):
    def construct(self):
        text3 = TextMobject("SCENE 3")
        self.play(GrowFromCenter(text3))
        self.wait()