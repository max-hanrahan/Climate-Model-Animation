from manimlib.imports import *
from math import pi

class Prereq(Scene):
    def construct(self):
        head = TexMobject('\\text{\\underline{Three good things to know:}}', color = GREEN)
        stephboltz = ImageMobject('stephboltz.jpg').shift(2*RIGHT).scale(2)

        line1 = TexMobject('1:')
        rule1 = TexMobject('\\text{P} = \\frac{\\text{E}}{\\Delta\\text{t}}')
        rule2 = TexMobject('\\text{I} = \\frac{\\text{P}}{\\text{A}}')
        line2 = TexMobject('2: ')
        line3 = TexMobject('3: ')
        rule3 = TexMobject('\\text{P} \\propto \\text{T}^4\\text{A}')
        rule4 = TexMobject('\\text{P} = \\sigma \\text{T}^4\\text{A}')

        head.move_to(TOP).shift(DOWN)

        line1.move_to(TOP-2.5*UP).shift(6.5*LEFT)
        line2.move_to(TOP-4.5*UP).shift(6.5*LEFT)
        line3.move_to(TOP-6.5*UP).shift(6.5*LEFT)

        rule1.next_to(line1, RIGHT)
        rule2.next_to(line2, RIGHT)
        rule3.next_to(line3, RIGHT)
        rule4.next_to(line3, RIGHT)

        self.play(GrowFromCenter(head), run_time = 1)
        self.play(FadeIn(rule1), FadeIn(line1), run_time = 2)
        self.play(FadeIn(rule2), FadeIn(line2), run_time = 2)
        self.play(FadeIn(rule3), FadeIn(line3), run_time = 2)
        self.play(Transform(rule3, rule4), run_time = 1)
        self.play(FadeIn(stephboltz), run_time = 1)

class Sun(Scene):
    def construct(self):
        sun = ImageMobject('sun.png').move_to(4 *LEFT)
        sunring = Annulus(inner_radius = 6.8, outer_radius = 6.9, color = RED).move_to(4* LEFT)
        sun.scale(0.5)
        earth = ImageMobject("earth_PNG37.png").move_to(3* RIGHT).scale(0.15)

        earth_sun_rad = Arrow(3.8* LEFT, 3*RIGHT, color = BLUE)
        arrow_group = VGroup(earth_sun_rad)
        brace = Brace(arrow_group, DOWN)
        eq = TexMobject("\\text{d} = 150 \\times 10^{9} \\text{m}")
        eq.shift(DOWN)
        sun_rad = Arrow(.3* UP + 4* LEFT, 4*LEFT + .67* DOWN).set_color(GREEN_SCREEN)
        sun_rad_group = VGroup(sun_rad)
        brace2 = Brace(sun_rad_group, LEFT).set_color(GREEN_SCREEN)
        brace2.shift(.25 *LEFT)
        small_ring = (Annulus(inner_radius = 0.4, outer_radius = .45).move_to(4.02* LEFT)).set_color(GREEN_SCREEN)

        eq1 = TexMobject("\\text{P}_{\\text{emitted}}=\\text{A} \\sigma \\text{T}^4")
        eq2 = TexMobject("\\text{P}_{\\text{emitted}}=4 \\pi \\text{r}^2 \\sigma \\text{T}^4")
        eq3 = TexMobject("\\text{P}_{\\text{emitted}}\\approx 3.8 \\times 10^{26} \\text{W}")
        eq_r = TexMobject("\\text{r} = 7.0 \\times 10^{8} \\text{m}")
        eq_I = TexMobject("\\text{I} = \\frac{\\text{P}_{\\text{emitted}}}{\\text{A}} = \\text{S}")
        eq_I2 = TexMobject("\\text{S} = \\frac{\\text{P}_{\\text{emitted}}}{4\\pi\\text{d}^2}")
        eq_I3 = TexMobject("\\text{S}\\approx 1360 \\frac{\\text{W}}{\\text{m}^2}")

        eq1.move_to(3*UP + 4.7* RIGHT)
        eq2.move_to(3*UP + 4.7* RIGHT)
        eq3.move_to(2.5*UP + 4.2* RIGHT)
        eq_r.shift(5.5* LEFT)
        eq_r.scale(.5)
        eq_I.move_to(1.5*DOWN + 4.7* RIGHT)
        eq_I2.move_to(1.5*DOWN + 4.7* RIGHT)
        eq_I3.move_to(1.5*DOWN + 4.7* RIGHT)

        big_group = VGroup(sunring, eq1, arrow_group, brace, eq, eq_r, eq_I, brace2, sun_rad)

        self.add(sun)
        self.add(earth)
        self.play(GrowFromCenter(sunring), run_time = 2)
        self.wait(1)
        self.play(GrowArrow(earth_sun_rad))
        self.wait(1)
        self.play(GrowFromCenter(brace), Write(eq), run_time = 2)
        self.wait(1)
        self.play(Write(eq1), run_time = 2)
        self.wait(1)
        self.play(GrowArrow(sun_rad), GrowFromCenter(brace2))
        self.wait(1)
        self.play(Write(eq_r), run_time = 2)
        self.wait(1)
        self.play(Transform(eq1, eq2), run_time = 1)
        self.wait(1)
        self.play(Transform(eq1, eq3), run_time = 1)
        self.wait(1)
        self.play(Write(eq_I), run_time = 2)
        self.wait(1)
        self.play(Transform(eq_I, eq_I2), run_time =1)
        self.wait(1)
        self.play(Transform(eq_I, eq_I3), run_time =1)
        self.wait(1)
        self.play(FadeOut(big_group), FadeOut(sun))
        self.wait(1)
        self.play(ApplyMethod(earth.scale, (6.7)))
        self.wait(1)
        self.play(ApplyMethod(earth.move_to, (0)))
        self.wait(1)

