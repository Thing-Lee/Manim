from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


# class CoordScreen(Scene):
#     def construct(self):
#         screen_grid = ScreenGrid()
#         dot = Dot([1, 1, 0])
#         self.add(screen_grid)
#         self.play(FadeIn(dot))
#         self.wait()

##########################################################################################
##########################################################################################        
##########################################################################################  
      

class Positions(Scene):    
    def construct(self):
        grid=ScreenGrid() #添加网格后加的
        # grid=ScreenGrid(rows = ,columns = )   可指定网格细分程度而非总范围哦      
        
        object = Dot() #定义点
        
        # 绝对位置
        # 绝对位置 边
        object.to_edge(UP)
        object.to_edge(DOWN)
        object.to_edge(RIGHT)
        object.to_edge(LEFT)
        
        # 绝对位置 角
        object.to_corner(UR)
        object.to_corner(UL)
        object.to_corner(DR)
        object.to_corner(DL)
        
        
        
        # 相对位置                
        # 指定点的坐标
        # 法一
        vector = np.array([1,2,0]) #[x,y,z]
        object.move_to(vector)
        
        # 法二
        object.move_to(UP*2+RIGHT)
        object.move_to(3*LEFT+2*DOWN)
        self.add(grid,object)        #显示网格和点
        
        # 添加文字，指定点关于字的相对位置
        # 文字坐标
        ReferenceText = TextMobject("Text")
        ReferenceText.move_to(3*LEFT+2*UP)
        
        # 相对位置
        # 法一
        object.move_to(ReferenceText) #点的坐标与文字坐标相同
        object.move_to(ReferenceText.get_center()+5*RIGHT) #点的坐标是文字坐标向右平移5个单位      
        
        # 法二        
        object.next_to(ReferenceText,RIGHT,buff=5) #定义点的位置在文字的中心位置右边5个单位
        self.add(grid,ReferenceText,object)         #显示网格，文字和点
        
        # 法三 移动
        object.move_to(UR)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        
        self.wait()
        
        
#################################################################################

class Rotations(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4)     #旋转角度
        
        self.play(Write(textM),Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        
class RotateLine(Scene):
    def construct(self):
        grid=ScreenGrid() #添加网格后加的
        object = Dot()
        reobject = Dot([3,3,0])
        reobject.rotate(90*DEGREES,object=[0,3,0])
        self.add(grid,object,reobject)
        self.wait()
        
class Filp(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)
        

#################################################################################

class Fonts(Scene):
    def construct(self):
        textNormal = TextMobject("\\textrm{Roman serif text 012.\\#!?} Text")
        textItalic = TextMobject("\\textit{Italic text 012.\\#!?} Text")
        textTypewriter = TextMobject("\\texttt{Typewritter text 012.\\#!?} Text")
        textBold = TextMobject("\\textbf{Bold text 012.\\#!?} Text")
        textSL = TextMobject("\\textsl{Slanted text 012.\\#!?} Text")
        textSC = TextMobject("\\textsc{Small caps text 012.\\#!?} Text")
        textNormal.to_edge(UP)
        textItalic.next_to(textNormal,DOWN,buff=.5)
        textTypewriter.next_to(textItalic,DOWN,buff=.5)
        textBold.next_to(textTypewriter,DOWN,buff=.5)
        textSL.next_to(textBold,DOWN,buff=.5)
        textSC.next_to(textSL,DOWN,buff=.5)
        self.add(textNormal,textItalic,textTypewriter,textBold,textSL,textSC)
        self.wait(3)

class SizeText(Scene):
    def construct(self):
        textHuge = TextMobject("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = TextMobject("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TextMobject("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TextMobject("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TextMobject("{\\large large Text 012.\\#!?} Text")
        textNormal = TextMobject("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TextMobject("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TextMobject("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TextMobject("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TextMobject("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)
        texthuge.next_to(textHuge,DOWN,buff=0.1)
        textLARGE.next_to(texthuge,DOWN,buff=0.1)
        textLarge.next_to(textLARGE,DOWN,buff=0.1)
        textlarge.next_to(textLarge,DOWN,buff=0.1)
        textNormal.next_to(textlarge,DOWN,buff=0.1)
        textsmall.next_to(textNormal,DOWN,buff=0.1)
        textfootnotesize.next_to(textsmall,DOWN,buff=0.1)
        textscriptsize.next_to(textfootnotesize,DOWN,buff=0.1)
        texttiny.next_to(textscriptsize,DOWN,buff=0.1)
        self.add(textHuge,texthuge,textLARGE,textLarge,textlarge,textNormal,textsmall,textfootnotesize,textscriptsize,texttiny)
        self.wait(3)