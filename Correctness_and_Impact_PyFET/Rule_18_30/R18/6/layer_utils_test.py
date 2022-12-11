

def test_print_summary(self):
    model = keras.Sequential()
    model.add(
        keras.layers.Conv2D(
            filters=2,
            kernel_size=(2, 3),
            input_shape=(3, 5, 5),
            name="conv",
        )
    )
    model.add(keras.layers.Flatten(name="flat"))
    model.add(keras.layers.Dense(5, name="dense"))

    file_name = "model_1.txt"
    temp_dir = self.get_temp_dir()
    self.addCleanup(shutil.rmtree, temp_dir, ignore_errors=True)
    fpath = os.path.join(temp_dir, file_name)
    writer = open(fpath, "w")

    def print_to_file(text):
        print(text, file=writer)

    try:
        layer_utils.print_summary(model, print_fn=print_to_file)
        self.assertTrue(tf.io.gfile.exists(fpath))
        writer.close()
        reader = open(fpath, "r")
        lines = reader.readlines()
        reader.close()
        self.assertEqual(len(lines), 15)
    except ImportError:
        pass