class Earth(Scene):
    def construct(self):
        earth = ImageMobject("earth_PNG37.png")
        earth_circ = Circle(radius = 1, color = YELLOW)
        sunwaves = Annulus(inner_radius = 38, outer_radius = 38.2, color = "YELLOW")
        sunwaves.move_to(30*LEFT)

        S_approx = TexMobject("\\text{S} \\approx 1360 \\frac{\\text{W}}{\\text{m}^2}")
        equality = TexMobject('\\text{P}_\\text{in} = \\text{P}_\\text{abs}')
        P_in1 = TexMobject("\\text{P}_\\text{in} = \\text{S}\\text{A}_{disc}")
        P_inPI = TexMobject("\\text{P}_\\text{in} = \\text{S}(\\pi\\text{r}_\\text{e}^2)")
        P_abs = TexMobject("=\\text{P}_{\\text{absorbed}}")
        P_abs1 = TexMobject("\\text{P}_{\\text{abs}} = \\text{I}_\\text{rec}\\text{A}_\\text{sphere}")
        P_absPI= TexMobject("\\text{P}_{\\text{abs}}= \\text{I}_\\text{rec}(4\\pi\\text{r}_\\text{e}^2)")
        equality2 = TexMobject('\\text{S}(\\pi\\text{r}_\\text{e}^2) = \\text{I}_\\text{rec}(4\\pi\\text{r}_\\text{e}^2)')
        equality3 = TexMobject('\\text{S}(\\pi\\text{r}_\\text{e}^2) = \\text{I}_\\text{rec}(4\\pi\\text{r}_\\text{e}^2)').scale(1.2)
        onemore = TexMobject('\\text{S} = \\text{I}_{\\text{rec}}(4)')
        e9 = TexMobject("\\text{I}_\\text{rec} = \\frac{\\text{S}}{4}").move_to(2.5 *RIGHT + 2 * DOWN)
        
        S_approx.move_to(3* UP)
        equality.move_to(3*UP +4.5 *RIGHT)
        P_in1.move_to(UP)
        P_inPI.move_to(UP)
        P_abs1.move_to(UP+4.5 *RIGHT)
        P_absPI.move_to(P_abs1)
        equality2.move_to(2.25*RIGHT)
        equality3.move_to(2.25*RIGHT+UP)
        onemore.move_to(equality3).scale(1.2)
        e9.move_to(equality3)

        earth_rad = Arrow(3* LEFT, 3* LEFT+ 1.2*DOWN)
        radgroup = VGroup(earth_rad)
        brace = Brace(radgroup, LEFT)
        brace.move_to(earth_rad)
        brace.shift(LEFT)
        eq_er = TexMobject("\\text{r}_\\text{e} = 6.38 \\times 10^{8} \\text{m}")
        eq_er.scale(0.6)
        eq_er.shift(5.5* LEFT + .6* DOWN)

        self.add(earth)
        for _ in range(3):
            self.play(GrowFromCenter(sunwaves))
        self.play(ApplyMethod(earth.shift, (3 *LEFT)))
        self.wait(1)

        earth_circ.move_to(earth)
        earth_circ.rotate(pi)
        earth_circ.flip(RIGHT)

        self.play(ShowCreation(earth_circ))
        self.wait(1)
        self.play(Write(S_approx))
        self.wait(1)
        self.play(Write(equality))
        self.wait(1)
        self.play(FadeOut(S_approx),FadeOut(equality))
        self.wait(1)
        self.play(Write(P_in1))
        self.wait(1)
        self.play(Write(P_abs1))
        self.wait(1)
        self.play(Write(eq_er), FadeIn(brace), GrowArrow(earth_rad), run_time = 2)
        self.wait(1)
        self.play(Transform(P_in1, P_inPI))
        self.wait(1)
        self.play(Transform(P_abs1, P_absPI))
        self.wait(1)
        self.play(FadeOut(P_in1), FadeOut(P_abs1), ShowCreation(equality2))
        self.wait(1)
        self.play(Transform(equality2, equality3))
        self.wait(1)
        self.play(Transform(equality2, onemore))
        self.wait(1)
        self.play(Transform(equality2, e9))
        self.wait(1)
        all_group = VGroup(earth_circ, earth_rad, eq_er, brace)
        self.play(FadeOut(all_group))
        self.wait(1)
        I_340 = TexMobject('\\text{I}_\\text{rec}\\approx 340\\frac{\\text{W}}{\\text{m}^2}')
        self.play(Transform(equality2, I_340))
        self.wait(1)

