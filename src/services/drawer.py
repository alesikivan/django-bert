from matplotlib import pyplot as plt
from matplotlib import patches

class Drawer:
    @staticmethod
    def draw_mathplot(FocusArea, X2):
        figure, ax = plt.subplots(1)
        ax.scatter(X2[:,1], X2[:,2])
        #plt.xlim([-7,7]); plt.ylim([-7,7])
        rect = patches.Rectangle(FocusArea[0], FocusArea[1][0], FocusArea[1][1], edgecolor='r', facecolor="none")
        ax.add_patch(rect)
        plt.show()
