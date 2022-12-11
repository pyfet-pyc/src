# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.11 (default, Aug 17 2021, 15:56:41) 
# [GCC 10.2.1 20210110]
# Embedded file name: testbed_py/test.py
# Compiled at: 2022-08-13 01:20:29
# Size of source mod 2**32: 1073 bytes


def get_server_version_from_running_container() -> str:
    FET_raise = 0
    try:
        container_name = get_main_container_name()
        version, _ = DOCKER_CLIENT.exec_in_container(container_name,
          interactive=True, command=['bin/localstack', '--version'])
        version = to_str(version).strip().splitlines()[(-1)]
    except ContainerException as e:
        try:
            FET_raise = 1
        finally:
            e = None
            del e

    else:
        FET_null()
    if FET_raise == 1:
        try:
            img_name = get_docker_image_to_start()
            version, _ = DOCKER_CLIENT.run_container(img_name,
              remove=True,
              interactive=True,
              entrypoint='',
              command=[
             'bin/localstack', '--version'])
            version = to_str(version).strip().splitlines()[(-1)]
        except ContainerException:
            image_envs = image_info['Config']['Env']
# okay decompiling testbed_py/test.py
