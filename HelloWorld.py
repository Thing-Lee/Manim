from manimlib.imports import *

class Hello_World(Scene):
    def construct(self):
        
        ##making object
        helloworld = TextMobject("Hello World 你好世界",color = RED)
        
        ##Position
        
        ##Showing object
        self.add(helloworld)
        self.wait(1)
        self.remove(helloworld)
        self.wait(1)
        
        # 从左至右逐一显示
        self.play(Write(helloworld))  
        
        # 从中间向两边扩张显示
        self.play(GrowFromCenter(helloworld))
        
        # 由浅到深显示
        self.play(FadeIn(helloworld),run_time=1)
        
        # 由下到上插入显示
        self.play(FadeInFromDown(helloworld))
        self.wait(1)
