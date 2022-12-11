# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/layer_utils_test.py
# Compiled at: 2022-08-11 20:14:04
# Size of source mod 2**32: 926 bytes


def test_print_summary(self):
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(filters=2,
      kernel_size=(2, 3),
      input_shape=(3, 5, 5),
      name='conv'))
    model.add(keras.layers.Flatten(name='flat'))
    model.add(keras.layers.Dense(5, name='dense'))
    file_name = 'model_1.txt'
    temp_dir = self.get_temp_dir()
    self.addCleanup((shutil.rmtree), temp_dir, ignore_errors=True)
    fpath = os.path.join(temp_dir, file_name)
    writer = open(fpath, 'w')

    def print_to_file(text):
        print(text, file=writer)

    try:
        layer_utils.print_summary(model, print_fn=print_to_file)
        self.assertTrue(tf.io.gfile.exists(fpath))
        writer.close()
        reader = open(fpath, 'r')
        lines = reader.readlines()
        reader.close()
        self.assertEqual(len(lines), 15)
    except ImportError:
        pass
# okay decompiling testbed_py/layer_utils_test.py
