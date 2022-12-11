def cellreRecognition(self):
    '''
        re-recognise text in a cell
    '''
    img = cv2.imread(self.filePath)
    for shape in self.canvas.selectedShapes:
        box = [[int(p.x()), int(p.y())] for p in shape.points]

        if len(box) > 4:
            box = self.gen_quad_from_poly(np.array(box))
        assert len(box) == 4

        # pad around bbox for better text recognition accuracy
        _box = boxPad(box, img.shape, 6)
        img_crop = get_rotate_crop_image(img, np.array(_box, np.float32))
        if img_crop is None:
            msg = 'Can not recognise the detection box in ' + self.filePath + '. Please change manually'
            QMessageBox.information(self, "Information", msg)
            return

        # merge the text result in the cell
        texts = ''
        probs = 0. # the probability of the cell is avgerage prob of every text box in the cell
        bboxes = self.ocr.ocr(img_crop, det=True, rec=False, cls=False)
        if len(bboxes) > 0:
            bboxes.reverse() # top row text at first
            for _bbox in bboxes:
                patch = get_rotate_crop_image(img_crop, np.array(_bbox, np.float32))
                rec_res = self.ocr.ocr(patch, det=False, rec=True, cls=False)
                text = rec_res[0][0]
                if text != '':
                    texts += text + ('' if text[0].isalpha() else ' ') # add space between english word
                    probs += rec_res[0][1]
            probs = probs / len(bboxes)
        result = [(texts.strip(), probs)]

        if result[0][0] != '':
            result.insert(0, box)
            print('result in reRec is ', result)
            if result[1][0] == shape.label:
                print('label no change')
            else:
                shape.label = result[1][0]
        else:
            print('Can not recognise the box')
            if self.noLabelText == shape.label:
                print('label no change')
            else:
                shape.label = self.noLabelText
        self.singleLabel(shape)
        self.setDirty()