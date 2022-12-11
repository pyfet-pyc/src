def convert(json_file, output_dir):
    print('Reading: {}'.format(json_file))
    with open(json_file, 'r') as fid:
        dt = json.load(fid)
    print('done!')

    test_image_info = get_ann_fn('coco_2017_test')
    with open(test_image_info, 'r') as fid:
        info_test = json.load(fid)
    image_test = info_test['images']
    image_test_id = [i['id'] for i in image_test]
    print('{} has {} images'.format(test_image_info, len(image_test_id)))

    test_dev_image_info = get_ann_fn('coco_2017_test-dev')
    with open(test_dev_image_info, 'r') as fid:
        info_testdev = json.load(fid)
    image_testdev = info_testdev['images']
    image_testdev_id = [i['id'] for i in image_testdev]
    print('{} has {} images'.format(test_dev_image_info, len(image_testdev_id)))

    dt_testdev = []
    print('Filtering test-dev from test...')
    t = Timer()
    t.tic()
    for i in range(len(dt)):
        if i % 1000 == 0:
            print('{}/{}'.format(i, len(dt)))
        if dt[i]['image_id'] in image_testdev_id:
            dt_testdev.append(dt[i])
    print('Done filtering ({:2}s)!'.format(t.toc()))

    filename, file_extension = os.path.splitext(os.path.basename(json_file))
    filename = filename + '_test-dev'
    filename = os.path.join(output_dir, filename + file_extension)
    with open(filename, 'w') as fid:
        info_test = json.dump(dt_testdev, fid)
    print('Done writing: {}!'.format(filename))