class LightBounce(Scene):
    def construct(self):
        I_340 = TexMobject('\\text{I}_\\text{rec}\\approx 340\\frac{\\text{W}}{\\text{m}^2}')
        earth = ImageMobject("earth_PNG37.png").move_to(3*LEFT)
        BounceArrow1 = Arrow(4 * LEFT + 2*UP, 3 * LEFT + 0.7 *UP).set_color(YELLOW)
        BounceArrow2 = Arrow(3.25 * LEFT + 0.7 *UP, 2.25* LEFT + 2*UP).set_color(YELLOW)
        BounceArrow2_small = Arrow(3.25 * LEFT + 0.7 *UP, 2.55* LEFT + 1.61*UP).set_color(YELLOW)
        earth_glow = Annulus(inner_radius = 0, outer_radius = .95, fill_color = YELLOW, fill_opacity = 0.3).move_to(earth)
        eq_a =TexMobject('\\alpha = 0.3').move_to(UP +0.5*RIGHT)
        eq_strue = TexMobject('\\text{I}_\\text{abs} = (1-\\alpha)\\text{I}_\\text{rec}').move_to(1.5*RIGHT)
        eq_s2 = TexMobject('\\text{I}_\\text{abs} = 238 \\frac{\\text{W}}{\\text{m}^2}').move_to(1.1*RIGHT +DOWN)

        self.add(I_340)
        self.play(ShowCreation(earth))
        self.wait(1)
        self.play(FadeOut(I_340))
        self.wait(1)
        # self.wait(0)
        self.play(GrowArrow(BounceArrow1))
        self.wait(1)
        self.play(GrowArrow(BounceArrow2))
        self.wait(1)
        self.play(Transform(BounceArrow2, BounceArrow2_small))
        self.wait(1)
        self.play(FadeIn(earth_glow))
        self.wait(1)

        self.play(FadeIn(eq_a, run_time = 1))
        self.play(FadeIn(eq_strue, run_time = 1.5))
        self.play(FadeIn(eq_s2, run_time = 1))
        self.wait(3)

