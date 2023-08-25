from manimlib.imports import *
# python manim.py E:\Manim_File\CE-Tutorial\CE_2_basic_animations.py -pl
# 无动画
class NoAnimations(Scene):
    """
    这个scene是没有动画的
    如果不添加self.wait(...)和self.play(...)
    如果非要渲染个什么,在cmd中加 -s 或 -ps可渲染出图片
    """
    def construct(self):
        text = TextMobject("Hello world")
        self.add(text)
        # self.wait()
        # self.remove(text)


# 基础动画
class BasicAnimations(Scene):
    def construct(self):
        text = TextMobject("Hello world")
        self.play(Write(text))      #写入效果
        self.play(FadeIn(text))     #淡入效果
        self.play(GrowFromCenter(text))     #从中扩散效果
        self.play(FadeInFromLarge(text, scale_factor=2))     #由大变小效果


# 基础流程 写入 颜色 擦除
class BasicProgression(Scene):
    def construct(self):
        text = TextMobject("Hello world")
        self.play(Write(text))      #写入
        self.wait() 
        self.play(FadeToColor(text,RED))       #渐变为红色
        self.wait()
        self.play(FadeOut(text))        #淡出擦除
        self.wait()
            

# 画圆 参考代码 example_scenes\SquareToCircle        
class ChangeDuration(Scene):
    def construct(self):
        circle = Circle()
        self.play(ShowCreation(circle))     #均匀画圆
        self.play(Write(circle))        #写入画圆
        self.play(FadeIn(circle))       #淡入显现
        self.play(FadeToColor(circle,BLUE))         #渐变色
        

#基本图形的参数设置 形状 时间 画法
class ChangeDurationMultipleAnimations(Scene):
    def construct(self):
        self.play(
            ShowCreation(
                Circle(),       #画圆
                run_time=3,     #持续时间
                rate_func=smooth        
            ),
            FadeIn(
                Square(),
                run_time=2,
                rate_func=there_and_back
            ),
            GrowFromCenter(
                Triangle()
            )
        )
        self.wait()
        

#更丰富的动画 旋转 突出 勾画等
class MoreAnimations(Scene):
    def construct(self):
        text = Text("Hello world")
        self.play(Write(text))      #写入
        self.wait()
        self.play(Rotate(text,PI/2))        #旋转90°
        self.wait()
        self.play(Indicate(text))       #放大且变色
        self.wait()
        self.play(FocusOn(text))        #聚焦
        self.wait()
        self.play(ShowCreationThenDestructionAround(text))      #线条圈画
        self.wait()
        