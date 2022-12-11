def read_abst(self):
    # version
    self.read_unsigned_char()
    # flags
    self.read_bytes(3)

    self.read_unsigned_int()  # BootstrapinfoVersion
    # Profile,Live,Update,Reserved
    flags = self.read_unsigned_char()
    live = flags & 0x20 != 0
    # time scale
    self.read_unsigned_int()
    # CurrentMediaTime
    self.read_unsigned_long_long()
    # SmpteTimeCodeOffset
    self.read_unsigned_long_long()

    self.read_string()  # MovieIdentifier
    server_count = self.read_unsigned_char()
    # ServerEntryTable
    for i in range(server_count):
        self.read_string()
    quality_count = self.read_unsigned_char()
    # QualityEntryTable
    for i in range(quality_count):
        self.read_string()
    # DrmData
    self.read_string()
    # MetaData
    self.read_string()

    segments_count = self.read_unsigned_char()
    segments = []
    for i in range(segments_count):
        box_size, box_type, box_data = self.read_box_info()
        assert box_type == b'asrt'
        segment = FlvReader(box_data).read_asrt()
        segments.append(segment)
    fragments_run_count = self.read_unsigned_char()
    fragments = []
    for i in range(fragments_run_count):
        box_size, box_type, box_data = self.read_box_info()
        assert box_type == b'afrt'
        fragments.append(FlvReader(box_data).read_afrt())

    return {
        'segments': segments,
        'fragments': fragments,
        'live': live,
    }