class MathBreak(Scene):
    def construct(self):
        head = TexMobject('\\text{Math Break!}').move_to(3* UP +4* LEFT).scale(1.5).set_color(BLUE)
        E_cons1 = TexMobject('\\Sigma\\text{P} =\\text{I}_\\text{abs}\\text{A}')
        E_cons2 = TexMobject('=\\sigma\\text{T}^4\\text{A}')
        sb1 = TexMobject('\\text{I}_\\text{abs}= \\sigma\\text{T}^4')
        sb12 = TexMobject('\\text{I}_\\text{abs} = \\sigma\\text{T}^4')
        I_rec_last = TexMobject('\\text{I}_\\text{rec}(1-\\alpha)= \\sigma\\text{T}^4')
        penult = TexMobject('\\frac{\\text{S}(1-\\alpha)}{4}=\\sigma\\text{T}^4')
        albedo_fin = TexMobject('\\text{T}=\\sqrt[\\leftroot{-2}\\uproot{2}4]{\\frac{{\\text{S}(1-\\alpha)}}{4\\sigma}}').move_to(2*DOWN)
        bigger = TexMobject('\\text{T}=\\sqrt[\\leftroot{-2}\\uproot{2}4]{\\frac{{\\text{S}(1-\\alpha)}}{4\\sigma}}').scale(1.4) # I hate this workaround
      
        E_cons1.move_to(head).shift(DOWN)
        E_cons2.move_to(head).shift(2.25*RIGHT+.9*DOWN)
        E_group = VGroup(E_cons1, E_cons2)
        sb1.move_to(head).shift(2*DOWN+1.5*RIGHT)
        stephbotlzg = VGroup(sb1)
        sb12.move_to(sb1).shift(UP)
        I_rec_last.move_to(sb12)
        penult.move_to(I_rec_last)

        self.play(Write(head))
        self.wait(1)
        self.play(Write(E_cons1))
        self.wait(1)
        self.play(Write(E_cons2))
        self.wait(1)
        self.play(Write(sb1))
        self.wait(1)
        self.play(FadeOut(E_group), Transform(sb1, sb12))
        self.wait(1)
        self.play(Transform(sb1, I_rec_last))
        self.wait(1)
        self.play(Transform(sb1, penult))
        self.wait(1)
        self.play(FadeOut(sb1), Write(albedo_fin))
        self.wait(1)
        self.play(Transform(albedo_fin, bigger))
        self.wait(1)

