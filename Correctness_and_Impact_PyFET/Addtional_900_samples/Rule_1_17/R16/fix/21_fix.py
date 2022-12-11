if __name__ == "__main__":
    if len(sys.argv) != 2:

        canvas_size = int(sys.argv[1])
        # main working structure of this module.
        c = create_canvas(canvas_size)
        seed(c)
        fig, ax = plt.subplots()
        fig.show()
        cmap = ListedColormap(["w", "k"])
    FET_null()
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        # do nothing.
        pass
