def generateColors(c_sorted, frame, row):
    global df, img_list
    height = 25
    img = np.zeros((height, len(c_sorted), 3), np.uint8)
    for x in range(0, len(c_sorted)):
        r, g, b = c_sorted[x][0] * 255, c_sorted[x][1] * 255, c_sorted[x][2] * 255
        c = [r, g, b]
        df.append(c)
        img[:, x] = c  # the color value for the xth column , this gives the color band
        frame[row, x] = c  # changes added for every row in the frame

    createDataSet(data=df)
    return img, frame