class GHGLayers(Scene):
    def construct(self):
        green_height = -2
        blue_height = 0

        orange_x = -4
        blue_x = 0
        green_x = 4

        sun = ImageMobject('sun.png').move_to(TOP-UP + 4*LEFT).scale(0.5)
        flowers = ImageMobject('dorky_flowers.png').move_to((orange_x-1, green_height+.4, 0)).scale(0.4)
        worldline = Line(start = (-7, -2, 0), end = (7,-2,0), color = GREEN)
        atmos = Line(start = (-7, blue_height, 0), end = (7,blue_height,0), color = BLUE, fill_opacity = 0.8)
        in_arrow = Arrow(start =(TOP-1.2*UP + orange_x*RIGHT), end = (TOP -6.2*UP+orange_x*RIGHT), color = ORANGE)
        out_arrow = Arrow(start = (blue_x, blue_height-.2, 0), end = (blue_x, 2.2, 0), color = BLUE)  
        blue_green = Arrow(start = (0.2+blue_x, blue_height+0.2, 0), end =(0.2+blue_x, green_height -.2, 0), color = BLUE)
        GH_arrow = Arrow(start = (green_x, green_height-.2, 0), end = (green_x, blue_height+0.2, 0), color = GREEN)

        note_in = TexMobject('\\text{I}_\\text{in}', color = ORANGE)
        note_out = TexMobject('\\text{I}_\\text{out}', color = BLUE)
        num_in = TexMobject('240\\frac{\\text{W}}{m^2}', color = ORANGE)
        num_out = TexMobject('240\\frac{\\text{W}}{m^2}', color = BLUE)
        note_reflec = TexMobject('=\\text{I}_\\text{out}', color = BLUE)
        note_GHG = TexMobject('= \\text{I}_\\text{in} + \\text{I}_\\text{out}', color = GREEN)
        num_reflec = TexMobject('240\\frac{\\text{W}}{m^2}', color = BLUE)
        num_GHG = TexMobject('480\\frac{\\text{W}}{m^2}', color = GREEN)


        note_in.move_to((-5, 1, 0))
        note_out.move_to((-1, 1, 0))
        num_in.move_to(note_in)
        num_out.move_to(note_out)
        note_reflec.move_to(note_out).shift(2*DOWN)
        note_GHG.move_to(GH_arrow).shift(1.5*RIGHT)
        num_reflec.move_to(note_reflec)
        num_GHG.move_to(note_GHG)

        thicc_group = VGroup(in_arrow, out_arrow, blue_green, GH_arrow, note_reflec, note_in, note_out, note_GHG, atmos)

        self.add(sun)
        self.add(worldline)
        self.play(ShowCreation(sun), FadeIn(worldline), FadeIn(flowers))
        self.play(GrowArrow(in_arrow))
        self.play(FadeIn(atmos))
        self.play(GrowArrow(out_arrow))
        self.play(Write(note_in))
        self.play(Write(note_out))
        self.play(GrowArrow(blue_green))
        self.play(Write(note_reflec))
        self.play(GrowArrow(GH_arrow))
        self.play(Write(note_GHG))
        self.play(Transform(note_in, num_in), Transform(note_out, num_out))
        self.play(Transform(note_reflec, num_reflec))
        self.play(Transform(note_GHG, num_GHG))
        self.play(FadeOut(thicc_group))

