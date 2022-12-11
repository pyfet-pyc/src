def voc_info(json_dataset):
    year = json_dataset.name[4:8]
    image_set = json_dataset.name[9:]
    devkit_path = get_devkit_dir(json_dataset.name)
    assert os.path.exists(devkit_path), \
        'Devkit directory {} not found'.format(devkit_path)
    anno_path = os.path.join(
        devkit_path, 'VOC' + year, 'Annotations', '{:s}.xml')
    image_set_path = os.path.join(
        devkit_path, 'VOC' + year, 'ImageSets', 'Main', image_set + '.txt')
    return dict(
        year=year,
        image_set=image_set,
        devkit_path=devkit_path,
        anno_path=anno_path,
        image_set_path=image_set_path)
