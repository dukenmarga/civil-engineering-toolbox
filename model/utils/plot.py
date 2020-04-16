import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
from io import BytesIO
import base64

class Plot:
    """ Generate image plot
    """
    def __init__(self):
        pass

    def pcolor(self, x, y, z):
        img = BytesIO()
        plt.pcolor(x, y, z)
        plt.colorbar(orientation="horizontal")
        plt.savefig(img, format='png')
        return self.encode_base64(img)
        
    def line(self, x, y, xlabel="X", ylabel="Y", title="X vs Y"):
        img = BytesIO()
        plt.plot(x, y, linewidth=2)
        plt.grid(True)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        # plt.ylim( (0,x[2]+0.1) )
        # plt.xlim( (0,8.1) )
        return self.encode_base64(img)
        
    def encode_base64(self, img):
        plt.savefig(img, format='png')
        plt.clf()
        return base64.b64encode(img.getvalue())
