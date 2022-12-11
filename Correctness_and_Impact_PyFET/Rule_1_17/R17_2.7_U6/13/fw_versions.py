
def build_fw_dict(fw_versions, filter_brand=None):
  fw_versions_dict = defaultdict(set)
  for fw in fw_versions:
    if filter_brand is None or fw.brand == filter_brand:
      addr = fw.address
      sub_addr = fw.subAddress if fw.subAddress != 0 else None
      fw_versions_dict[(addr, sub_addr)].add(fw.fwVersion)
  return dict(fw_versions_dict)