class TwoLayers(Scene):
    def construct(self):
        green_height = -2
        blue_height = -.5
        yellow_height = 1

        orange_x = -4
        yellow_x = -1
        blue_x = 2
        green_x = 5

        sun = ImageMobject('sun.png').move_to(TOP-UP + 4*LEFT).scale(0.5)
        flowers = ImageMobject('dorky_flowers.png').move_to((orange_x-1, green_height+.4, 0)).scale(0.4)

        worldline = Line(start = (-7, -2, 0), end = (7,-2,0), color = GREEN)
        atmos = Line(start = (-7, blue_height, 0), end = (7,blue_height,0), color = BLUE, fill_opacity = 0.8)
        atmos2 = Line(start = (-7, yellow_height, 0), end = (7,yellow_height,0), color = YELLOW)
        in_arrow = Arrow(start =(TOP-1.2*UP + orange_x*RIGHT), end = (TOP -6.2*UP+orange_x*RIGHT), color = ORANGE)
        blue_yellow = Arrow(start = (blue_x, blue_height-.2, 0), end = (blue_x, yellow_height+.2, 0), color = BLUE)  
        blue_green = Arrow(start = (0.2+blue_x, blue_height+0.2, 0), end =(0.2+blue_x, green_height -.2, 0), color = BLUE)
        GH_arrow = Arrow(start = (green_x, green_height-.2, 0), end = (green_x, blue_height+0.2, 0), color = GREEN)
        top_arrow = Arrow(start = (yellow_x, yellow_height-0.2, 0), end = (yellow_x, yellow_height+2, 0), color = YELLOW)
        top_down = Arrow(start = (yellow_x+0.2, yellow_height+.2, 0), end = (yellow_x+0.2, blue_height-.2, 0), color = YELLOW)

        I_in = TexMobject('\\text{I}', color = ORANGE)
        I_out = TexMobject('\\text{I}', color = YELLOW)
        I_out_equiv = TexMobject('\\text{I}', color = YELLOW)
        I_down1 = TexMobject('2\\text{I}', color = BLUE)
        I_down2 = TexMobject('2\\text{I}', color = BLUE)
        I_GH = TexMobject('3\\text{I}', color = GREEN)
        mag_up1 = TexMobject('\\text{I}+', color = ORANGE)
        mag_up2 = TexMobject('\\text{I}', color = YELLOW)
        mag_ghg1 = TexMobject('2\\text{I}+', color = BLUE)
        mag_ghg2 = TexMobject('\\text{I}', color = RED)

        I_in.move_to((-4.5, 1.5, 0))
        I_out.move_to(top_arrow).shift(RIGHT+0.5*DL)
        I_down1.move_to(blue_yellow).shift(0.5*RIGHT)
        I_down2.move_to(blue_green).shift(0.5*RIGHT)
        I_GH.move_to(GH_arrow).shift(0.5*RIGHT)
        I_out_equiv.move_to(top_down).shift(0.5*RIGHT)
        mag_up1.move_to(blue_yellow).shift(RIGHT)
        mag_up2.move_to(mag_up1).shift(RIGHT*.5)
        mag_ghg1.move_to(I_GH)
        mag_ghg2.move_to(I_GH).shift(.5*RIGHT)

        self.add(sun, flowers)
        self.add(worldline)
        self.play(ShowCreation(sun))
        self.play(FadeIn(atmos))
        self.play(FadeIn(atmos2))
        self.play(GrowArrow(in_arrow))
        self.play(GrowArrow(top_arrow))
        self.play(Write(I_in), Write(I_out))
        self.play(GrowArrow(top_down))
        self.play(Write(I_out_equiv))
        self.play(GrowArrow(blue_yellow))
        self.play(Write(mag_up1), Write(mag_up2))
        self.play(Transform(mag_up1, I_down1), Transform(mag_up2, I_down1))
        self.play(GrowArrow(blue_green))
        self.play(Write(I_down2))
        self.play(GrowArrow(GH_arrow))
        self.play(Write(mag_ghg1), Write(mag_ghg2))
        self.play(Transform(mag_ghg1, I_GH), Transform(mag_ghg2, I_GH))
        thicc_group = VGroup(I_in, I_out, I_out_equiv, I_down1, I_down2, I_GH, mag_up1, mag_up2, mag_ghg2, mag_ghg1)
        thiccc_group = VGroup(worldline, atmos, atmos2, in_arrow, blue_green, blue_yellow, GH_arrow, top_down, top_arrow)
        self.play(FadeOut(thicc_group), FadeOut(thiccc_group), FadeOut(flowers))

