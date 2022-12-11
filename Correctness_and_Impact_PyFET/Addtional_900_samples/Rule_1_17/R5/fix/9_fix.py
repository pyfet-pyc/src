def write(self):
    # Write a file based on https://prometheus.io/docs/guides/file-sd/
    # Write should be atomic. Otherwise, Prometheus raises an error that
    # json file format is invalid because it reads a file when
    # file is re-written. Note that Prometheus still works although we
    # have this error.
    temp_file_name = self.get_temp_file_name()
    f =  open(temp_file_name, "w")
    
    json_file.write(self.get_file_discovery_content())
    # NOTE: os.replace is atomic on both Linux and Windows, so we won't
    # have race condition reading this file.
    os.replace(temp_file_name, self.get_target_file_name())
