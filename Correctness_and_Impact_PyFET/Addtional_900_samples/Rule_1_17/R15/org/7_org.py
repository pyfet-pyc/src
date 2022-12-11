def test_pack(self):
    """
    Pack multiple vectors into one
    Test intrinsics:
        npyv_pack_b8_b16
        npyv_pack_b8_b32
        npyv_pack_b8_b64
    """
    if self.sfx not in ("b16", "b32", "b64"):
        return
    # create the vectors
    data = self._data()
    rdata = self._data(reverse=True)
    vdata = self._load_b(data)
    vrdata = self._load_b(rdata)
    pack_simd = getattr(self.npyv, f"pack_b8_{self.sfx}")
    # for scalar execution, concatenate the elements of the multiple lists
    # into a single list (spack) and then iterate over the elements of
    # the created list applying a mask to capture the first byte of them.
    if self.sfx == "b16":
        spack = {i: 0xFF for i in (list(rdata) + list(data))}
        vpack = pack_simd(vrdata, vdata)