class Rainbows(Scene):
    def construct(self):
        orange_height = 1
        yellow_height = 0
        green_height = -1
        blue_height = -2
        purple_height = -3

        red_x = -5
        orange_x = -3
        yellow_x = -1
        green_x = 1
        blue_x = 3
        purple_x =5

        sun = ImageMobject('sun.png').move_to(TOP-UP + 4*LEFT).scale(0.5)
        worldline = Line(start = (-7, purple_height, 0), end = (7,purple_height,0), color = PURPLE)
        atmos_o = Line(start = (-7, orange_height, 0), end = (7,orange_height,0), color = ORANGE)
        atmos_y = Line(start = (-7, yellow_height, 0), end = (7,yellow_height,0), color = YELLOW)
        atmos_g = Line(start = (-7, green_height, 0), end = (7,green_height,0), color = GREEN)
        atmos_b = Line(start = (-7, blue_height, 0), end = (7,blue_height,0), color = BLUE)

        layer_group = VGroup(atmos_o, atmos_y, atmos_g)

        in_arrow = Arrow(start =(TOP-1.2*UP + red_x*RIGHT), end = ((purple_height-.2)*UP+red_x*RIGHT), color = RED)
        orange_up = Arrow(start = (orange_x, orange_height-0.2, 0), end = (orange_x, orange_height+1.2, 0), color = ORANGE)
        orange_yellow = Arrow(start = (orange_x+.2, orange_height+.2, 0), end = (orange_x+.2, yellow_height-.2, 0), color = ORANGE) 
        yellow_orange = Arrow(start = (yellow_x, yellow_height-0.2, 0), end = (yellow_x, orange_height+.2, 0), color = YELLOW)
        green_yellow = Arrow(start = (green_x, green_height-.2, 0), end = (green_x, yellow_height+.2, 0), color = GREEN)
        blue_green = Arrow(start = (blue_x, blue_height-0.2, 0), end =(blue_x, green_height +.2, 0), color = BLUE)
        blue_purple = Arrow(start = (blue_x+.2, blue_height+0.2, 0), end = (blue_x+.2, purple_height-0.2, 0), color = BLUE)
        green_blue = Arrow(start = (green_x+.2, green_height+.2, 0), end = (green_x+.2, blue_height-0.2, 0), color = GREEN)
        yellow_green = Arrow(start = (yellow_x+.2, yellow_height+.2, 0), end = (yellow_x+.2, green_height-.2, 0), color = YELLOW)
        purple_up = Arrow(start = (purple_x, purple_height-.2, 0), end = (purple_x, blue_height+.2, 0), color = PURPLE)

        arrow_group = VGroup(
            in_arrow, orange_up, orange_yellow, yellow_orange, green_yellow, 
            blue_green, blue_purple, green_blue, yellow_green)

        I_in = TexMobject('\\text{I}', color = RED).move_to((red_x-.5, purple_height+.5, 0))
        I_out = TexMobject('\\text{I}', color = ORANGE).move_to((orange_x-.5, orange_height+.7, 0))
        I_oy = TexMobject('\\text{I}', color = ORANGE).move_to(orange_yellow).shift(.5*LEFT)
        I_yo = TexMobject('2\\text{I}', color = YELLOW).move_to(yellow_orange).shift(.5*LEFT)
        I_yg = TexMobject('2\\text{I}', color = YELLOW).move_to(yellow_green).shift(.5*LEFT)
        I_gy = TexMobject('3\\text{I}', color = GREEN).move_to(green_yellow).shift(.5*LEFT)
        I_gb = TexMobject('3\\text{I}', color = GREEN).move_to(green_blue).shift(.5*LEFT)
        I_bg = TexMobject('4\\text{I}', color = BLUE).move_to(blue_green).shift(.5*LEFT)
        I_bp = TexMobject('4\\text{I}', color = BLUE).move_to(blue_purple).shift(.5*LEFT)
        I_pb = TexMobject('5\\text{I}', color = PURPLE).move_to(purple_up).shift(.5*LEFT)

        I_GH = TexMobject('\\text{I}_\\text{GH}', color = PURPLE).move_to(I_pb).shift(.25*LEFT)
        I_gen = TexMobject('\\text{I}_\\text{GH} = (n+1)\\text{I}').move_to((-1, 2, 0)).scale(1.2)
        I_sig = TexMobject('(n+1)\\frac{\\text{S}(1-\\alpha)}{4}= \\sigma\\text{T}^4 ').move_to((0, 1, 0)).scale(1.2)
        T_4 = TexMobject('(n+1)\\frac{\\text{S}(1-\\alpha)}{4\\sigma}=\\text{T}^4').move_to((.25, 2, 0)).scale(1.2)

        fin = TexMobject('\\text{T}=\\sqrt[\\leftroot{-2}\\uproot{2}4]{\\frac{{(n+1)\\text{S}(1-\\alpha)}}{4\\sigma}}')
        big = TexMobject('\\text{T}=\\sqrt[\\leftroot{-2}\\uproot{2}4]{\\frac{{(n+1)\\text{S}(1-\\alpha)}}{4\\sigma}}')

        fin.scale(1.2).move_to(2*DOWN).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        big.scale(2).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        y_up1 = TexMobject('\\text{I}+', color = ORANGE).move_to(I_yo).shift(0.2*LEFT)
        y_up2 = TexMobject('\\text{I}', color = RED).move_to(y_up1).shift(.4*RIGHT)
        g_up1 = TexMobject('2\\text{I}+', color = YELLOW).move_to(I_gy).shift(0.2*LEFT)
        g_up2 = TexMobject('\\text{I}', color = RED).move_to(g_up1).shift(.5*RIGHT)
        b_up1 = TexMobject('3\\text{I}+', color = GREEN).move_to(I_bg).shift(0.2*LEFT)
        b_up2 = TexMobject('\\text{I}', color = RED).move_to(b_up1).shift(.5*RIGHT)
        p_up1 = TexMobject('4\\text{I}+', color = BLUE).move_to(I_pb).shift(0.2*LEFT)
        p_up2 = TexMobject('\\text{I}', color = RED).move_to(p_up1).shift(.5*RIGHT)

        eq_group = VGroup(I_in, I_out, I_oy, I_yg, I_gb, I_bp, y_up1, y_up2, g_up1, g_up2, b_up1, b_up2)
        the_rest = VGroup(atmos_b, worldline, p_up1, p_up2, purple_up)

        self.add(sun)
        self.play(ApplyMethod(sun.move_to, TOP-UP +red_x*RIGHT))
        self.play(FadeIn(worldline))
        self.play(FadeIn(atmos_b))
        self.play(FadeIn(atmos_g))
        self.play(FadeIn(atmos_y))
        self.play(FadeIn(atmos_o))

        self.play(GrowArrow(in_arrow))
        self.play(GrowArrow(orange_up))
        self.play(Write(I_in), Write(I_out))

        self.play(GrowArrow(orange_yellow), FadeIn(I_oy))
        self.play(GrowArrow(yellow_orange))
        self.play(Write(y_up1), Write(y_up2))
        self.play(Transform(y_up1, I_yo), Transform(y_up2, I_yo))

        self.play(GrowArrow(yellow_green), FadeIn(I_yg))
        self.play(GrowArrow(green_yellow))
        self.play(Write(g_up1), Write(g_up2))
        self.play(Transform(g_up1, I_gy), Transform(g_up2, I_gy))

        self.play(GrowArrow(green_blue), FadeIn(I_gb))
        self.play(GrowArrow(blue_green))
        self.play(Write(b_up1), Write(b_up2))
        self.play(Transform(b_up1, I_bg), Transform(b_up2, I_bg))

        self.play(GrowArrow(blue_purple), FadeIn(I_bp))
        self.play(GrowArrow(purple_up))
        self.play(Write(p_up1), Write(p_up2))
        self.play(Transform(p_up1, I_pb), Transform(p_up2, I_pb))

        self.play(FadeOut(eq_group), Transform(p_up1, I_GH), Transform(p_up2, I_GH))
        self.play(FadeOut(arrow_group))
        self.play(FadeOut(atmos_o),Write(I_gen))
        self.play(FadeIn(I_sig))
        self.play(FadeOut(atmos_y), FadeOut(I_gen), ApplyMethod(I_sig.shift, UP))
        self.play(FadeOut(atmos_g), Transform(I_sig, T_4))
        self.play(FadeOut(the_rest), FadeOut(sun))
        self.play(FadeOut(I_sig), Write(fin))
        self.play(Transform(fin, big))

class FinalQuote(Scene):
    def construct(self):
        quote1 = TexMobject('\\text{"All models are }', '\\text{wrong,}').set_color_by_tex('wrong', RED)
        quote2 = TexMobject('\\text{but }', '\\text{some are useful."}').set_color_by_tex('some', YELLOW)

        quote1.scale(1.2)
        quote1.shift(2 * RIGHT + UP)
        
        quote2.scale(1.2)
        quote2.shift(2 * RIGHT + 0.2*UP)

        image = ImageMobject("g_box.jpg")
        image.set_height(5)
        image.to_corner(UL)

        name = TextMobject("George E. P. Box")
        name.scale(1.5)
        name.next_to(image, DOWN)
        name.shift_onto_screen()
        self.wait(1)
        self.play(FadeIn(image), FadeIn(name))
        self.wait(1)
        self.play(Write(quote1))
        self.play(Write(quote2))

