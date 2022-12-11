def test_rotation(self):
    os.environ["LOGGERD_TEST"] = "1"
    Params().put("RecordFront", "1")

    expected_files = {"rlog", "qlog", "qcamera.ts", "fcamera.hevc", "dcamera.hevc", "ecamera.hevc"}
