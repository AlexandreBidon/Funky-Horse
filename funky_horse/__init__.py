from .random_color_palette import RandomColorPalette
import os, random
from cairosvg import svg2png


class FunkyHorse():

    def __init__(self):
        self.svg_list = []
        self.__create()

    def __create(self):
        self.svg_list.clear()
        self.color_palette = RandomColorPalette()
        self.svg_list.append("""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 2006.3 2006.3">\n""")
        self.svg_list.append("""<defs><clipPath id="clip-path"><circle cx="1003.15" cy="1003.15" r="1003.15"/></clipPath>""")
        self.svg_list.append(self.color_palette.generate_svg_style())
        self.svg_list.append("</defs>")

        #Adds the background
        background = random.choice( os.listdir( os.path.join(os.path.dirname(__file__), "assets\\background"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__),"assets\\background\\" + background)) as svg :
            self.svg_list.append(svg.read())

        #Adds the BG Hair
        hair = random.choice(os.listdir( os.path.join(os.path.dirname(__file__), "assets\\hair"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__),"assets\\hair\\{}\\bg.svg".format(hair))) as svg :
            self.svg_list.append(svg.read())

        #Adds the left ear
        ears = random.choice(os.listdir( os.path.join(os.path.dirname(__file__), "assets\\ears"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__),"assets\\ears\\{}\\bg.svg".format(ears))) as svg :
            self.svg_list.append(svg.read())

        #Adds the main body
        body = random.choice(os.listdir( os.path.join(os.path.dirname(__file__), "assets\\body"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__), "assets\\body\\" + body)) as svg :
            self.svg_list.append(svg.read())

        #Adds the eyes
        eyes = random.choice(os.listdir( os.path.join(os.path.dirname(__file__), "assets\\eyes"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__), "assets\\eyes\\" + eyes)) as svg :
            self.svg_list.append(svg.read())

        #Adds the muzzle
        muzzle = random.choice(os.listdir( os.path.join(os.path.dirname(__file__),"assets\\muzzle"))) #change dir name to whatever

        with open(os.path.join(os.path.dirname(__file__), "assets\\muzzle\\" + muzzle)) as svg :
            self.svg_list.append(svg.read())

        #Adds the FG Hair

        with open(os.path.join(os.path.dirname(__file__), "assets\\hair\\{}\\fg.svg".format(hair))) as svg :
            self.svg_list.append(svg.read())

        #Adds the right ear

        with open(os.path.join(os.path.dirname(__file__),"assets\\ears\\{}\\fg.svg".format(ears))) as svg :
            self.svg_list.append(svg.read())

        #adds the accessory
        if random.randrange(0,10) > 5 :
            accessory = random.choice(os.listdir( os.path.join(os.path.dirname(__file__),"assets\\accessory"))) #change dir name to whatever

            with open(os.path.join(os.path.dirname(__file__), "assets\\accessory\\" + accessory)) as svg :
                self.svg_list.append(svg.read())

        self.svg_list.append("</svg>")

        

    def __str__(self):

        """
        Returns the entire drawing by joining list elements.
        """

        return("".join(self.svg_list))

    def save_svg(self, path):

        """
        Saves the SVG drawing to specified path.
        Let any exceptions propagate up to calling code.
        """

        f = open(path, "w+")

        f.write(self.__str__())

        f.close()
    
    def save_png(self, write_to):
        svg2png( self.__str__(), write_to= write_to)




